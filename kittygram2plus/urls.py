from rest_framework import routers

from django.contrib import admin
from django.urls import include, path

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
