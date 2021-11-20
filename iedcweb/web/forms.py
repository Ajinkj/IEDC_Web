from django import forms


class form_msg(forms.Form):
    name=forms.CharField(label='name', max_length=200, widget=forms.TextInput)
    email=forms.EmailField(label='email', required=True, widget=forms.EmailInput)
    message=forms.CharField(label='message', max_length=1000, required=True, widget=forms.Textarea)