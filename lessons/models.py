import environ
from django.db import models
from cloudinary.models import CloudinaryField
from embed_video.fields import EmbedVideoField
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField

env = environ.Env()

VIDEO_PROVIDERS = (
    ("Youtube", 'YOUTUBE'),
    ('Vimeo', 'VIMEO'),
    ('SoundCloud', 'SOUND_CLOUD'),
)

SECTION_CHOICES = (
    ("A", "A"),
    ("B", "B"),
    ("C", "C"),
)


class Grade(models.Model):
    name = models.CharField(max_length=10, unique=True)
    section = models.CharField(
        default='A', choices=SECTION_CHOICES, max_length=2)

    def __str__(self):
        return f'{self.name} - {self.section}'


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
    thumbnail = CloudinaryField('thumbnail', folder='thumbnails',
                                default=env('DEFAULT_THUMBNAIL'))
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
    attachment_download_link = models.CharField(
        max_length=2000, null=True, blank=True)
    grade = models.ForeignKey(
        Grade, on_delete=models.CASCADE, null=True, blank=True)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.id}: {self.title}'
