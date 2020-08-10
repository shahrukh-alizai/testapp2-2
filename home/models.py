from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)
    fkUser = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="customtext_fkUser",
    )

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class AnotherModel(models.Model):
    "Generated Model"
    test = models.BigIntegerField()
    newField = models.ForeignKey(
        "home.CustomText",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="anothermodel_newField",
    )


class DemoModel(models.Model):
    "Generated Model"
    demoField = models.BigIntegerField()
    fkKey = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="demomodel_fkKey",
    )


class DemoModel101(models.Model):
    "Generated Model"
    demoField = models.BigIntegerField()
    demoFieldModel101 = models.ForeignKey(
        "home.DemoModel10123",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="demomodel101_demoFieldModel101",
    )


class DemoModel10123(models.Model):
    "Generated Model"
    demoField = models.BigIntegerField()
