from django import forms
from .models import Meeting


class MeetingForm(forms.ModelForm):

	date = forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))
	time = forms.TimeField()

	class Meta:
		model = Meeting
		fields = ['number', 'agenda', 'date', 'venue', 'time', 'minutes', 'resolutions']
