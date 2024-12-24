from django.db import models
from django.contrib.auth.models import User


#model for category
class Categories(models.Model):
    category_name = models.CharField(max_length=100, null=True, blank=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category_name}"

# model for rules 
class Rules(models.Model):
    rule_text = models.CharField(max_length=255)
    
    def __str__(self):
        return self.rule_text


class VerifiedManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return (
            super().get_queryset().filter(status = RentItem.Status.VERIFIED)
        )


# model for rentitem
class RentItem(models.Model):
    class Status(models.TextChoices):
        VERIFIED = 'VF','Verified'
        NOTVERIFIED = 'NVF','Not Verified'
    owner = models.ForeignKey(to=User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,null=True, blank=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='rent_category')
    price = models.CharField(max_length=30, null=True, blank=True)
    thumbnailImage = models.ImageField(upload_to='thumbnails',null=True, blank=True)
    description = models.TextField()
    inStock = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    address= models.CharField(max_length=255,null=True, blank=True)
    latitude = models.CharField(max_length=20,null=True, blank=True)
    longitude = models.CharField(max_length=20,null=True, blank=True)
    rules = models.ManyToManyField(Rules, blank=True)
    status = models.CharField(
        max_length=4,
        choices = Status,
        default= Status.NOTVERIFIED
    )

    objects = models.Manager()
    verified = VerifiedManager()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.title}"
    

class Booking(models.Model):
    """
    Define the booking models of the rentItems
    """
    class Status(models.TextChoices):
        PENDING = 'pending','pending'
        ACCEPTED = 'accepted','accepted'
        NOTACCEPTED = 'notAccepted','notAccepted'
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    rent_item = models.ForeignKey(to=RentItem,on_delete=models.CASCADE,related_name='bookings')
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(
        max_length=200,
        choices=Status.choices,
        default=Status.PENDING
    )
    total_price = models.CharField(max_length=30, null=True, blank=True)


    def save(self,*args,**kwargs):
        # calculate days
        days = (self.end_date - self.start_date).days+1
        totalPrice= days * float(self.rent_item.price)
        self.total_price = str(totalPrice)
        super().save(*args,**kwargs)

    def __str__(self):
        return f"{self.user.username} => {self.rent_item.title}"