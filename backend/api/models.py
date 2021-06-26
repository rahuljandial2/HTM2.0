from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail as _send_mail

from datetime import datetime

class Profile(models.Model):
    user    = models.OneToOneField(User, on_delete=models.CASCADE)
    

    def send_mail(self, subject, message, from_email=None, html_message=None, **kwargs):
        _send_mail(subject, message, from_email, [self.user.email], html_message, **kwargs)

class Task(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)     #
    name            = models.CharField(max_length=64)
    is_completed    = models.BooleanField(default=False)
    parent_task     = models.ForeignKey('self', on_delete=models.CASCADE, default=None, blank=True, null=True)
    
    duration        = models.DurationField(blank=True, null=True)
    starts_at       = models.DateTimeField(blank=True, null=True)
    ends_at         = models.DateTimeField(blank=True, null=True)
    completed_at    = models.DateTimeField(blank=True, null=True)           #

    remarks         = models.CharField(max_length=200, null=True, blank=True)
    # alert           = True

    @property
    def child_tasks(self):
        return self.task_set.all()

    def save(self, *args, **kwargs):
        if self.is_completed and self.completed_at==None:
            self.completed_at = datetime.now()
        
        children = self.child_tasks
        for child in children:
            if not child.is_completed:
                child.is_completed = True
                child.save()

        return super().save(*args, **kwargs)
        

