from django import forms
from django.contrib.auth.models import User

from core.models import Profile



from django.utils.safestring import mark_safe
from django import forms

class ImagePreviewWidget(forms.widgets.FileInput):
    def render(self, name, value, attrs=None, **kwargs):
        input_html = super().render(name, value, attrs=None, **kwargs)
        img_html = mark_safe(f'<br><br><img src="{value.url}"/>')
        return f'{input_html}{img_html}'


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email',]


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ['created', 'modified', 'user']
        picture = forms.ImageField(widget=ImagePreviewWidget,)

