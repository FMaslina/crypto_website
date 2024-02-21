from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from calculator.misc import get_exchange_rate
from calculator.models import Percent


class GetCalculatorInfo(APIView):
    def get(self, request):
        buy_percent = Percent.objects.filter(percent_type='Покупка').last()
        sell_percent = Percent.objects.filter(percent_type='Продажа').last()
        change_rate = get_exchange_rate()

        return Response(data={'buy_percent': buy_percent.percent_value, 'sell_percent': sell_percent.percent_value,
                              'change_rate': change_rate}, status=status.HTTP_200_OK)
