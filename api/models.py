from django.db import models

# Create your models here.
class Category(models.Model):
    categoryName = models.CharField(max_length=200)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.categoryName


class Image(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return str(self.image)

    
class RentList(models.Model):
    name = models.CharField(max_length=200,null=True, blank=True)
    price = models.DecimalField(max_digits=7,decimal_places=2,null=True, blank=True)
    images = models.ManyToManyField(Image)
    description= models.TextField(null=True,blank=True)
    rating= models.DecimalField(max_digits=7,decimal_places=2, null=True, blank=True)
    numReviews= models.IntegerField(null=True, blank=True, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')

    def __str__(self):
        return self.name

