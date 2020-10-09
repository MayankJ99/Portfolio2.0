from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
# from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from hitcount.models import HitCount
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from tinymce import models as tinymce_models

# Create your models here.
CurrentUser = get_user_model()


class User(auth_models.User, auth_models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)


class UserProfile(models.Model):
    profile_pic = models.ImageField(upload_to="images/", blank=True, null=True, default="images/BlueHead.jpg")
    user = models.OneToOneField(CurrentUser, unique=True, on_delete=models.CASCADE, null=True)
    bio = models.TextField(default="", blank=True)
    bio_html = models.TextField(editable=False)

    location = models.CharField(default="", blank=True, max_length=255)
    occupation = models.CharField(default="", blank=True, max_length=255)
    github = models.CharField(default="", blank=True, max_length=255)
    instagram = models.CharField(default="", blank=True, max_length=255)
    linkedin = models.CharField(default="", blank=True, max_length=255)

    quote = models.CharField(default="", blank=True, max_length=255)

    id = models.AutoField(primary_key=True)

    def __str__(self):
        # return self.bio
        return self.user.username


class Project(models.Model):
    user = models.ForeignKey(CurrentUser, related_name='project', on_delete=models.CASCADE, null=True)
    date = models.DateField()
    name = models.CharField(default="", blank=True, max_length=255)
    short_description = models.CharField(default="", max_length=255)
    full_description = models.TextField(default="", blank=True)
    demo = models.CharField(default="", blank=True, null=True, max_length=255)
    link = models.CharField(default="", blank=True, max_length=255)
    # cover = models.ImageField(upload_to='images/', null=True)
    cover = ProcessedImageField(upload_to='images/',
                                           processors=[ResizeToFill(1280, 720)],
                                           format='JPEG',
                                           options={'quality': 70}, null=True, blank=True)

    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('personal-index')

    class Meta:
        ordering = ['-date']


class Work(models.Model):
    user = models.ForeignKey(CurrentUser, related_name='work', on_delete=models.CASCADE, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    location = models.CharField(default="", max_length=255)
    position = models.CharField(default="", max_length=255)
    company = models.CharField(default="", max_length=255)

    full_description = models.TextField(default="", )
    # cover = models.ImageField(upload_to='images/', blank=True, null=True)
    cover = ProcessedImageField(upload_to='images/',
                                           processors=[ResizeToFill(1280, 720)],
                                           format='JPEG',
                                           options={'quality': 70}, null=True, blank=True)
    def __str__(self):
        return self.position

    def get_absolute_url(self):
        return reverse('personal-index')

    class Meta:
        ordering = ['-start_date']


class Intro(models.Model):
    user = models.ForeignKey(CurrentUser, related_name='quote', on_delete=models.CASCADE, null=True)
    quote = models.CharField(default="", max_length=255)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.quote

    def get_absolute_url(self):
        return reverse('personal-index')

    class Meta:
        ordering = ['-created_at']


class Blog(models.Model):
    user = models.ForeignKey(CurrentUser, related_name='blogger', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True)
    content = tinymce_models.HTMLField(blank=True, null=True)
    cover = ProcessedImageField(upload_to='images/',
                                           processors=[ResizeToFill(1280, 720)],
                                           format='JPEG',
                                           options={'quality': 70}, null=True, blank=True)  
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
     related_query_name='hit_count_generic_relation')
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('bloglist')

    class Meta:
        ordering = ['-created_at']

class Comment(models.Model):
    post = models.ForeignKey('Blog', related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    comment = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()


    class Meta:
        ordering = ['-created_date']
