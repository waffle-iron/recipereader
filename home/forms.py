from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Recipe


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "first_name", "last_name", "email"]

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        for key in ["first_name", "last_name", "email"]:
            self.fields[key].required = False

        self.fields['username'].help_text = ''
        self.fields['password2'].help_text = ''
        self.fields['first_name'].widget = forms.TextInput(attrs={'placeholder': '(optional)'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'placeholder': '(optional)'})
        self.fields['email'].widget = forms.TextInput(attrs={'placeholder': '(optional)'})


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]

    def __init__(self, *args, **kwargs):
        # first call the 'real' __init__()
        super(LoginForm, self).__init__(*args, **kwargs)
        # then do extra stuff:
        self.fields['username'].help_text = ''


class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        exclude = ('user', 'pub_date',)

    def __init__(self, *args, **kwargs):
        super(AddRecipeForm, self).__init__(*args, **kwargs)

        for f in ['prep_time_hours', 'cook_time_hours', 'ready_in_hours']:
            self.fields[f].widget = forms.NumberInput(attrs={'placeholder': 'hours'})
        for f in ['prep_time_minutes', 'cook_time_minutes', 'ready_in_minutes']:
            self.fields[f].widget = forms.NumberInput(attrs={'placeholder': 'minutes'})

        self.fields['ingredients_text'].widget = forms.Textarea(attrs={
            'placeholder': 'put each ingredient on its own line'
        })
        self.fields['instructions_text'].widget = forms.Textarea(attrs={
            'placeholder': 'put each step on its own line'
        })

        # make recipe name big:
        self.fields['recipe_name'].widget = forms.TextInput(attrs={'style': 'font-size: 30px'})

