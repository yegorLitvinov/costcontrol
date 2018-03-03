from django import forms


class YearFilterForm(forms.Form):
    year = forms.IntegerField(min_value=1990, max_value=2200, required=True)


class DateFilterForm(YearFilterForm):
    month = forms.IntegerField(min_value=1, max_value=12, required=True)
