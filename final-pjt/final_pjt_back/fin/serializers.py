from rest_framework import serializers
from .models import DepositProducts, SavingProducts

class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'
        read_only_fields = ('like_users',)
        # serializer에도 unique 필드 설정 추가
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=DepositProducts.objects.all(),
              fields=['fin_co_no','fin_prdt_cd','save_trm', 'intr_rate_type_nm','intr_rate','intr_rate2'], 
                message="이미 존재하는 상품입니다."
            )
        ]

class SavingProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProducts
        fields = '__all__'
        read_only_fields = ('like_users',)
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=SavingProducts.objects.all(),
                fields=['fin_co_no','fin_prdt_cd','save_trm', 'intr_rate_type_nm','intr_rate','intr_rate2'], 
                message="이미 존재하는 상품입니다."
            )
        ]