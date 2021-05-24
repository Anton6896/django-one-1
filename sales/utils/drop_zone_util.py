import csv

from customers.models import Customer
from products.models import Products
from sales.models import Csv
from django.utils.dateparse import parse_date


def csv_handler(file):
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

            if product_obj and customer_obj:
                pass
