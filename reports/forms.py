from django import forms
from .models import Report


class ReportForm(forms.ModelForm):
    remarks = forms.CharField(widget=forms.Textarea(attrs={
        "id": "report_text",
        "rows": "3",
        'placeholder': 'Please enter report here ... '
    }))

    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Report name',
            "id": "report_name",
        }),
        label="Report name",
        required=True)

    class Meta:
        model = Report
        fields = ('name', 'remarks',)
