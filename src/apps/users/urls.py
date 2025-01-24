from django.urls import path, include
from . import views
from .viewsets import (
    DashboardView,
    LoginUserView,
    LogoutView,
    RegisterUserView,
    get_all_users,
    get_all_users_lang,
    get_user_details,
)
from rest_framework import routers
from rest_framework.authtoken import views as auth_views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)

urlpatterns = [
    path("register/", views.user_register, name="user_register"),
    path("login/", views.user_login, name="user_login"),
    path("logout/", views.user_logout, name="user_logout"),
    path("profile/", views.user_profile, name="user_profile"),
    path("", views.user_list, name="user_list"),
    path("create/", views.user_create, name="user_create"),
    path("update/<int:pk>/", views.user_update, name="user_update"),
    path("delete/<int:pk>/", views.user_delete, name="user_delete"),
    path("api/", include(router.urls)),
    path("api/auth/", auth_views.obtain_auth_token),
    path("user/<int:user_id>/", get_user_details, name="get_user_details"),
    path("users/", get_all_users, name="get_all_users"),
    path("lang/users/", get_all_users_lang, name="get_all_users_lang"),
    
    path("api/register/", RegisterUserView.as_view(), name="register"),
    path("api/login/", views.MyTokenObtainPairView.as_view(), name="login"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/dashboard/", DashboardView.as_view(), name="api_dashboard"),
    path("api/logout/", LogoutView.as_view(), name="api_logout"),
]
