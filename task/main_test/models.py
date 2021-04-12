from django.db import models


class Deal(models.Model):
    customer = models.CharField(verbose_name='Наименование товара', max_length=70)
    item = models.CharField(verbose_name='Наименование товара', max_length=70)
    total = models.DecimalField(verbose_name='Сумма сделки', max_digits=10, decimal_places=2)
    quantity = models.IntegerField(verbose_name='Колличество товара, шт')
    date = models.DateTimeField(verbose_name='Дата и время регистрации сделки')

    def __str__(self):
        return f'{self.customer}{self.item}{self.total}{self.quantity}{self.date}'

    class Meta:
        verbose_name = 'Сделка'
        verbose_name_plural = 'Сделки'