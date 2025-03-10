from datetime import date, datetime, timedelta
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Image(models.Model):
    """
    Model representing an image in the gallery.
    """

    image = models.ImageField()
    caption = models.CharField(
        max_length=128,
        blank=True,
        null=True,
        unique=False,
        validators=[
            MaxLengthValidator(128, "Your caption must be at most 128 characters long."),
        ]
    )
    pub_date = models.DateTimeField(verbose_name="Uploaded at", auto_now_add=True)
    description = models.TextField(blank=True, null=True, validators=[MaxLengthValidator(512)])

    def __str__(self):
        """Returns a string representation of the object."""
        return self.caption or "Image with no caption."

    def was_published_recently(self):
        """Checks if the image was published within the last day."""
        return self.pub_date >= (datetime.now().date() - timedelta(days=1))

    class Meta:
        ordering = ["-pub_date"]
        verbose_name = "Image"
        verbose_name_plural = "Images"


class User(models.Model):
    """
    A Django model representing a user.
    """

    username = models.CharField(
        max_length=16,
        unique=True,
        validators=[
            MinLengthValidator(6, "Your username must be at least 6 characters long."),
            MaxLengthValidator(16, "Your username must be at most 16 characters long."),
        ],
        error_messages={"unique": "This username is already taken."},
        verbose_name="Username",
    )
    password = models.CharField(
        max_length=64,
        validators=[
            MinLengthValidator(12, "Your password must be at least 12 characters long."),
            MaxLengthValidator(64, "Your password must be at most 64 characters long."),
        ],
        verbose_name="Password",
    )
    email = models.EmailField(unique=True, verbose_name="Email")
    first_name = models.CharField(max_length=16, verbose_name="First Name")
    last_name = models.CharField(max_length=24, verbose_name="Last Name")
    date_joined = models.DateField(auto_now_add=True, verbose_name="Date Joined")
    last_login = models.DateField(auto_now=True, verbose_name="Last Login")
    is_staff = models.BooleanField(default=False, verbose_name="Staff Member")
    images = models.ManyToManyField(Image, blank=True, related_name="users")

    def __str__(self):
        """Returns the username of the user."""
        return self.username

    def get_full_name(self):
        """Returns the full name of the user."""
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        """Returns the first name of the user."""
        return self.first_name

    def was_logged_in_recently(self):
        """Checks if the user has logged in within the last 7 days."""
        return self.last_login >= date.today() - timedelta(days=7)
