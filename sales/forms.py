from django import forms

CHART_CHOICES = (
    ('1', 'Bar chart'),
    ('2', 'Pie chart'),
    ('3', 'Line chart'),
)

RESULT_CHOICES = (
    ('1', 'Transaction'),
    ('2', 'Sales date'),
)


class SaleSearchForm(forms.Form):
    date_from = forms.DateField(widget=forms.DateInput(attrs={'type': "date", "id": "date_from"}))
    date_to = forms.DateField(widget=forms.DateInput(attrs={'type': "date", "id": "date_to"}))
    chart_type = forms.ChoiceField(choices=CHART_CHOICES)
    result_by = forms.ChoiceField(choices=RESULT_CHOICES)
