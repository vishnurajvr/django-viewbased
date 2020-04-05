from rest_framework.decorators import api_view
from rest_framework.response import Response

from apiview.models import UserModel
from apiview.serializer import UserSerializer

@api_view(['GET', 'POST'])
def crud_api_view(request):

    if request.method == 'GET':
        queryset = UserModel.objects.all()
        serialized_data = UserSerializer(queryset, many=True)
        return Response(serialized_data.data)

    if request.method == 'POST':
        serialized_data = UserSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        return Response({'error' : 'your data is not corrected format'})


@api_view(['GET', 'PUT', 'DELETE'])
def crud_api_view_udpate(request, pk):

    if request.method == 'GET':
        try:
            return Response(UserSerializer(UserModel.objects.get(pk=pk)).data)
        except:
            return Response({'user' : 'User not found'})

    if request.method == 'PUT':
        serialized_data = UserSerializer(instance=pk, data=request.data, partial=True)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        return Response({'error':'They have invalid url or id '})

    if request.method == 'DELETE':
        try:
            user = UserModel.objects.get(pk=pk)
        except:
            return {'user':'user already deleted'}
        user.delete()
        return Response({'user':'user sucessfully deleted'})