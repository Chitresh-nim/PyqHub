from django.db import models
from django.contrib.auth.models import User
from PyqProject.storage import SupabaseStorage, ProfileStorage

# Create your models here.
class Subject(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    branch = models.CharField(max_length=50)
    semester = models.IntegerField()

    def __str__(self):
        return self.title

class PYQ(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    year = models.CharField(max_length=10)
    drive_link = models.URLField(blank=True)
    pdf = models.FileField(upload_to="papers/",
                           storage=SupabaseStorage(),
                            blank=True, null=True)
    
    def __str__(self):
        return f"{self.subject.title} - {self.year}"
    
class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paper = models.ForeignKey(PYQ,on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ("user", "paper")
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="profile_pictures/",
                                        storage=ProfileStorage(),
                                        default="profile_pictures/default.png",
                                        blank=True)
    
    def __str__(self):
        return self.user.username