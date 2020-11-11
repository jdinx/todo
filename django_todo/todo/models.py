from django.db import models

# Create your models here.



class Task(models.Model):
	name = models.TextField()
	due_date = models.DateTimeField()
	reminder_date = models.DateTimeField()
	complete = models.BooleanField(default=False)


	def __str__(self):
		return self.name

	def get_date(self):
		return self.due_date.date()
