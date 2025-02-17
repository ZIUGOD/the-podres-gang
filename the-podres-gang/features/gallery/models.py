from datetime import date, timedelta
from django.db import models


class Image(models.Model):
    """
    Model representing an image in the gallery.

    Attributes:
        image (ImageField): The image file, stored in the "gallery/images/" directory.
        caption (CharField): A short caption for the image, with a maximum length of 128 characters.
        pub_date (DateField): The date the image was uploaded, automatically set to the current date.
        description (TextField): An optional description of the image, with a maximum length of 512 characters.

    Methods:
        __str__(): Returns the caption of the image.
        was_published_recently(): Returns True if the image was published within the last day, otherwise False.
    """

    image = models.ImageField(upload_to=f"gallery/images/")
    caption = models.CharField(max_length=128, blank=True, null=True)
    pub_date = models.DateField(verbose_name="Uploaded at", auto_now_add=True)
    description = models.TextField(blank=True, null=True, max_length=512)

    def __str__(self):
        """Returns the caption of the image."""
        return self.caption

    def was_published_recently(self):
        """Checks if the image was published within the last day."""
        return self.pub_date >= date.today() - timedelta(days=1)


class User(models.Model):
    """
    A Django model representing a user.

    Attributes:
        username (str): The username of the user. Maximum length is 24 characters.
        password (str): The password of the user. Maximum length is 64 characters.
        email (str): The email address of the user. Maximum length is 64 characters.
        first_name (str): The first name of the user. Maximum length is 64 characters.
        last_name (str): The last name of the user. Maximum length is 64 characters.
        date_joined (date): The date when the user joined. Automatically set to the current date.
        last_login (date): The date when the user last logged in. Automatically updated to the current date.
        is_staff (bool): A boolean indicating whether the user is a staff member. Default is False.
        images (Image): A foreign key to the Image model. Can be null or blank.

    Methods:
        __str__(): Returns the username of the user.
        get_full_name(): Returns the full name of the user.
        get_short_name(): Returns the first name of the user.
        was_logged_in_recently(): Returns True if the user has logged in within the last 7 days.
    """

    username = models.CharField(max_length=24)
    password = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    date_joined = models.DateField(auto_now_add=True)
    last_login = models.DateField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    images = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, blank=True)

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
