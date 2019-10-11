from django.contrib import admin
from django.forms.models import BaseInlineFormSet
from django.core.exceptions import ValidationError
from .models import Answer, Card, CardSet
# Register your models here.


class AnswerFormSet(BaseInlineFormSet):
    def clean(self):
        super(AnswerFormSet, self).clean()
        total_correct= 0
        for form in self.forms:
            data = form.cleaned_data
            is_correct = data.get('is_correct', False)
            if is_correct:
                total_correct += 1
        if total_correct == 0:
            raise ValidationError("Выберите хотя бы один верный ответ!")


class MembershipInline(admin.TabularInline):
    model = CardSet.card.through


class AnswerInline(admin.TabularInline):
    model = Answer
    formset = AnswerFormSet


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

    def get_model_perms(self, request):
        return {} 


@admin.register(CardSet)
class CardSetAdmin(admin.ModelAdmin):
    inlines = [MembershipInline]
    exclude = ('card', )