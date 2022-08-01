from django.db import models
# from django.contrib.auth import models as author_models


class Profile(models.Model):
    fio = models.TextField()
    age = models.IntegerField()
    kind_of_sport = models.CharField(max_length=30)

    title = models.CharField(max_length=200)
#    authors = models.ForeignKey(author_models.User, on_delete=models.CASCADE)

    opened_at = models.DateTimeField(auto_created=True)
    closed_at = models.DateTimeField(null=True, blank=True)
