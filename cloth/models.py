from django.db import models



class CustomerCL(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username
class OrderCL(models.Model):
    customer = models.ForeignKey(CustomerCL, on_delete=models.CASCADE)
    products = models.ManyToManyField('ProductCL')
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order for {self.customer} on {self.order_date}'
class ProductCL(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='', null=True)
    description = models.TextField(blank=True)
    cost = models.PositiveIntegerField()
    tags = models.ManyToManyField('TagCL', related_name='content_name')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}-{self.created_at}'
class TagCL(models.Model):
    name = models.CharField(max_length=100, verbose_name='Add a hashtag')

    def __str__(self):
        return f'#{self.name}'
