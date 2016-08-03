from django import forms

from cars.models import Car


class CarCreateForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = (
            'mark',
            'series',
            'body',
            'engine',
            'color',
            'manufacturer_country',
            'wheels',
            'cost',
            'year',
            'options',
            'image',
        )
