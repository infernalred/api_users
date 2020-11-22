from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from .models import User
from .permissions import IsAdminOrReadOnly
from .serializer import (
    ReadOnlyUserSerializerSerializer as ReadUser,
    WriteOnlyUserSerializerSerializer as WriteUser
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminOrReadOnly)

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return ReadUser
        return WriteUser

    @swagger_auto_schema(
        request_body=WriteUser,
        responses={200: ReadUser}
    )
    def update(self, request, *args, **kwargs):
        wr_serializer = WriteUser(
            data=request.data
        )
        wr_serializer.is_valid(raise_exception=True)
        instance = wr_serializer.save()
        read_serializer = ReadUser(instance)
        return Response(read_serializer.data)

    @swagger_auto_schema(
        request_body=WriteUser,
        responses={201: ReadUser}
    )
    def create(self, request, *args, **kwargs):
        wr_serializer = WriteUser(
            data=request.data
        )
        wr_serializer.is_valid(raise_exception=True)
        instance = wr_serializer.save()
        read_serializer = ReadUser(instance)
        return Response(
            read_serializer.data,
            status=HTTP_201_CREATED
        )

    @swagger_auto_schema(
        request_body=WriteUser,
        responses={200: ReadUser}
    )
    def partial_update(self, request, *args, **kwargs):
        wr_serializer = WriteUser(
            data=request.data
        )
        wr_serializer.is_valid(raise_exception=True)
        instance = wr_serializer.save()
        read_serializer = ReadUser(instance)
        return Response(read_serializer.data)
