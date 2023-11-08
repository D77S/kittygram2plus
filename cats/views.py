from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
#  from rest_framework.throttling import AnonRateThrottle
from rest_framework.throttling import ScopedRateThrottle
#  from rest_framework.pagination import PageNumberPagination
#  from rest_framework.pagination import LimitOffsetPagination
#  from .pagination import CatsPagination

from .models import Achievement, Cat, User
from .serializers import AchievementSerializer, CatSerializer, UserSerializer
from .permissions import OwnerOrReadOnly
from .throttling import WorkingHoursRateThrottle


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all().order_by('id')
    serializer_class = CatSerializer
    permission_classes = (OwnerOrReadOnly,)
    # throttle_classes = (AnonRateThrottle,)  # Подключили AnonRateThrottle
    # Если кастомный тротлинг-класс вернёт True - запросы будут обработаны
    # Если он вернёт False - все запросы будут отклонены
    throttle_classes = (WorkingHoursRateThrottle, ScopedRateThrottle)
    # А далее применится лимит low_request
    # Для любых пользователей установим кастомный лимит 1 запрос в минуту
    throttle_scope = 'low_request'
    #  pagination_class = CatsPagination
    #  pagination_class = PageNumberPagination
    #  pagination_class = LimitOffsetPagination
    # Указываем фильтрующий бэкенд DjangoFilterBackend
    # Из библиотеки django-filter
    # И еще добавим в кортеж ещё один бэкенд
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    # Временно отключим пагинацию на уровне вьюсета,
    # так будет удобнее настраивать фильтрацию
    pagination_class = None
    # Фильтровать будем по полям color и birth_year модели Cat
    filterset_fields = ('color', 'birth_year')
    search_fields = ('^name', 'achievements__name', 'owner__username')
    ordering = ('birth_year',)
    ordering_fields = ('name', 'birth_year')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
