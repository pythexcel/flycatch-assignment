from django import forms

from .models import CustomUser


class RegistrationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    password = forms.CharField(widget=forms.PasswordInput(
        attrs= {
            "placeholder": "Enter Password"
        }
    ))
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs= {
            "placeholder": "Confirm Password"
        }
    ))

    class Meta:
        model = CustomUser
        fields = ['email', 'password']

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']

        if password != confirm_password:
            raise forms.ValidationError(
                message="Password does not match!"
            )
