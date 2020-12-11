from django.urls import path

from api.ranking.views import RakingAPIView

urlpatterns = [
    path('', RakingAPIView.as_view(), name='ranking')
]

app_name = 'ranking'
