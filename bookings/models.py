from django.db import models
from django.contrib.auth.models import User
from tutors.models import Tutor

class Booking(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    date = models.DateField()
    message = models.TextField()

    def __str__(self):
        return f"{self.student.username} booked {self.tutor.user.username}"
    
class Review(models.Model):

    tutor = models.ForeignKey('tutors.Tutor', on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)

    rating = models.IntegerField()
    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} review for {self.tutor.user.username}"