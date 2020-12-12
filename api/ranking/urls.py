from django.urls import path

from api.ranking.views import RankingAPIView

urlpatterns = [
    path('', RankingAPIView.as_view(), name='ranking')
]

app_name = 'ranking'
