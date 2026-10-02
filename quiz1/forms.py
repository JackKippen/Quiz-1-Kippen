from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import Project, Inquiry, TechStack, Testimony


class ProjectForm(forms.ModelForm):
    project_name = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Project Name'}),
    )
    description = forms.CharField(
        required=True,
        strip=True,
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Write a short project description'}),
    )
    tech_stacks = forms.ModelChoiceField(
        queryset=TechStack.objects.none(),
        widget=forms.RadioSelect,
        required=True,
        label='Tech Stacks',
        empty_label=None,
    )
    link = forms.URLField(
        required=True,
        widget=forms.URLInput(attrs={'placeholder': 'https://example.com'}),
    )

    class Meta:
        model = Project
        fields = ['project_name', 'description', 'tech_stacks', 'link']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tech_stacks'].queryset = TechStack.objects.order_by('name')

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        if not description or not description.strip():
            raise forms.ValidationError('Description is required.')
        return description.strip()

    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get('description')
        if description is not None and not description.strip():
            self.add_error('description', 'Description is required.')
        return cleaned_data


class TechStackForm(forms.ModelForm):
    class Meta:
        model = TechStack
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'e.g. Python'}),
        }


class AdminOnlyAuthenticationForm(AuthenticationForm):
    error_messages = {
        **AuthenticationForm.error_messages,
        'invalid_login': 'Only superusers may sign in here.',
    }

    def confirm_login_allowed(self, user):
        super().confirm_login_allowed(user)
        if not user.is_superuser:
            raise forms.ValidationError('Only superusers may sign in here.', code='invalid_login')


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['first_name', 'last_name', 'contact_number', 'email', 'address', 'message']


class TestimonyForm(forms.ModelForm):
    class Meta:
        model = Testimony
        fields = ['full_name', 'content']
