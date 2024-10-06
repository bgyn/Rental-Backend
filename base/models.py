from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


#model for category
class Categories(models.Model):
    category_name = models.CharField(max_length=100, null=True, blank=True)
    category_image = models.ImageField(upload_to='categoryIcons',null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

# model for rules 
class Rules(models.Model):
    rule_text = models.CharField(max_length=255)
    
    def __str__(self):
        return self.rule_text


# model for rentitem
class RentItem(models.Model):
    title = models.CharField(max_length=100,null=True, blank=True)
    price = models.DecimalField(max_digits=4,decimal_places=2, null=True, blank=True)
    thumbnailImage = models.ImageField(upload_to='thumbnails',null=True, blank=True)
    description = models.TextField()
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(default=0, max_digits=2, decimal_places=1, validators=[MinValueValidator(0),MaxValueValidator(5)])
    numOfReviews = models.IntegerField(null=True, blank=True)
    address= models.CharField(max_length=255,null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6,null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6,null=True, blank=True)
    rules = models.ManyToManyField(Rules, blank=True)

    def __str__(self):
        return self.title
    
    