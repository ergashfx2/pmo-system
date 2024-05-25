from django import forms
from .models import User

class CreateUserForm(forms.Form):
    username = forms.CharField(max_length=150)
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if self.password1 != self.password2 :
            self.add_error('password1',"Ikkala parol bir xil bo'lishi kerak")
            self.add_error('password2',"Ikkala parol bir xil bo'lishi kerak")

        if len(str(self.username)) > 150 :
            self.add_error('username',"Username 150 belgidan ko'p bo'lishi mumkin emas ")



class UserLoginForm(forms.Form):
    username = forms.CharField(label="Enter your username", max_length=150)
    password = forms.CharField(label="Enter your password", widget=forms.PasswordInput())

    def clean(self):
        data = super().clean()
        username = data.get('username')
        password = data.get('password')

        if not User.objects.filter(username=username) :
            self.add_error('username','Bunday username egasi topilmadi')

