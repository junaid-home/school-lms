from django.db import models
from lessons.models import Course
from users.models import User

STATUS_CHOICES = (
    ('passed', 'PASSED'),
    ('failed', 'FAILED')
)

COLOR_CHOICES = (
    ('red', 'RED'),
    ('blue', 'BLUE'),
    ('green', 'GREEN'),
    ('yellow', 'YELLOW'),
)

RESULT_TYPE_CHOICES = (
    ('sessional', 'SESSIONAL'),
    ('quizz', 'QUIZZ')
)


class Result(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(
        default='sessional', choices=RESULT_TYPE_CHOICES, max_length=20)
    total_marks = models.IntegerField(default=100)
    obtained_marks = models.IntegerField(default=0)
    status = models.CharField(
        default='passed', choices=STATUS_CHOICES, max_length=20)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    color = models.CharField(
        default='red', choices=COLOR_CHOICES, max_length=20)

    def __str__(self):
        return f'user({self.user.id} - {self.user.user_name}) {self.name}({self.type})'


class SubjectResult(models.Model):
    result = models.ForeignKey(
        Result, on_delete=models.CASCADE, blank=True, null=True)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, null=True, blank=True)
    total_marks = models.IntegerField(null=True, blank=True)
    obtained_marks = models.IntegerField(null=True, blank=True)
    status = models.CharField(
        default='passed', choices=STATUS_CHOICES, max_length=20)

    def __str__(self):
        return f'user({self.result.user.id}) {self.course.grade} ({self.result.name} {self.course.name})'
