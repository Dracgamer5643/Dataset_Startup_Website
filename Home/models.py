from django.db import models

# Create your models here.

class pop_datasets(models.Model):
    db_name = models.CharField(max_length=25)
    db_disc = models.CharField(max_length=200)
    db_time = models.DateTimeField(auto_now_add=True, editable=False)
    db_logo = models.ImageField(upload_to="images/logos")
    db_rating = models.FloatField(null=True, blank=True)
    db_price = models.IntegerField(null=True, blank=True)

def __str__(self):
    return self.db.name


class pop_models(models.Model):
    md_name = models.CharField(max_length=25)
    md_disc = models.CharField(max_length=200)
    md_time = models.DateTimeField(auto_now_add=True, editable=False)
    md_type = models.CharField(max_length=30)
    md_rating = models.FloatField(null=True, blank=True)

def __str__(self):
    return self.md_name

class feedbacks(models.Model):
    feed_name = models.CharField(max_length=20)
    feed_message = models.CharField(max_length=100)
    feed_rating = models.FloatField(null=True, blank=True)
    feed_logo = models.ImageField(upload_to="images/logos")

def __str__(self):
    return self.feed_name