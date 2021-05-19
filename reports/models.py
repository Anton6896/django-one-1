from django.db import models
# from django.urls import reverse
from django.shortcuts import reverse

from profiles.models import Profile
from root.utils import customer_image_file_path


class Report(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=customer_image_file_path, blank=True)
    remarks = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{str(self.name)} by {str(self.author.user)} at {self.created.strftime('%d/%m/%Y')}"

    def get_absolute_url(self):
        return reverse('reports:detail', kwargs={"pk": self.pk})
