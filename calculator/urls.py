from django.urls import path
from calculator.views import GetCalculatorInfo

urlpatterns = [
    path('calculator/rates', GetCalculatorInfo.as_view(), name='Данные для калькулятора')
]