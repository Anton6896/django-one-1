from django.db import models

from profiles.models import Profile
from root.utils import customer_image_file_path


class Report(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to=customer_image_file_path)
    remarks = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{str(self.name)} by {str(self.author.user)} at {self.created.strftime('%d/%m/%Y')}"
