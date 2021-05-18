import base64

from django.db.models import Q

from customers.models import Customer
from profiles.models import Profile
from sales.models import Sale
import pandas as pd
from django.contrib import messages
from io import BytesIO
import matplotlib.pyplot as plt

# global variables
merge_df = None


# work with database
def sales_and_positions(date_from, date_to, chart_type=None, request=None) -> dict or None:
    sales_df = None
    positions_df = None
    global merge_df
    positions_list = []

    # load data to Pandas DataFrame for calculations
    sales_qs = Sale.objects.filter(Q(created__date__gte=date_from), Q(created__date__lte=date_to))

    # if any sales founds
    if len(sales_qs) > 0:

        for sale in sales_qs:
            # get all positions for all sales
            for pos in sale.get_positions():
                positions_list.append(
                    {
                        "sale_id": pos.get_sale_id(),
                        "position_id": pos.pk,
                        "product": str(pos.product.name),
                        "quantity": pos.quantity,
                        "price": pos.price,
                    }
                )

        # create DataFrames
        sales_df = pd.DataFrame(sales_qs.values())
        positions_df = pd.DataFrame(positions_list)

        # change customer id to customer name and salesman id to salesman name
        # change column name
        # created updated datetime look
        sales_df["customer_id"] = sales_df["customer_id"].apply(_get_customer_name)
        sales_df["sales_man_id"] = sales_df["sales_man_id"].apply(_get_salesman_name)
        sales_df["created"] = sales_df["created"].apply(lambda x: x.strftime('%d/%m/%Y'))
        sales_df["updated"] = sales_df["updated"].apply(lambda x: x.strftime('%d/%m/%Y'))
        sales_df.rename({
            "customer_id": "customer",
            "sales_man_id": "sales man",
            "id": "sale_id"
        }, axis=1, inplace=True)

        # created one big data source with all variables
        merge_df = pd.merge(sales_df, positions_df, on="sale_id")

        # detailed view of big data
        by_id = merge_df.groupby('transaction_id', as_index=False)['price'].agg('sum')
        by_customer = merge_df.groupby('customer', as_index=False)['price'].agg('sum')
        by_sales_man = merge_df.groupby('sales man', as_index=False)['price'].agg('sum')

        # amazing bootstrap classes (its a free magic), convert data to html tables
        main_df_html = merge_df.to_html(classes=["table-bordered", "table-striped", "table-hover", "table"])
        by_id_html = by_id.to_html(classes=["table-bordered", "table-striped", "table-hover", "table"])
        by_customer_html = by_customer.to_html(classes=["table-bordered", "table-striped", "table-hover", "table"])
        by_sales_man_html = by_sales_man.to_html(classes=["table-bordered", "table-striped", "table-hover", "table"])

        # creating chart based on the user choose
        chart = get_chart(chart_type, by_id, labels=by_id['transaction_id'].values)

        # return as tuple all data
        return main_df_html, by_id_html, by_customer_html, by_sales_man_html, chart

    else:
        messages.warning(request, f'Sorry can not find data for this time period !')
        return None


# Inner utils functions  ====================
def _get_salesman_name(id: int) -> str:
    profile = Profile.objects.get(pk=id)
    return profile.user.username


def _get_customer_name(id: int) -> str:
    customer = Customer.objects.get(pk=id)
    return customer.name


def _get_graph():
    """
    # have an 2 ways for do that one is using buffer in rum_memory (nice and fast)
    # second for all query save chart and upload to the storage (not good decision)
    """

    # after getting data from user and figure type
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    img_png = buffer.getvalue()
    # encode picture
    graph = base64.b64encode(img_png)
    # decode to html utf-8
    graph = graph.decode('utf-8')
    # close and return html friendly obj
    buffer.close()
    return graph


def get_chart(chart_type, data, **kwargs):
    """
    by getting choose from user decide what kind of chart will return ,
    as data will use [sum(prise) grouped by transaction_id]
    """
    plt.switch_backend('AGG')
    plt.figure(figsize=(10, 4))
    plt.tight_layout()

    if chart_type == "1":
        print("1 : Bar Chart")
        plt.bar(data['transaction_id'], data['price'])

    elif chart_type == "2":
        print("2 : Pie Chart")
        plt.pie(data=data, x='price', labels=kwargs['labels'])

    elif chart_type == "3":
        print("3 : Line Chart")
        plt.plot(data['transaction_id'], data['price'])

    else:
        print(" -- some strange chart ! failed to identify it ...")

    chart = _get_graph()
    return chart
