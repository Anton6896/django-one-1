from django.db import models
from django.db.models.signals import post_save

from customers.models import Customer
from products.models import Products
from profiles.models import Profile
from django.utils import timezone

from root.utils import generate_id
from django.shortcuts import reverse

"""
for ech sale have couple positions ! m2m field 
ech sale have sales_man (Profile) and user (Customer) and can have couple Positions on it .
(one sales_name on sale can sale 1-shirt(pos1) , 3-pents(pos2) etc. )
ech Position have amount and price for some product that was sailed 
"""


class Position(models.Model):
    """
    position is Product with certain quantity for specific price
    """
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField(blank=True)
    created = models.DateTimeField(blank=True)

    class Meta:
        db_table = 'position'

    def __str__(self):
        return f"pk: {self.pk}, product: {str(self.product)}, quantity: {self.quantity}"

    def save(self, *args, **kwargs):
        self.price = self.product.price * self.quantity
        return super().save(*args, **kwargs)

    def get_sale_id(self):
        # revers relation in orm db
        sale_obj = self.sale_set.first()
        return sale_obj.id


class Sale(models.Model):
    """
    who sale to who with what quantity and for what price
    """
    transaction_id = models.CharField(max_length=20, blank=True)
    positions = models.ManyToManyField(Position)
    # for total price m2m will create special receiver
    total_price = models.FloatField(blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sales_man = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(blank=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'sale'

    def get_absolute_url(self):
        return reverse('sales:detail', kwargs={"pk": self.pk})

    def __str__(self):
        return f"id: {str(self.transaction_id)} - at: {self.created.strftime('%d/%m/%Y')}," \
               f" total price: {self.total_price}"

    def save(self, *args, **kwargs):
        # auto create tine zone (Singleton)
        if self.created is None:
            self.created = timezone.now()

        # generate transaction id
        if not self.transaction_id:
            self.transaction_id = generate_id(17)

        return super().save(*args, **kwargs)

    def get_positions(self):
        return self.positions.all()


class Csv(models.Model):
    file_name = models.FileField(upload_to='csv_files', null=True)
    activated = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'csv'

    def __str__(self):
        return f"filename: {str(self.file_name)}"
