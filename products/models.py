from django.db import models

# Create your models here.
class Product(models.Model):
	title=models.CharField(max_length=120)
	content=models.TextField(blank=True,null=True)
	price=models.DecimalField(max_digits=15,decimal_places=2,default=99.99)

	@property
	def sale_price(self): #add 80% discount
		return '%.2f' % (float(self.price)*0.8)

	@property 
	def getDiscount(self):
		return "80%"
		
	#using title as field to show on admin
	def __str__(self):
		return self.title