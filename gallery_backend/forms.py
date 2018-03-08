from django.forms import ModelForm
from product.models import Product
from django import forms


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ["modified", "created"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ignore_fields = ["image"]
        for field in self.fields:
            if field in ignore_fields:
                continue
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class ImportForm(forms.Form):
    excel_field = forms.FileField(label="Excel-Datei")
