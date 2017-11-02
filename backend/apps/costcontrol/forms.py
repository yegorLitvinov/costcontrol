from django import forms


class DateFilterForm(forms.Form):
    year = forms.IntegerField(min_value=1990, max_value=2200, required=True)
    month = forms.IntegerField(min_value=1, max_value=12, required=True)
