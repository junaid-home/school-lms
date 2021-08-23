from lessons.models import Course, Grade
from django.db import models
from users.models import User
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

FEE_STATUS_CHOICES = (
    ('paid', "PAID"),
    ('pending', 'PENDING')
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


class School_timing(models.Model):
    start = models.TimeField()
    end = models.TimeField()

    def __str__(self):
        return f'{self.start} - {self.end}'


class Event(models.Model):
    date = models.DateField(null=True, blank=True, default=timezone.now)
    start = models.TimeField()
    end = models.TimeField()
    type = models.CharField(max_length=30, null=True, blank=True)
    note = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.type} {self.start.hour} - {self.end.hour}'


class Fee(models.Model):
    month = models.CharField(max_length=10, null=True, blank=True)
    year = models.CharField(max_length=5, null=True, blank=True)
    amount = models.IntegerField()
    status = models.CharField(
        max_length=30, default='pending', choices=FEE_STATUS_CHOICES)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'user({self.user.id} - {self.user.user_name}) {self.month} {self.year}'
