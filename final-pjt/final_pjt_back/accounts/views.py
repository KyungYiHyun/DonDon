from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import UserUpdateSerializer
from rest_framework.decorators import api_view, permission_classes

class UserUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        user = request.user  # 현재 인증된 사용자
        serializer = UserUpdateSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_current_user(request):
    if request.user.is_authenticated:
        return Response({
            'user_id': request.user.id,
            'username': request.user.username,
            'userEmail' : request.user.email,
            'nickname' : request.user.nickname,
            'userAge' : request.user.age,
            'userGender' : request.user.gender,
            'userAssets' : request.user.assets,
            'userSalary' : request.user.salary,
            'userJob' : request.user.job,
        })
    return Response({'user_id': None})


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request):
    user = request.user
    user.delete()
    return Response({"msg": "회원 탈퇴 완료"}, status=status.HTTP_204_NO_CONTENT)