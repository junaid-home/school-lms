from django.db import models
from cloudinary.models import CloudinaryField
from embed_video.fields import EmbedVideoField
from users.models import Grade
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField

VIDEO_PROVIDERS = (
    ("Youtube", 'YOUTUBE'),
    ('Vimeo', 'VIMEO'),
    ('SoundCloud', 'SOUND_CLOUD'),
)


class Course(models.Model):
    name = models.CharField(max_length=20)
    teacher = models.CharField(max_length=20)
    grade = models.ForeignKey(
        Grade, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name} ({self.grade})'


class Video(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=250, null=True, blank=True)
    link = EmbedVideoField()
    thumbnail = CloudinaryField('thumbnail', folder='avatars',
                                default='https://res.cloudinary.com/school-lms/image/upload/v1629519702/Hnet.com-image_1_sz2sf0.jpg')
    type = models.CharField(
        default='Youtube', choices=VIDEO_PROVIDERS, max_length=20)
    grade = models.ForeignKey(
        Grade, on_delete=models.CASCADE, null=True, blank=True)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.id}: {self.title}'


class Note(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=250, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    attachment = CloudinaryField(
        'attachment', folder='attachments', null=True, blank=True)
    grade = models.ForeignKey(
        Grade, on_delete=models.CASCADE, null=True, blank=True)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.id}: {self.title}'
