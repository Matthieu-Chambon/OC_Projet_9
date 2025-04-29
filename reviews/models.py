from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Ticket(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=2048, blank=True)
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    time_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

class Review(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(max_length=1024, validators=[
        MinValueValidator(0),
        MaxValueValidator(5)
    ])
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.ticket.title} - {self.user.username}'