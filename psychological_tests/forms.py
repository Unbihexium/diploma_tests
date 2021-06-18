from django import forms

from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    """
    Форма авторизации
    """

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if user is None:
            raise forms.ValidationError('Введён некорректный username или пароль, попробуйте ввести их ещё раз!',
                                        code='invalid_login_password')
        if not user.is_active:
            raise forms.ValidationError('Вам закрыт доступ к сайту!', code='access_denied')

    class Meta:
        model = User
        fields = ['username', 'password']

