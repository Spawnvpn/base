import datetime
from django import forms
from django.contrib.auth import authenticate, models
from django.forms.widgets import TextInput, MultiWidget, Select


class PhoneWidget(MultiWidget):
    def __init__(self, attrs=None, **kwargs):
        widgets = [Select(choices=(('+38', '+38'), ('+7', '+7'))),
                   Select(choices=(('050', '050'), ('095', '095'),)),
                   TextInput(attrs={'size': 7, 'max_length': 7})]
        super(PhoneWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.code, value.operator, value.number]
        return ["", "", ""]

    def format_output(self, rendered_widgets):
        return rendered_widgets[0] + "(" + rendered_widgets[1] + ")" + rendered_widgets[2]


class PhoneField(forms.MultiValueField):
    def __init__(self, *args, **kwargs):
        list_fields = [forms.CharField(),
                       forms.CharField(),
                       forms.CharField()]
        super(PhoneField, self).__init__(
            list_fields, widget=PhoneWidget(), *args, **kwargs)

    def compress(self, values):
        return values[0] + values[1] + values[2]


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'fill-container'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'fill-container'}))

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError(message='Invalid username or password',
                                        code='invalid_login')


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(max_length=30)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    birth_date = forms.DateField()
    phone_number = PhoneField()

    def clean_birth_date(self):
        date = self.cleaned_data.get("birth_date")
        today = datetime.date.today()
        if date.year >= today.year - 12:
            raise forms.ValidationError("You must grow up!")
        return date

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    class Meta:
        model = models.User
        fields = (
            "username",
            "password1",
            "password2",
            "email",
            "first_name",
            "last_name",
            "phone_number",
        )

