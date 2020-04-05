from rest_framework.response import Response
from rest_framework import viewsets

from apiview.serializer import UserSerializer
from apiview.models import UserModel


class UserViewSet(viewsets.ViewSet):

    def list(self, request, pk=None):
        queryset = UserModel.objects.all()
        return Response(UserSerializer(queryset, many=True).data)

    def retrieve(self, request, pk=None):
        try:
            user = UserModel.objects.get(pk=pk)
        except:
            return Response({'error' : 'User not found'})
        return Response(UserSerializer(user).data)


    def create(self,request): 
        serialized_data = UserSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        return Response({'user' : 'use correct format'})

    def update(self, request, pk=None):
        serialized_data = UserSerializer(data=request.data, instance=pk, partial=True)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        return Response({'error' : 'Send correct format json'})

    def destroy(self, request, pk=None):
        try:
            user = UserModel.objects.get(pk=pk)
        except:
            return Response({'error' : 'User not found'})
        user.delete()
        return Response({'user' : 'User sucessfully deleted'})

class UserModelViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer