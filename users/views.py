from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from users.serializers import UserSerializers,UserUpdateSerializers,RefreshTokenSerializer
from users.models import User


class UserView(APIView):
    def post(self, request):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': f'가입완료! \n${serializer.data}'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': f'${serializer.errors}'}, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User,id = user_id)
        serializer = UserSerializers(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        # request.data["email"] = request.user.email
        print(request.user.email)
        if request.user == user:
            serializer = UserUpdateSerializers(user,data = request.data)
            if serializer.is_valid(): 
                serializer.save()
                return Response({'message': f'수정완료! ${serializer.data}'}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': '인증된 사용자가 아닙니다.'}, status=status.HTTP_403_FORBIDDEN)
    def delete(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        if request.user == user:
            user.delete()
            return Response({'message':'삭제되었습니다'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': '인증된 사용자가 아닙니다.'}, status=status.HTTP_403_FORBIDDEN)


class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated, )
    def post(self,request):
        sz = RefreshTokenSerializer(data=request.data)
        sz.is_valid(raise_exception=True)
        sz.save()
        return Response({'message':'로그아웃되었습니다.'},status=status.HTTP_204_NO_CONTENT)