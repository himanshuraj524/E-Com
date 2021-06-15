from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=30)
    category = models.CharField(max_length=50, blank=True)
    sub_category = models.CharField(max_length=50, blank=True)
    price = models.IntegerField(default=0)
    product_desc = models.CharField(max_length=300)
    product_publish_date = models.DateField()
    product_image = models.ImageField(upload_to = "shop/images", default=" ")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, blank=True)
    phone = models.IntegerField()
    desc = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    pin_code = models.CharField(max_length=15)
    phone = models.CharField(max_length=15, default="")

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length = 500)
    timestamp = models.DateField(auto_now_add=True)

    def update(self):
        # return self.update_desc[0:7] +"..."
        return self.order_id