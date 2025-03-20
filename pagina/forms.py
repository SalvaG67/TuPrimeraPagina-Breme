from django.contrib.auth.forms import AuthenticationForm

class loginForm(AuthenticationForm):
    class meta:
        model = AuthenticationForm
        fields = ['username', 'password']
