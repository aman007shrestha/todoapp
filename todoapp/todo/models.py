from django.db import models

# Create your models here.

class TodoItem(models.Model):
	content = models.TextField()

	def __str__(self):
		if len(self.content) < 20:
			return self.content
		else:
			return self.content[:20]