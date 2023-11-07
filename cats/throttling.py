from rest_framework import throttling

import datetime


class WorkingHoursRateThrottle(throttling.BaseThrottle):

    def allow_request(self, request, view):
        #  Кастомные тротлинг-классы принято описывать
        #  и хранить в файле throttling.py.
        #  Их наследуют от базового класса BaseThrottle,
        #  и в наследнике описывают метод allow_request.
        #  Этот метод должен возвращать True, если нужно разрешить запрос,
        #  и False — если запрос следует отклонить.
        now = datetime.datetime.now().hour
        if now >= 3 and now <= 5:
            return False
        return True
