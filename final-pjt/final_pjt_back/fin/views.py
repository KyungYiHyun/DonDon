import pandas as pd
from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
import requests
from .models import DepositProducts,SavingProducts
from rest_framework.response import Response
from .serializers import DepositProductsSerializer, SavingProductsSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.db.models import Case, When
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
from django.db import IntegrityError
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
# Create your views here.
disable_warnings(InsecureRequestWarning)

API_KEY = settings.BANK_API_KEY
EXCHANGE_API_KEY = settings.EXCHANGE_API_KEY

BASE_URL = 'http://finlife.fss.or.kr/finlifeapi/'

User = get_user_model()

topFinGrpNo = ['020000','030300']

@api_view(['GET'])
def exchange(request):
    URL = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={EXCHANGE_API_KEY}&searchdate=20241111&data=AP01'
    response = requests.get(URL, verify=False).json()
    return Response(response)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def deposit_likes(request, deposit_pk):
    deposit = get_object_or_404(DepositProducts, pk=deposit_pk)
    if request.user in deposit.like_users.all():
        deposit.like_users.remove(request.user)
        return Response({'message': '상품 담기 취소'}, status=status.HTTP_200_OK)
    else:
        deposit.like_users.add(request.user)
        return Response({'message': '상품 담기 성공'}, status=status.HTTP_200_OK)
    
@api_view(['POST']) 
@permission_classes([IsAuthenticated])
def saving_likes(request, saving_pk):
    saving = get_object_or_404(SavingProducts, pk=saving_pk)
    if request.user in saving.like_users.all():
        saving.like_users.remove(request.user)
        return Response({'message': '상품 담기 취소'}, status=status.HTTP_200_OK)
    else:
        saving.like_users.add(request.user)
        return Response({'message': '상품 담기 성공'}, status=status.HTTP_200_OK)    

