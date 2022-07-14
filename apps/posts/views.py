from django.http import JsonResponse, HttpResponse

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status, generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.posts.models import Post, PostCategories
from apps.posts.serializer import PostSerializer, PostCategorySerializer


class PostAPIView(generics.ListCreateAPIView):
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_active', 'tag']
    serializer_class = PostSerializer
    search_fields = ['title']
    ordering_fields = ['created_at']
    queryset = Post.objects.all()


class PostRetrieveAPIView(APIView):
    def get(self, request, pk):
        try:
            product = Post.objects.get(id=pk)
        except Post.DoesNotExist:
            return Response({'msg': 'product not found'}, status=status.HTTP_404_NOT_FOUND)
        srz = PostSerializer(product, many=False)
        return Response(srz.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            product = Post.objects.get(id=pk)
        except Post.DoesNotExist:
            return JsonResponse({'msg': 'product not found'}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class PostCategoriesAPIView(generics.ListAPIView):
    serializer_class = PostCategorySerializer
    queryset = PostCategories.objects.all()

    def post(self, request):
        request_body = request.data
        new_product = PostCategories.objects.create(title=request_body['title'],
                                                       )
        srz = PostCategorySerializer(new_product, many=False)
        return Response(srz.data, status=status.HTTP_201_CREATED)


class PostCategoryRetrieveAPIView(APIView):
    def get(self, request, pk):
        try:
            category = PostCategories.objects.get(id=pk)
        except PostCategories.DoesNotExist:
            return Response({'msg': 'category not found'}, status=status.HTTP_404_NOT_FOUND)
        srz = PostCategorySerializer(category, many=False)
        return Response(srz.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            category = Post.objects.get(id=pk)
        except PostCategories.DoesNotExist:
            return Response({'msg': 'category not found'}, status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
