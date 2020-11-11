from django import forms
from .models import Task

class AddTask(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['name','due_date','reminder_date','complete']

	name = forms.CharField(widget=forms.TextInput(
		attrs={"type":"text", "name":"name", "class":"form-control", "id":"taskInput1", "aria-describedby":"textHelp", "placeholder":"Super important thing to do.", "autocomplete":"off"}))
	due_date = forms.DateTimeField(widget=forms.DateTimeInput(
		attrs={"autocomplete":"off", "type":"text", "name":"due_date", "class":"form-control"}
		))
	reminder_date = forms.DateTimeField(widget=forms.DateTimeInput(
		attrs={"autocomplete":"off", "type":"text", "name":"reminder_date", "class":"form-control"}
		))
	complete = forms.BooleanField(required=False)