from django.contrib import admin
from events.models import Candidate
from events.models import Question
# Register your models here.
admin.site.register(Candidate)
admin.site.register(Question)