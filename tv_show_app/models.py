from django.db import models


class ShowManager(models.Manager):
    def basic_validator(self, data):
        errors = {}
        if len(data["title"]) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if len(data["network"]) < 3:
            errors["network"] = "Network should at least 3 characters"
        if len(data["desc"]) < 10:
            errors["description"] = "Description should be at least 10 characters"
        print(errors)
        return errors


class Show(models.Model):
    title = models.CharField(max_length=100)
    network = models.CharField(max_length=100)
    release_date = models.DateTimeField(null=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
