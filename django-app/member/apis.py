import requests
from django.conf import settings
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView


class FacebookLoginAPIView(APIView):
    APP_ACCESS_TOKEN = '{}|{}'.format(
        settings.FACEBOOK_APP_ID,
        settings.FACEBOOK_SECRET_CODE,
    )
    def post(self,request):
        token = request.data.get('token')
        if not token:
            raise APIException('token require')

        debug_result = self.debug_token(token)

    def debug_token(self,token):
        url_debug_token = 'https://graph.facebook.com/debug_token'
        url_debug_token_params = {
            'input_token': token,
            'access_token': self.APP_ACCESS_TOKEN
        }
        response = requests.get(url_debug_token, url_debug_token_params)
        result = response.json()
        if 'error' in result['data']:
            raise APIException('token invalid')
        else:
            return result