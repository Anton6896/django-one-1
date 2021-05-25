import csv

from customers.models import Customer
from products.models import Products
from sales.models import Csv, Position, Sale
from django.utils.dateparse import parse_date

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

            try:
                product_obj = Products.objects.get(name__iexact=product)
                # anti sql injection (name must be less then 20 chars)
                if len(customer) > 20:
                    customer = customer[:20]
                customer_obj, _ = Customer.objects.get_or_create(name__iexact=customer)

            except Products.DoesNotExist or Customer.DoesNotExist:
                product_obj = customer_obj = None
                print("======= Cant get product or customer from csv file =======")

            # create position and Sale for this position
            if product_obj and customer_obj:
                """^^^ not good ^^^"""
                sale_obj = None
                position_obj, created = Position.objects.get_or_create(
                    product=product_obj,
                    quantity=quantity,
                    created=date
                )

                if created:
                    sale_obj, _ = Sale.objects.get_or_create(
                        transaction_id=transaction_id,
                        positions=position_obj,
                        customer=customer_obj,
                        sales_man=request.user,
                        created=date
                    )
