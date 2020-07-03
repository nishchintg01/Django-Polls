from django.db import models
from django.contrib.auth.models import User

Ratings =( 
    ("1", "One"), 
    ("2", "Two"), 
    ("3", "Three"), 
    ("4", "Four"), 
    ("5", "Five"), 
) 

# Surveys Class
class Poll(models.Model):
	user  = models.ForeignKey(User,related_name="polls",on_delete=models.CASCADE)
	Question = models.CharField(max_length = 2000)
	Option1 = models.CharField(max_length = 2000)
	Option2 = models.CharField(max_length = 2000)
	Option3 = models.CharField(max_length = 2000)
	Points3 = models.IntegerField(default=0,null=True)
	Points2 = models.IntegerField(default=0,null=True)
	Points1 = models.IntegerField(default=0,null=True)


	def __str__(self):
		return self.Question