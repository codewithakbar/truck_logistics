import json
import asyncio
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import update_last_login
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from django.middleware.csrf import get_token
from django.forms.models import model_to_dict
from django.views import View
from .models import User
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer
from asgiref.sync import sync_to_async


@method_decorator(csrf_exempt, name="dispatch")
class RegisterUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class LoginUserView(TokenObtainPairView):
    pass


@method_decorator(login_required, name="dispatch")
class DashboardView(View):
    def get(self, request):
        return JsonResponse(
            {
                "message": "Dashboard sahifasi",
                "user": model_to_dict(request.user, exclude=["password"]),
            }
        )


@method_decorator(csrf_exempt, name="dispatch")
class LogoutView(View):
    def post(self, request):
        try:
            request.user.auth_token.delete()
            return JsonResponse(
                {"message": "Tizimdan muvaffaqiyatli chiqdingiz!"}, status=200
            )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


async def get_user_details(request, user_id):

    user = await asyncio.to_thread(get_object_or_404, User, id=user_id)

    data = {
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "phone_number": user.phone_number,
    }
    return JsonResponse(data)


@sync_to_async
def get_users():
    return list(User.objects.all())


# @cache_page(60 * 15)
async def get_all_users(request):
    users = await get_users()

    data = [
        {
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "phone_number": user.phone_number,
        }
        for user in users
    ]

    return JsonResponse(data, safe=False)


@require_POST
@csrf_exempt
async def get_all_users_lang(request):
    """
    Foydalanuvchilar ro'yxatini berilgan tilga mos ravishda qaytaradi.

    POST so'rovi bo'lishi kerak va headerda 'lang' parametri orqali til ko'rsatilishi kerak (uz, ru, en).
    """
    try:
        lang = request.headers.get("lang")

        if not lang:
            lang = "uz"

        if lang not in ["uz", "ru", "en"]:
            return JsonResponse(
                {
                    "error": "Noto'g'ri til tanlandi. 'uz', 'ru' yoki 'en' qiymatlarini kiriting."
                },
                status=400,
            )

        users = await get_users()
        response_data = []

        for user in users:
            user_data = {
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "phone_number": user.phone_number,
            }

            if lang == "uz":
                user_data["uz_message"] = (
                    f"Assalomu alaykum {user.first_name} {user.last_name}!"
                )
            elif lang == "ru":
                user_data["ru_message"] = (
                    f"Здравствуйте {user.first_name} {user.last_name}!"
                )
            elif lang == "en":
                user_data["en_message"] = f"Hello {user.first_name} {user.last_name}!"

            response_data.append(user_data)

        return JsonResponse(response_data, safe=False)

    except Exception as e:
        return JsonResponse({"error": f"Xatolik yuz berdi: {str(e)}"}, status=500)
