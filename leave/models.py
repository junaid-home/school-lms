from django.db import models
from users.models import User
from ckeditor.fields import RichTextField

LEAVE_TYPES = (
    ("sick_leave", "SICK_LEAVE"),
    ("urgent_work", "URGENT_WORK"),
    ("family_function", "FAMILY_FUNCTION"),
    ("relative_marriage", "RELATIVE_MARRIAGE"),
    ("relative_death", "RELATIVE_DEATH"),
)

APPLICATION_STATUS = (
    ('pending', 'PENDING'),
    ('approved', 'APPROVED'),
    ('rejected', 'REJECTED'),
)


class LeaveApplication(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(
        max_length=20, choices=LEAVE_TYPES, default='sick_leave')
    date_from = models.DateField()
    date_to = models.DateField()
    description = RichTextField()
    status = models.CharField(
        max_length=20, choices=APPLICATION_STATUS, default='pending')

    def __str__(self):
        return f'user({self.user.id}: {self.user.user_name}) {self.status} {self.type} ({self.date_from} - {self.date_to})'
