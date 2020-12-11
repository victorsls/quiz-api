from rest_framework import status
from rest_framework.exceptions import APIException


class MinimumQuestionsException(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = 'This category does not have enough questions'


class MissingQuestionsException(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = "You haven't answered all the questions"


class QuizAnsweredException(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = 'This quiz has already been answered'


class QuizNotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'Quiz not found'