@api_view(['GET'])
def send_deposit(request):
    deposits = DepositProducts.objects.all()
    serializer = DepositProductsSerializer(deposits, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def send_saving(request):
    savings = SavingProducts.objects.all()
    serializer = SavingProductsSerializer(savings, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def save_deposit_products(request):
    URL = BASE_URL + 'depositProductsSearch.json'
    for code in topFinGrpNo:
        page = 1
        total_pages = None
        while True:
            params = {
                'auth': API_KEY,
                'topFinGrpNo': code,
                'pageNo': page
            }

            response = requests.get(URL, params=params).json()
            if total_pages is None:
                total_pages = response["result"].get("max_page_no", 4)

            base_list = response["result"]["baseList"]
            option_list = response["result"]["optionList"]

            for result in base_list:
                product_options = [
                    option for option in option_list 
                    if option.get('fin_prdt_cd') == result.get('fin_prdt_cd')
                ]

                for option in product_options:
                    intr_rate = option.get('intr_rate')
                    save_trm = int(option.get('save_trm', 0))
                    if not intr_rate:
                        intr_rate = -1
                    if save_trm <6:
                        continue

                    combined_data = {
                        'fin_co_no': result.get('fin_co_no'),
                        'fin_prdt_cd': result.get('fin_prdt_cd'),
                        'kor_co_nm': result.get('kor_co_nm'),
                        'fin_prdt_nm': result.get('fin_prdt_nm'),
                        'mtrt_int': result.get('mtrt_int'),
                        'etc_note': result.get('etc_note'),
                        'join_deny': result.get('join_deny'),
                        'join_member': result.get('join_member'),
                        'join_way': result.get('join_way'),
                        'spcl_cnd': result.get('spcl_cnd'),
                        'max_limit': result.get('max_limit'),
                        'fin_grp_cd': code,
                        'intr_rate': intr_rate,
                        'intr_rate_type': option.get('intr_rate_type'),
                        'intr_rate_type_nm': option.get('intr_rate_type_nm'),
                        'intr_rate2': option.get('intr_rate2'),
                        'save_trm': option.get('save_trm'),
                    }

                    try:
                        serializer = DepositProductsSerializer(data=combined_data)
                        if serializer.is_valid(raise_exception=True):
                            serializer.save()
                    except (IntegrityError,ValidationError):
                        continue

            page += 1
            if page > total_pages:
                break
    return Response({"성공!"})



@api_view(['GET'])
def save_saving_products(request):
    URL = BASE_URL + 'savingProductsSearch.json'
    for code in topFinGrpNo:
        page = 1
        total_pages = None
        while True:
            params = {
                'auth': API_KEY,
                'topFinGrpNo': code,
                'pageNo': page
            }

            response = requests.get(URL, params=params).json()
            if total_pages is None:
                total_pages = response["result"].get("max_page_no", 4)

            base_list = response["result"]["baseList"]
            option_list = response["result"]["optionList"]

            for result in base_list:
                # 각 상품에 대한 옵션들을 찾습니다
                product_options = [
                    option for option in option_list 
                    if option.get('fin_prdt_cd') == result.get('fin_prdt_cd')
                ]

                for option in product_options:
                    intr_rate = option.get('intr_rate')
                    save_trm = int(option.get('save_trm', 0))
                    if not intr_rate:
                        intr_rate = -1
                    if save_trm <6:
                        continue

                    # 기본 정보와 옵션 정보를 합친 데이터 생성
                    combined_data = {
                        'fin_co_no': result.get('fin_co_no'),
                        'fin_prdt_cd': result.get('fin_prdt_cd'),
                        'kor_co_nm': result.get('kor_co_nm'),
                        'fin_prdt_nm': result.get('fin_prdt_nm'),
                        'mtrt_int': result.get('mtrt_int'),
                        'etc_note': result.get('etc_note'),
                        'join_deny': result.get('join_deny'),
                        'join_member': result.get('join_member'),
                        'join_way': result.get('join_way'),
                        'spcl_cnd': result.get('spcl_cnd'),
                        'max_limit': result.get('max_limit'),
                        'fin_grp_cd': code,
                        # 옵션 정보 추가
                        'intr_rate': intr_rate,
                        'intr_rate_type': option.get('intr_rate_type'),
                        'intr_rate_type_nm': option.get('intr_rate_type_nm'),
                        'rsrv_type' : option.get('rsrv_type'),
                        'rsrv_type_nm' : option.get('rsrv_type_nm'),
                        'intr_rate2': option.get('intr_rate2'),
                        'save_trm': option.get('save_trm'),
                    }

                    try:
                        serializer = SavingProductsSerializer(data=combined_data)
                        if serializer.is_valid(raise_exception=True):
                            serializer.save()
                    except (IntegrityError,ValidationError):
                        continue

            page += 1
            if page > total_pages:
                break
    return Response({"성공!"})

def get_current_user_info(request):
    current_user = request.user
    return {
        'id' :  current_user.id,
        'salary': current_user.salary,
        'assets': current_user.assets,
        'age': current_user.age,
        'gender': current_user.gender,
        'job': current_user.job
    }


def get_similar_users(current_user_info):
    # Django ORM을 사용하여 모든 유저 데이터를 가져옴
    users = User.objects.all().values('id', 'salary', 'assets', 'age', 'gender','job')

    # Pandas DataFrame으로 변환
    user_df = pd.DataFrame(list(users))
    # 현재 유저와 비슷한 유저 필터링 (연봉, 자산, 나이, 성별 기준)
    similar_users = user_df[
    (user_df['salary'] * 0.9 <= current_user_info['salary']) & (current_user_info['salary'] <= user_df['salary'] * 1.1) &
    (user_df['assets'] * 0.9 <= current_user_info['assets']) & (current_user_info['assets'] <= user_df['assets'] * 1.1) &
    (user_df['age'] - 3 <= current_user_info['age']) & (current_user_info['age'] <= user_df['age'] + 3) &
    (user_df['gender'] == current_user_info['gender']) &
    (user_df['job'] == current_user_info['job'])
]

    similar_users = similar_users[similar_users['id'] != current_user_info['id']]

    return similar_users['id'].tolist()  # 비슷한 유저들의 ID 리스트 반환


def get_deposit_products_by_users(user_ids):
    # 중간 테이블에서 해당 유저들이 가입한 금융상품 가져오기
    user_likes_deposits = DepositProducts.objects.filter(like_users__in=user_ids).values('id')
   
    # Pandas DataFrame으로 변환하여 빈도 계산
    deposit_df = pd.DataFrame(list(user_likes_deposits))
   
    # 각 금융상품의 빈도 계산 후 상위 10개 추출
    top_10_products = deposit_df['id'].value_counts().head(10).index.tolist()
    # 상위 10개 정렬 유지
    preserved_order = Case(*[When(id=pk, then=pos) for pos, pk in enumerate(top_10_products)])
  
    return DepositProducts.objects.filter(id__in=top_10_products).order_by(preserved_order)

@api_view(['GET'])
def recommend_deposit_products(request):
    # 현재 로그인된 사용자 정보 가져오기
    current_user_info = get_current_user_info(request)

    # 비슷한 사용자들 찾기
    similar_user_ids = get_similar_users(current_user_info)
    print(similar_user_ids)
    if not similar_user_ids:
        return Response()
  
    # 비슷한 사용자들이 가입한 상위 10개의 금융상품 추천
    recommended_products = get_deposit_products_by_users(similar_user_ids)
    # Serializer를 사용하여 데이터 반환 (필요 시)
    serializer = DepositProductsSerializer(recommended_products, many=True)

    if serializer.data:
        return Response(serializer.data)
    else:
        return Response({'데이터 없음'})


def get_saving_products_by_users(user_ids):
    # 중간 테이블에서 해당 유저들이 가입한 금융상품 가져오기
    user_likes_saving = SavingProducts.objects.filter(like_users__in=user_ids).values('id')
   
    # Pandas DataFrame으로 변환하여 빈도 계산
    saving_df = pd.DataFrame(list(user_likes_saving))
   
    # 각 금융상품의 빈도 계산 후 상위 10개 추출
    top_10_products = saving_df['id'].value_counts().head(10).index.tolist()
    preserved_order = Case(*[When(id=pk, then=pos) for pos, pk in enumerate(top_10_products)])
  
    return SavingProducts.objects.filter(id__in=top_10_products).order_by(preserved_order)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommend_saving_products(request):
    # 현재 로그인된 사용자 정보 가져오기
    current_user_info = get_current_user_info(request)

    # 비슷한 사용자들 찾기
    similar_user_ids = get_similar_users(current_user_info)

    if not similar_user_ids:
        return Response()

    # 비슷한 사용자들이 가입한 상위 10개의 금융상품 추천
    recommended_products = get_saving_products_by_users(similar_user_ids)
    # Serializer를 사용하여 데이터 반환 (필요 시)
    serializer = SavingProductsSerializer(recommended_products, many=True)
    if serializer.data:
        return Response(serializer.data)
    else:
        return Response({'데이터 없음'})
    
# 사용자의 관심 예금 상품 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_liked_deposit_products(request):
    user = request.user
    liked_products = user.like_depositproducts.all()
    serializer = DepositProductsSerializer(liked_products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# 사용자의 관심 적금 상품 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_liked_saving_products(request):
    user = request.user
    liked_products = user.like_savingproducts.all()
    serializer = DepositProductsSerializer(liked_products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)