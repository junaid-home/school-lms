from lessons.models import Course
from django.db import models
from users.models import Grade, User
from django.utils import timezone

ATTENDENCE_STATUS = (
    ('absent', 'ABSENT'),
    ('present', 'PRESENT'),
)

DAY_CHOICES = (
    ('monday', 'MONDAY'),
    ('tuesday', 'TUESDAY'),
    ('wednesday', 'WEDNESDAY'),
    ('thursday', 'THURSDAY'),
    ('friday', 'FRIDAY'),
    ('saturday', 'SATURDAY'),
    ('sunday', 'SUNDAY'),
)


class Attendence(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(null=True, blank=True, default=timezone.now)
    status = models.CharField(
        default='present', max_length=10, choices=ATTENDENCE_STATUS)

    def __str__(self):
        return f'user({self.user.id} - {self.user.user_name}) {self.date} {self.status}'


class Timetable(models.Model):
    grade = models.ForeignKey(
        Grade, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.grade}'


class Period(models.Model):
    timetable = models.ForeignKey(
        Timetable, on_delete=models.CASCADE, null=True, blank=True)
    day = models.CharField(
        default='monday', max_length=10, choices=DAY_CHOICES)
    period_one = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='first+', null=True, blank=True)
    period_two = models.ForeignKey(
        Course, on_delete=models.CASCADE, null=True, related_name='second+', blank=True)
    period_three = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='third+', null=True, blank=True)
    period_four = models.ForeignKey(
        Course, on_delete=models.CASCADE, null=True, related_name='fourth+', blank=True)
    period_five = models.ForeignKey(
        Course, on_delete=models.CASCADE, null=True, related_name='fifth+', blank=True)
    period_six = models.ForeignKey(
        Course, on_delete=models.CASCADE, null=True, related_name='sixth+', blank=True)
    period_seven = models.ForeignKey(
        Course, on_delete=models.CASCADE, null=True, related_name='seventh+', blank=True)
    period_eight = models.ForeignKey(
        Course, on_delete=models.CASCADE, null=True, related_name='eigth+', blank=True)
