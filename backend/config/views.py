from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
import  logging
from django.contrib.auth import get_user_model  # If used custom user model
from django.contrib.auth.models import User
from news.twitterAPI import read_neo_feed
from news.twitterAPI import read_python_user_stream


# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer




class FeedSerializer(serializers.Serializer):
    """expects JSON of the form {"feed": "twitterName"}
       example: {"feed": "NEOnewstoday"} """
    feed = serializers.CharField()



UserModel = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
          write_only=True,
    )

    class Meta:
       model = User
       fields = ('username','password')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        # if 'password' in validated_data:
        user.set_password(validated_data['password'])
        user.save()
        return user





class TwitterFeedView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = FeedSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # read_python_user_stream()
        return Response(read_neo_feed(serializer.data['feed']), status=status.HTTP_201_CREATED)


class CreateUserView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.create(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)