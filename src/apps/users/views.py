from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from rest_framework import viewsets, permissions
from .serializers import UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from django.views.decorators.cache import cache_page

User = get_user_model()


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def user_register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def user_login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
    else:
        return Response(
            {"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def user_logout(request):
    logout(request)
    return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


@login_required
def user_profile(request):
    user = request.user
    return render(request, "user_profile.html", {"user": user})


# @login_required
@cache_page(60 * 15)
def user_list(request):
    users = User.objects.all()
    return render(request, "user_list.html", {"users": users})


@login_required
def user_create(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user_list")
    else:
        form = UserForm()
    return render(request, "user_form.html", {"form": form})


@login_required
def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("user_list")
    else:
        form = UserUpdateForm(instance=user)
    return render(request, "user_form.html", {"form": form})


@login_required
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        user.delete()
        return redirect("user_list")
    return render(request, "user_delete.html", {"user": user})
