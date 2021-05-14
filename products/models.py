from django.db import models

from root.utils import customer_image_file_path


class Products(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(default='no_image.jpg', upload_to=customer_image_file_path)
    price = models.FloatField(help_text="in US dollars $")
    created = models.DateTimeField(auto_now_add=True)
    updates = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{str(self.name)} -- {self.created.strftime('%d/%m/%Y')}"

    class Meta:
        db_table = 'products'
