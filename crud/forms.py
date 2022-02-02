from django import forms
from .models import *


class AddTracks(forms.ModelForm):
    class Meta:
        fields = '__all__'
        labels = {
            'name': 'Track Name'
        }
        model = Tracks


class InsertStudent(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['trackid'].widget.choices= [(track.tr_id, track.name) for track in Tracks.objects.all()]

    class Meta:
        model = Students
        fields = '__all__'
        labels = {
            'id': 'ID',
            'fname': 'First Name',
            'lname': 'Last Name',
            'trackid':'Track'
        }
