from rest_framework import status

from library.exceptions import BaseAPIException


class ValidationException(BaseAPIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Invalid data provided'
    default_code = 'validation_error'
