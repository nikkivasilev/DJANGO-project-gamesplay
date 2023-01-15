from random import choices

from django.core import validators
from django.db import models


# Create your models here.


class Profile(models.Model):
    MAX_30_LENGth = 30
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.IntegerField(
        validators=[validators.MinValueValidator(12)],
        null=False,
        blank=False,
    )
    password = models.CharField(
        max_length=MAX_30_LENGth,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_30_LENGth,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_30_LENGth,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Game(models.Model):
    ACTION = "Action"
    ADVENTURE = "Adventure"
    PUZZLE = "Puzzle"
    STRATEGY = "Strategy"
    SPORTS = "Sports"
    BOARD_AND_CARD = "Board/Card Game"
    OTHER = "Other"
    CATEGORY_CHOICES = (
        (ACTION, ACTION),
        (ADVENTURE, ADVENTURE),
        (PUZZLE, PUZZLE),
        (STRATEGY, STRATEGY),
        (SPORTS, SPORTS),
        (BOARD_AND_CARD, BOARD_AND_CARD),
        (OTHER, OTHER),
    )

    title = models.CharField(
        max_length=30,
        unique=True,
        default=None,
        null=False,
        blank=False,
    )
    category = models.CharField(
        max_length=15,
        null=False,
        blank=False,
        choices=CATEGORY_CHOICES,
    )

    rating = models.FloatField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(0.1),
            validators.MaxValueValidator(5.0),
        ),
    )
    max_level = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            validators.MinValueValidator(1),
        ),
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )
    summary = models.TextField(
        null=True,
        blank=True,
    )
