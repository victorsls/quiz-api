from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.quiz.models import Quiz


class RakingAPIView(APIView):
    """
    A simple APIView to list the Ranking
    """
    queryset = Quiz.objects.all()

    def get(self, request):
        category = request.query_params.get('category')
        if category:
            quizzes = self.queryset.filter(category=category)
        else:
            quizzes = self.queryset.all()
        quizzes.exclude(player=None).order_by('player')

        user_score = {}
        for quiz in quizzes:
            key = quiz.player.username
            if user_score.get(key):
                user_score[key] += quiz.score
            else:
                user_score[key] = quiz.score
        ranking = []
        for username, score in reversed(sorted(user_score.items(), key=lambda x: x[1])):
            ranking.append({'username': username, 'score': score})
        return Response(ranking, status=status.HTTP_200_OK)
