from django import forms


class DateFilterForm(forms.Form):
    year = forms.IntegerField(min_value=0, max_value=3000, required=True)
    month = forms.IntegerField(min_value=1, max_value=12, required=True)
