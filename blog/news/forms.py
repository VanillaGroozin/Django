from django.forms import ModelForm 
from news.models import News

class NewsForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['creator'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = 'form-control'

        self.fields['title'].widget.attrs['placeholder'] = 'News title ..'
        self.fields['description'].widget.attrs['placeholder'] = 'Descriptions ..'

    class Meta:
        model = News
        verbose_name="Новости"
        fields = "__all__"
