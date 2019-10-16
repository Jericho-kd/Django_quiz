from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.template import RequestContext
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import CardSet


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class CardSetListView(generic.ListView):
    model = CardSet
    context_object_name = 'card_set_list'
    template_name = 'home.html'


@method_decorator(login_required, name='dispatch')
class CardListView(generic.ListView):
    model = CardSet
    context_object_name = 'card_set'
    template_name = 'quiz.html'

    def get_queryset(self, *args, **kwargs):
        return CardSet.objects.get(pk=self.kwargs['pk'])


def is_correct_answer(answers, request):
    correct = True
    for answer in answers:
        was_given = str(answer.pk) in request.POST
        if (answer.is_correct and not was_given) or (not answer.is_correct and was_given):
            correct = False
            break
    return correct


def clear_session(session):
    session.pop('question', None)
    session.pop('score', None)


decorators = [never_cache, login_required]


@method_decorator(decorators, name='dispatch')
class Quiz(generic.ListView):
    def get(self, request):
        clear_session(request.session)
        return redirect('/')

    def post(self, request):
        card_id = request.POST['card_id']
        question = int(request.session.get('question', 0))
        score = int(request.session.get('score', 0))
        cards = CardSet.objects.get(pk=card_id).card.all()
        total = len(cards)
        if question != 0 and is_correct_answer(cards[question - 1].answer_set.all(), request):
            score = score + 1
        if question == total:
            clear_session(request.session)
            return render(request, 'results.html', context={'score': int(100/total*score)})
        else:
            request.session['question'] = question + 1
            request.session['score'] = score
            return render(request, 'takequiz.html', context={'card': cards[question],
                                                                'card_id': card_id})
# Create your views here.

