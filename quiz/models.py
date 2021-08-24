from django.db import models
from lessons.models import Grade, Course
from users.models import User
from cloudinary.models import CloudinaryField


class Quizz(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    subtitle = models.CharField(max_length=250, blank=True, null=True)
    total_questions = models.IntegerField(default=10)
    passing_percentage = models.IntegerField(default=40)
    time_in_minutes = models.IntegerField(default=10)
    thumbnail = CloudinaryField('thumbnail', folder='avatars',
                                default='https://res.cloudinary.com/school-lms/image/upload/v1629519702/Hnet.com-image_1_sz2sf0.jpg')
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, null=True, blank=True)
    attempted_students = models.ManyToManyField(
        User,  blank=True)

    def __str__(self):
        return f'{self.id}({self.course.grade}) - {self.course.name}({self.course.teacher})'


class Question(models.Model):
    quiz = models.ForeignKey(
        Quizz, on_delete=models.CASCADE, null=True, blank=True)
    question = models.CharField(max_length=250, blank=True, null=True)
    option_1 = models.CharField(max_length=100, blank=True, null=True)
    option_2 = models.CharField(max_length=100, blank=True, null=True)
    option_3 = models.CharField(max_length=100, blank=True, null=True)
    option_4 = models.CharField(max_length=100, blank=True, null=True)
    answer = models.CharField(max_length=100, blank=True, null=True)
