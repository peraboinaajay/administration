from django import forms
from admissions.models import School

class studentmodelform(forms.ModelForm):
    class Meta:
        model=School
        fields='__all__'

class vendorform(forms.Form):
    name=forms.CharField()
    address=forms.CharField()
    contact=forms.CharField()
    items=forms.CharField()        