from django.conf import settings
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Candidate(models.Model):
	firstname = models.CharField(default='',max_length=25)
	lastname = models.CharField(default='',max_length=25)
	email = models.URLField(default='')
	bitsid = models.CharField(default='',max_length=20)
	contact = models.IntegerField()

	def update_user_profile(sender, instance, created, **kwargs):
		if created:
			Candidate.objects.create(user=instance)
			instance.candidate.save()

class Question(models.Model):
	ques = models.TextField()
	opt1 = models.CharField(max_length=25)
	opt2 = models.CharField(max_length=25)
	opt3 = models.CharField(max_length=25)
	opt4 = models.CharField(max_length=25)

	def publish(self):
		self.save()

	def __str__(self):
		return self.ques