from rest_framework import generics, exceptions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PostagemSerializer, UserSerializer, LikePostagensSerializer, ReviewSerializer

from .models import Postagem, User, LikePostagens, Review

'''
List, Create
'''
@api_view(['GET'])
def apiOverview(request):

    api_urls = {
        'List Users':'/user-list/',
        'Detail User':'/user-detail/<str:pk>/',
        'Create User':'/user-create/',
        'Update User':'/user-update/<str:pk>/',
        'Delete User':'/user-delete/<str:pk>/'
    }

    return Response(api_urls)

@api_view(['GET'])
def userList(request):
    users = User.objects.all()
    serializer = UserSerializer(users)
    return Response(serializer.data)

@api_view(['GET'])
def userDetail(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def userCreate(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)


class PostagensAPIView(generics.ListCreateAPIView):
        queryset = Postagem.objects.all()
        serializer_class = PostagemSerializer

        def get_queryset(self):
            if self.kwargs.get('pk'):
                return self.queryset.filter(user_id=self.kwargs.get('pk'))
            return self.queryset.all()


class UsersAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UsersAPIViewCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LikePostagensAPIView(generics.ListCreateAPIView):
    queryset = LikePostagens.objects.all()
    serializer_class = LikePostagensSerializer


class ReviewAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

'''
Delete, Update

'''


class PostagemAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer


class UserAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LikePostagemAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LikePostagens.objects.all()
    serializer_class = LikePostagensSerializer


class ReviewAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
