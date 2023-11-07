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
#  "mcmVzaCIsImV4cCI6MTY5OTQ0MzgwMSwianRpIjoiNDhhZmJkNWI5ZGVlNGJiOWFkZmM2M2JhZmE1ZjE3MTgiLCJ1c2VyX2lkIjoyfQ.MnDnW4vQK2dOQEE_m2j_j-hpVitxLkWw-r2lWdpO6uY"),
#    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWN" +
#  "jZXNzIiwiZXhwIjoxNjk5NDQzODAxLCJqdGkiOiI5ZWZkMDA2MjNhNDI0NWQ5YTk0ZjgzMzMyMzMyNWRiMCIsInVzZXJfaWQiOjJ9.k_Yg6a4QIJGDZdvR3bWL2AOZsdWtHPrDDRMPbnzsM4s"
#
# user_id3 login/pass user2/user2, token:
# "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmc" +
#  "mVzaCIsImV4cCI6MTY5OTQ0MzkyNCwianRpIjoiZDIyNGFkNGQyYjg1NDExYWJiNzI5OTBiOWI0NmE4YTciLCJ1c2VyX2lkIjozfQ.b7Sqr-mpC52IjwvSEjsHxj0l74hiJdG9c4OUagmyTtY",
#    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWN" +
#  "jZXNzIiwiZXhwIjoxNjk5NDQzOTI0LCJqdGkiOiJjZDRkNTU4Njg3MTk0ODBmOTAxZDZmZDkyYjczZWE5NiIsInVzZXJfaWQiOjN9.eLf0sYMyVBWVR2_8MdDrJerZ8bpXoIsgzj25r8a1O54"
