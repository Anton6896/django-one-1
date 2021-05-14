from django.db import models

from root.utils import customer_image_file_path


class Customer(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(default='default.jpg', upload_to=customer_image_file_path)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = 'customers'
