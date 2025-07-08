from django import forms
from .models import Capsule
from ckeditor.widgets import CKEditorWidget

class CapsuleForm(forms.ModelForm):
    unlock_datetime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    message = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Capsule
        fields = ['title', 'message', 'file', 'recipient_email', 'unlock_datetime'] 