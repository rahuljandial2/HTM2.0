from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail as _send_mail
from django.db import models
from django.utils.timezone import utc
from django.urls import reverse
from datetime import datetime
from string import ascii_letters, digits
import random

class VerifyKey(models.Model):
    key     = models.CharField(max_length=40, default='')
    user    = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def create_key(self):
        charset = ascii_letters + digits
        rnd_str = ''.join((random.choice(charset) for _ in range(40)))
        self.key = rnd_str

    def is_key_valid(self):
        now = datetime.utcnow().replace(tzinfo=utc)
        time_flag = (now-self.created_at).total_seconds()<12*3600
        if time_flag:
            return True 

        return False

    def save(self, *args, **kwargs):
        self.create_key()
        return super().save(*args, **kwargs)

class Profile(models.Model):
    user    = models.OneToOneField(User, on_delete=models.CASCADE)

    def send_mail(self, subject=None, message=None, from_email=None, html_message=None, **kwargs):
        _send_mail(subject, message, from_email, [self.user.email], html_message=html_message, **kwargs)
        a = 123
        
    def make_body(self, link):
        body = f'''<h2>
                Here's your activation link...
                <a href="{link}">{link}</a>
                Click it to get verified
                </h2>
        '''
        return body

    def send_activation_mail(self):
        key = self.user.verifykey.key
        link = settings.SITE_LINK+reverse('verify', kwargs={'_key': key})[1:]
        html_body = self.make_body(link)
        self.send_mail('Varification Key FOR ACTIVATION', message=link)

    def activate(self):
        self.user.is_active = True
        self.user.verifykey.delete()

        self.user.save()

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
        
    def __str__(self) -> str:
        return f'{self.id} - {self.name}'
