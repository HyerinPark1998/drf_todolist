from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from todo.serializers import ToDoSerializer,ToDoCreateSerializer
from todo.models import ToDo


class ToDoListView(APIView):
    def get(self,request):
        to_do_list = ToDo.objects.all()
        serializer = ToDoSerializer(to_do_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self,request):
        serializer = ToDoCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({'message':'할일이 등록되었습니다'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ToDoDetailView(APIView):
    def get(self,request,todo_id):
        to_do = get_object_or_404(ToDo, id=todo_id)
        serializer = ToDoSerializer(to_do)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self,request,todo_id):
        to_do = get_object_or_404(ToDo,id=todo_id)
        if request.user == to_do.user:
            serializer = ToDoCreateSerializer(to_do,data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response({'message':'할일이 수정되었습니다'}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message':'권한이 없습니다'}, status=status.HTTP_403_FORBIDDEN)
    def delete(self,request,todo_id):
        to_do = get_object_or_404(ToDo,id=todo_id)
        if request.user == to_do.user:
            to_do.delete()
            return Response({'message':'삭제되었습니다'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message':'권한이 없습니다'}, status=status.HTTP_403_FORBIDDEN)