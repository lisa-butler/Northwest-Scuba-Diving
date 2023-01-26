from django import forms
from .models import Newsletter


class NewsletterSignupForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'email': 'Your Email',

        }

        self.fields['email'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black profile-form-input'  # noqa
            self.fields[field].label = False
