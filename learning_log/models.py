from django.db import models

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=120)
    credatim = models.DateTimeField(auto_now_add=True)
    upddatim = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name if len(self.name) < 50 else self.name[:50] + "..."

    def __unicode__(self):
        return self.name if len(self.name) < 50 else self.name[:50] + "..."


class Entry(models.Model):
    name = models.CharField(max_length=120)
    credatim = models.DateTimeField(auto_now_add=True)
    upddatim = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.name if len(self.name) < 50 else self.name[:50] + "..."

    def __unicode__(self):
        return self.name if len(self.name) < 50 else self.name[:50] + "..."

class Promise(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=1024)
    credatim = models.DateTimeField(auto_now_add=True)
    upddatim = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "promises"


    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title