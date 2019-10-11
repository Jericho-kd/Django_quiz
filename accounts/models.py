from django.db import models
# Create your models here.


class Answer(models.Model):
    text = models.CharField(max_length=100)
    is_correct = models.BooleanField()
    card = models.ForeignKey('Card', on_delete=models.CASCADE)

    class Meta:
        ordering = ['?']  # random ordering of answers

    def __str__(self):
        return f'{self.text}'#[{self.is_correct}]'


class Card(models.Model):
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text


class CardSet(models.Model):
    name = models.CharField(max_length=100)
    card = models.ManyToManyField(Card)
    
    def __str__(self):
        return self.name
