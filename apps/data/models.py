from django.db import models
from django.db.models.signals import post_save

from apps.data.managers import EntryManager
from apps.data import handlers

# Create your models here.
class Entry(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    title = models.CharField(max_length = 64)
    text = models.TextField()
    published = models.BooleanField(db_index = True, default = True)

    objects = EntryManager()
    def __unicode__(self):
        return u'%s - %s' % (self.title, self.created)

post_save.connect(handlers.model_saved, sender=Entry)