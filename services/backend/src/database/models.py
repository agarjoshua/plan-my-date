from tortoise import fields, models

from database import Base

class Users(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    full_name = fields.CharField(max_length=50, null=True)
    password = fields.CharField(max_length=128, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)


class Notes(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=225)
    content = fields.TextField()
    author = fields.ForeignKeyField("models.Users", related_name="note")
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}, {self.author_id} on {self.created_at}"


class Restaurant(models.Model):

    status_choices = (
            ("default", "cheap"),
            ("500-1000", "affordable"),
            ("1000-5000", "Medium"),
            ("5000-*", "pricey"),
        )

    id = fields.IntField(pk=True)
    location = fields.CharField(max_length=225)
    name = fields.CharField(max_length=225)
    ratings = fields.IntField()
    review = fields.CharField(max_length=1000)
    prices = fields.CharField(Default="default", choices=status_choices, max_length=100)
    images = fields.ForeignKeyField("models.Images", related_name="Image")


class Image(models.Model):
    id = fields.IntField(pk=True)
    link = fields.CharField(max_length=225)


class Review(models.Model):
    id = fields.IntField(pk=True)
    restaurant = fields.ForeignKeyField("models.Restaurant", related_name="review")
    reviewer = fields.ForeignKeyField("models.Users", related_name="review")
    review = fields.CharField(max_length=225)
