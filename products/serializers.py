from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
	#for changing getDiscount property name
	discount=serializers.SerializerMethodField(read_only=True)
	class Meta:
		model=Product
		fields=[
			'title',
			'content',
			'price',
			'sale_price',
			'discount'
		]
	
	#telling serializer what discount property means
	#obj contains instance of data
	def get_discount(self,obj):
		return obj.getDiscount