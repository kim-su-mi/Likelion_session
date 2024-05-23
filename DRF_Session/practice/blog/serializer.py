#serializer

from .models import Blog
from rest_framework import serializers

##모델을 json형태로 보여주게 하기 위한 것
class BlogSerializer(serializers.ModelSerializer):
    
    class Meta:
        ##Bolg모델에 있는 모든 필드를 직렬화 하겠다 
        model = Blog
        fields = '__all__'

