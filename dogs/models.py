from django.db import models


class Breed(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Breed name", help_text="Input breed name"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Breed description",
        help_text="Input dog breed",
    )

    class Meta:
        verbose_name = "Breed"
        verbose_name_plural = "Breeds"

    def __str__(self):
        return self.name


class Dog(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Dog name", help_text="Input dog name"
    )
    breed = models.ForeignKey(
        Breed,
        on_delete=models.SET_NULL,
        verbose_name="Poroda",
        help_text="Input dog poroda",
        null=True,
        blank=True,
        related_name='dogs',
    )
    photo = models.ImageField(
        upload_to="dogs/photo",
        blank=True,
        null=True,
        verbose_name="Photo",
        help_text="Input dog photo",
    )
    date_born = models.DateField(
        blank=True, null=True, verbose_name="born fate", help_text="Input dog date born"
    )

    class Meta:
        verbose_name = "Dog"
        verbose_name_plural = "Dogs"
        ordering = ["breed", "name"]

    def __str__(self):
        return self.name
