from django.db import models
from calculator.percent_model_constants import PERCENT_TYPES


class Percent(models.Model):
    percent_type = models.CharField(max_length=10, verbose_name='Тип процента', choices=PERCENT_TYPES)
    percent_value = models.FloatField(verbose_name='Значение процента')

    class Meta:
        verbose_name = 'Процент'
        verbose_name_plural = 'Проценты'
