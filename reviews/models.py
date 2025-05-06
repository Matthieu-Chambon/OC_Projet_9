from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import os


class Ticket(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=2048, blank=True)
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    answered = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        if self.image:
            try:
                os.remove(self.image.path)
            except FileNotFoundError:
                pass
        super().delete(*args, **kwargs)


class Review(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(5)
    ])
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.ticket.title} - {self.user.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.ticket.answered = True
        self.ticket.save()

    def delete(self, *args, **kwargs):
        self.ticket.answered = False
        self.ticket.save()
        super().delete(*args, **kwargs)
