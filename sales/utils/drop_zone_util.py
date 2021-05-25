import csv

from customers.models import Customer
from products.models import Products
from profiles.models import Profile
from sales.models import Csv, Position, Sale
from django.utils.dateparse import parse_date
from django.db.models import Q

"""
this is bad logic for creating sale and positions for it 
actually must create poo that groped by date (or other flag) and then push from pool and create Sale 
by date, then pop flag from pool and move to next one for grouping Sales 

but for simplicity and only functionality will live this one (save time and move to other project)   
"""


def csv_handler(file, request):
    # create save csv file
    csv_obj = Csv.objects.create(file_name=file)

    # get data from csv file and crete new DB entry from it
    with open(csv_obj.file_name.path, 'r') as f:
        data = csv.reader(f)
        data.__next__()  # skip header
        for row in data:
            line = ' '.join(row).split(' ')

            transaction_id = str(line[1][:6])
            product = str(line[2])
            quantity = int(line[3])
            customer = str(line[4])
            date = parse_date(line[5])

            if Sale.objects.filter(
                    Q(transaction_id=transaction_id) &
                    Q(created=date)
            ).exists():
                continue

            try:
                customer_obj, _ = Customer.objects.get_or_create(name__iexact=customer)
                profile_obj = Profile.objects.get(user=request.user)
                product_obj = Products.objects.get(name__iexact=product)

            except Products.DoesNotExist or Customer.DoesNotExist:
                product_obj = customer_obj = None
                print("======= Cant get product or customer from csv file =======")

            # create position and Sale for this position
            if product_obj and customer_obj:
                """^^^ not good ^^^"""
                position_obj, _ = Position.objects.get_or_create(
                    product=product_obj,
                    quantity=quantity,
                    created=date
                )

                # prevent for creation same object

                sale_obj, _ = Sale.objects.get_or_create(
                    transaction_id=transaction_id,
                    customer=customer_obj,
                    sales_man=profile_obj,
                    created=date
                )
                sale_obj.positions.add(position_obj)
                sale_obj.save()

                if sale_obj:
                    print(f" -- Sale obj created ")
