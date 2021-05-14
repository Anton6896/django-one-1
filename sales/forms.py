from django import forms

CHART_CHOICES = (
    ('#1', 'Bar chart'),
    ('#1', 'Pie chart'),
    ('#1', 'Line chart'),
)


class SaleSearchForm(forms.Form):
    date_from = forms.DateField(widget=forms.DateInput(attrs={'type': "date", "id": "date_from"}))
    date_to = forms.DateField(widget=forms.DateInput(attrs={'type': "date", "id": "date_to"}))
    chart_type = forms.ChoiceField(choices=CHART_CHOICES)
