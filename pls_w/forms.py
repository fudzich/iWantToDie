from django import forms

from pls_w.models import Article


class articleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'author', 'game', 'content')


class loginForm(forms.Form):
    login = forms.CharField(required=False)
    password = forms.CharField(required=False)

class registerForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField()

