from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=60, blank=True, null=True)
    state_province = models.CharField(max_length=30, verbose_name='State/Province')
    country = models.CharField(max_length=50)
    website = models.URLField()
    
    def __str__(self):
        return self.name
        
    class Meta:
        ordering = ['name']
    
    
class Author(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='First Name')
    last_name = models.CharField(max_length=40, verbose_name='Last Name')
    email = models.EmailField(blank=True, null=True, verbose_name='e-mail')
    
    def __str__(self):
        return u'{} {}'.format(self.first_name, self.last_name)
        
    class Meta:
        ordering = ['last_name']
        
        
class Tag(models.Model):
    tag = models.CharField(max_length=30)
    
    def __str__(self):
        return self.tag
    
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(blank=True, null=True, verbose_name='Pub Date')
    
    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ['-publication_date']