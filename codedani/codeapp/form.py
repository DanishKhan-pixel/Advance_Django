from django import forms


class userForm(forms.Form):
     num1 = forms.CharField(label="Value 1", required=False, widget=forms.TextInput)
     num2 = forms.CharField(label="Value 2", required=False, widget=forms.TextInput)
