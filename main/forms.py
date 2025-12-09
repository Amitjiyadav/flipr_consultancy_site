from django import forms
from .models import Contact, Subscriber, Project, Client

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'mobile', 'city']


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']


# Optional: custom admin panel ke liye forms
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["image", "name", "description"]

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["image", "name", "designation", "description"]