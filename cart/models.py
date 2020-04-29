from django.db import models
from product.models import Variation
from user.models import CustomerUser

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    #Bảng ghi này được tạo ra khi nào
    created_at = models.DateTimeField(auto_now_add=True)
    #Lần update cuối cùng nó sẽ lấy thời gian hiện tại của hệ thống
    updated_at = models.DateTimeField(auto_now=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Variation, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)