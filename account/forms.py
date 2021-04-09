from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    
    password2 = forms.CharField(label='Repeat password',widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
   # def clean_password(self):

   #     password = self.cleaned_data.get('password')
   #     try:                                                     analizar mas a fondo este codigo
    #        validate_password(password, self.instance)
    #    except forms.ValidationError as error:
#
 #           # Method inherited from BaseForm
  #          self.add_error('password', error)
   #     return password
        
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']