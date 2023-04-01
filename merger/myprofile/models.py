from django.db import models

# Create your models here.


class Profile(models.Model):
    """
    Model that contain profiles
    """

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    birthplace = models.CharField(max_length=255)
    birthday = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Profile ({self.pk})"

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'


class Document(models.Model):
    """
    Model that contain documents
    """

    name = models.CharField(max_length=255)
    number = models.CharField(max_length=50)
    date_issued = models.DateField()
    expiration_date = models.DateField()
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='documents')

    def __str__(self):
        return f"{self.name} ({self.number})"

    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"
