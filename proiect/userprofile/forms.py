from django.contrib.auth.models import User
from django import forms


class NewAccountForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

    def clean(self):
        field_data = self.cleaned_data
        email_value = field_data.get('email')
        username_value = field_data.get('username')
        if User.objects.filter(email=email_value).exists():
            self._errors['email'] = self.error_class(["Emailul deja exista, te rugam sa adaugi un email unic"])
        if User.objects.filter(username=username_value).exists():
            self._errors['username'] = self.error_class(['Username-ul deja exista!'])
        return field_data
