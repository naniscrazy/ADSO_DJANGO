from django.db import models

# Create your models here.

class AuthorModel(models.Model):
    name = models.CharField(max_length=75, null=False, blank=False, verbose_name='Name')
    last_name = models.CharField(max_length=80, verbose_name='Last name')
    birthday = models.DateField(verbose_name='Birthday', null=False, blank=False)
    country = models.CharField(max_length=100, null=True, blank=True, verbose_name='Country')
    profession = models.CharField(max_length=200, null=True, blank=True, verbose_name='Profession')
    
    class Meta:
        db_table = 'Authors'
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
    
    # Define cómo se representará el objeto como una cadena. 
    # En este caso, muestra el nombre del autor.
    def __str__(self) -> str:
        return self.name
    
    
    
class VideoGameModel(models.Model):
    name = models.CharField(max_length=80, null=False, blank=False,  verbose_name='Name')
    Release_Date = models.DateField(null=False, blank=False, verbose_name='Release date')
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE, verbose_name='Author')
    
    class Meta:
        db_table = 'Video Games'
        verbose_name = 'Video Game'
        verbose_name_plural = 'Video Games' 
    
    # Define cómo se representará el objeto como una cadena. 
    # En este caso, muestra el nombre del autor.
    def __str__(self) -> str:
        return self.name
    
    