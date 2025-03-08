


from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Contacts  # Changed from Contact to Contacts

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'address', 'password1', 'password2']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts  # Changed from Contact to Contacts
        fields = ['name', 'email', 'subject', 'message']  # Make sure these field names match exactly
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }