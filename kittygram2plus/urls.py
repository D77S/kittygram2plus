from rest_framework import routers, permissions

from django.contrib import admin
from django.urls import include, path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url

from cats.views import AchievementViewSet, CatViewSet, UserViewSet


router = routers.DefaultRouter()
router.register(r'cats', CatViewSet)
router.register(r'users', UserViewSet)
router.register(r'achievements', AchievementViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
# superuser login/pass admin1/admin1
#
# user_id2 login/pass user1/pass1pass1, token:
#  "refresh": ("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmV" +
# "mcmVzaCIsImV4cCI6MTY5OTUzNDc2NywianRpIjoiMjIzMWNhNDhhN2VmNDliZTgwMDliZjYxZmE2ZWIyNTYiLCJ1c2VyX2lkIjoyfQ.1QYG3Fe98iiF9ry6V8VGTSGMJ6ATbhVa6-vhTf8gmDc"),
#      "access": ("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoi" +
# "YWNjZXNzIiwiZXhwIjoxNzg1NzYxOTY3LCJqdGkiOiIxNGY5YzVkOWZkZTQ0ODFiOTM2OTQxZTBhNjdkN2UwMiIsInVzZXJfaWQiOjJ9.YTiv9jRSRgvXWvV0PLrEcMcI0ELH-ulokSXGhYbGdOY")
schema_view = get_schema_view(
   openapi.Info(
      title="Cats API",
      default_version='v1',
      description="Документация для приложения cats проекта Kittygram",
      # terms_of_service="URL страницы с пользовательским соглашением",
      contact=openapi.Contact(email="admin@kittygram.ru"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
   url(r'^swagger(?P<format>\.json|\.yaml)$',
       schema_view.without_ui(cache_timeout=0), name='schema-json'),
   url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
       name='schema-swagger-ui'),
   url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
       name='schema-redoc'),
]
