# goods/serializers.py

from rest_framework import serializers
from .models import Goods, GoodsCategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


# ModelSerializer实现商品列表页
class GoodsSerializer(serializers.ModelSerializer):
    # 覆盖外键字段
    category = CategorySerializer()

    class Meta:
        model = Goods
        fields = '__all__'
