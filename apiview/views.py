from rest_framework.views import APIView
from rest_framework.response import Response

from .models import UserModel
from .serializer import UserSerializer


class crud_apiview(APIView):

    def get(self, request, pk=None):
        if pk:
            queryset = UserModel.objects.get(pk=pk)
            return Response(UserSerializer(queryset).data)
        else:
            queryset = UserModel.objects.all()
            serialized_data = UserSerializer(queryset, many=True)
            return Response(serialized_data.data)

    def post(self, request, pk=None):
        serialized_data = UserSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        return Response({'error':'your data is not corrected format'})

    def put(self, request, pk=None):
        serialized_data = UserSerializer(instance=pk, data=request.data, partial=True)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        return Response({'error':'They have invalid url or id  '})

    def delete(self, request, pk=None):
        try:
            user = UserModel.objects.get(pk=pk)
        except:
            return {'user':'user already deleted'}
        user.delete()
        return Response({'user':'user sucessfully deleted'})
