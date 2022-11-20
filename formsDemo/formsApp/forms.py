from django import forms
from django.core import validators

class UserRegistrationForm(forms.Form):
    GENDER = [('male','MALE'),('female','FEMALE')]
    firstName = forms.CharField()
    lastName = forms.CharField(required=False,validators = 
    [validators.MinLengthValidator(5), validators.MaxLengthValidator(20)])
    email = forms.CharField(required=False)
    gender = forms.CharField(widget=forms.Select(choices=GENDER))
    password = forms.CharField(widget=forms.PasswordInput)

"""
    def clean(self):
        user_cleaned_data =  super().clean()
        inputFirstName = user_cleaned_data['firstName']
        if len(inputFirstName) > 20:
            raise forms.ValidationError('The maximum length of firstName is 20 characters')
        
        inputemail = self.cleaned_data['email']
        if inputemail.find('@')==-1:
            raise forms.ValidationError('The email should connect @')

    def clean_firstName(self):
        inputFirstName = self.cleaned_data['firstName']
        if len(inputFirstName) > 20:
            raise forms.ValidationError('The maximum length of firstName is 20 characters')
        return inputFirstName

    def clean_email(self):
        inputemail = self.cleaned_data['email']
        if inputemail.find('@')==-1:
            raise forms.ValidationError('The email should connect @')
        return inputemail

"""




