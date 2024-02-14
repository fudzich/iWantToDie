from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=20, blank=False, null=False, verbose_name="First Name",
                                  help_text="Enter your first name")
    last_name = models.CharField(max_length=20, blank=False, null=False, verbose_name="Last Name",
                                 help_text="Enter your last name")
    position = models.CharField(max_length=20, blank=False, null=False, verbose_name="Position",
                                help_text="Enter your position")

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        db_table = 'employee'


class Genre(models.Model):
    title = models.CharField(max_length=20, blank=False, null=False, verbose_name="Title")
    short_desc = models.CharField(max_length=10, blank=False, null=False, verbose_name="Short Description")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "genre"


class Game(models.Model):
    title = models.CharField(max_length=20, blank=False, null=False, verbose_name="Title",
                             help_text="Enter game's title")

    #genre = models.CharField(max_length=20, blank=False, null=False, verbose_name="Genre", help_text="Enter game's genre")

    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, blank=False, null=False, verbose_name="Genre",
                              help_text="Enter genre of this game")

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'game'


class Article(models.Model):
    title = models.CharField(max_length=20, blank=False, null=False, verbose_name="Title",
                             help_text="Enter article's title")
    author = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=False, null=False,
                               verbose_name="Article's Author", help_text="Enter article's author")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, blank=False, null=False, verbose_name="Game",
                             help_text="Enter game this article covers")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "article"

# Create your models here.
