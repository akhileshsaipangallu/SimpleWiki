# Django
from django import forms

# local Django
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', 'viewPermissionLevel', 'editPermissionLevel']

    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if Post.objects.filter(title__iexact=title):
    #         raise forms.ValidationError("'%s' has already been taken" % title)
    #     return title

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].widget.attrs['class'] = 'form-control'
            self.fields[key].widget.attrs['placeholder'] = \
                self.fields[key].label
            self.fields[key].widget.attrs['id'] = self.fields[key].label
