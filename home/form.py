from django import forms


from django import forms

class thanksform(forms.Form):
    name = forms.CharField(max_length=10)
    school  = forms.IntegerField(max_value=14)
    email = forms.EmailField()