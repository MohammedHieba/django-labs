from rest_framework.response import Response
from rest_framework import status
from books.models import Book
from .serializers import BookSerializer,UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes



@api_view(["POST"])
def api_signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,
            "message": "User has been registered successfully"
        }, status=status.HTTP_201_CREATED)

    return Response(data={
        "success": False,
        "message": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def index(request):
    books = Book.objects.all()
    serializer = BookSerializer(instance = books, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,
            "message": "Book has been created successfully"
        }, status = status.HTTP_201_CREATED)

    return Response(data={
        "success": False,
        "message": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET"])
def show(request, id):
    book = Book.objects.filter(pk=id)
    serializer = BookSerializer(instance=book, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def edit(request, id):
    book = Book.objects.get(pk=id)

    serializer = BookSerializer(instance=book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,
            "message": "Book has been updated successfully"
        }, status = status.HTTP_200_OK)

    return Response(data={
        "success": False,
        "message": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def destroy(request, id):
    book = Book.objects.get(pk=id)
    book.delete()
    return Response(data={
            "success": True,
            "message": "Book has been deleted successfully"
        }, status=status.HTTP_200_OK)
