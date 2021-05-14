from .models import Sale
from django.db.models.signals import m2m_changed
from django.dispatch import receiver


@receiver(m2m_changed, sender=Sale.positions.through)
def calculate_tot_price(sender, instance: Sale, action, **kwargs):
    # override ready() in apps.py , __init__.py config path
    # all this for trigger in db
    tot_price = 0
    if action in ('post_add', 'post_remove',):
        for item in instance.get_positions():
            tot_price += item.price

    instance.total_price = tot_price
    instance.save()
