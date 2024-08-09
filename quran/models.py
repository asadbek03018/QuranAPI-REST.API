from django.db import models

# Create your models here.


class Author(models.Model):
    full_name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='quran/author/images/')
    age = models.CharField(max_length=100)
    about = models.TextField()

    def __str__(self):
        return self.full_name


    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authorlar"

class Sura(models.Model):
    LANGUAGES = (
        ('english', 'English'),
        ('uzbek', 'Uzbek'),
        ('russian', 'Russian'),
        ('arabic', 'Arabic')
    )
    name = models.CharField(max_length=200)
    total_oyat = models.IntegerField(default=0)
    lang = models.CharField(max_length=45, choices=LANGUAGES)
    written_place = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sura"
        verbose_name_plural = "Suralar"


class Oyat(models.Model):
    LANGUAGES = (
        ('english', 'English'),
        ('uzbek', 'Uzbek'),
        ('russian', 'Russian'),
        ('arabic', 'Arabic')
    )
    sura = models.ForeignKey(Sura, related_name='oyatlar', on_delete=models.CASCADE)  # Ensure this is correct
    lang = models.CharField(max_length=45, choices=LANGUAGES)
    oyat_number = models.BigIntegerField(default=0)
    translate = models.TextField(default="Tarjimasi")
    audio = models.FileField(upload_to='quran/audios/')
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.sura.name} - {self.oyat_number}"

    class Meta:
        verbose_name = "Oyat"
        verbose_name_plural = "Oyatlar"
