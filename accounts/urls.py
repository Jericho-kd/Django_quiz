from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('', views.CardSetListView.as_view(), name='home'),
    path('cardset/<int:pk>', views.CardListView.as_view(), name='cardset'),
    #path('startQuiz/', views.takequiz, name='startQuiz'),
    path('stqrtQuiz/', views.Quiz.as_view(), name='startQuiz'),
]
