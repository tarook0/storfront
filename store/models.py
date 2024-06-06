from django.db import models
from django.core.validators import MinValueValidator

class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_products=models.ForeignKey('Product',on_delete=models.SET_NULL,null=True,related_name='+')
    def __str__(self) ->str:
        return self.title
    class Meta:
        ordering=['title']
    
class Promotion(models.Model):
    description=models.CharField(max_length=255)
    discount=models.FloatField()
    
class Product(models.Model):
    title = models.CharField(max_length=255)  # varchar
    description = models.TextField(null=True,blank=True)
    slug=models.SlugField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2,validators=[MinValueValidator(1)])
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions=models.ManyToManyField(Promotion,blank=True)
    def __str__(self)->str:
        return self.title
    class Meta:
        ordering=['title']
    

class Item(models.Model):
    name = models.CharField(max_length=255)
    count = models.IntegerField()


class Customer(models.Model):
    MEMBER_BORANZ = 'B'
    MEMBER_GOLD = 'G'
    MEMBER_SILVER = 'S'
    MEMBERSHIP_CHOICES = [
        (MEMBER_BORANZ, 'Bronz'),
        (MEMBER_BORANZ, 'Silver'),
        (MEMBER_BORANZ, 'Gold'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBER_BORANZ)
    def __str__(self):
        return f'{self.first_name}{self.last_name}'
    class Meta:
        ordering=['first_name','last_name']
    
    
    
    # class Meta:
    #     db_table='store_customers'
    #     indexes=[models.Index(fields=['last_name','first_name'])]

class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Faild'),
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    # def __str__(self)->str:
    #     return self.id
    # class Meta:
    #     Ordering=['id']
    


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    prdouct = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()


class Adress(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
