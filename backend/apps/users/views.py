from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.recipes.pagination import CustomPagination
from .models import Follow
from .serializers import ListFollowSerializer

User = get_user_model()


class FollowApiView(APIView):
    def post(self, request, pk):
        user = request.user
        following = get_object_or_404(User, id=pk)
        if Follow.objects.filter(user=user, following=following).exists():
            return Response(
                {'error': 'Нельзя подписаться на автора дважды'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        create_follow = user.following.create()
        serializer = ListFollowSerializer(
            create_follow, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        user = request.user
        following = get_object_or_404(User, id=pk)
        delete_follow = user.following.all()
        if delete_follow.exists():
            delete_follow.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class FollowListViewSet(ListAPIView):
    queryset = Follow.objects.all()
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = ListFollowSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        user = self.request.user
        return Follow.objects.filter(user=user)
