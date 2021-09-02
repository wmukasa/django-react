from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,RetrieveAPIView
from wed.models import BlogPost
from wed.serializers import BlogPostSerializer

class BlogPostListView(ListAPIView):
    queryset =  BlogPost.objects.order_by('-date_created')
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny,)

class BlogPostDetailView(RetrieveAPIView):
    queryset =  BlogPost.objects.order_by('-date_created')
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny,)

class BlogPostFeacturedView(ListAPIView):
    queryset =  BlogPost.objects.all().filter(featured=True)
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny,)

class BlogPostcategoryView(APIView):
    serializer_class = BlogPostSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self,request,formant=None):
        data = self.request.data
        category = data['category']
        queryset = BlogPost.objects.order_by('-date_created').filter(category__iexact=category)
        serializer = BlogPostSerializer(queryset, many=True)
        return Response(serializer.data)

