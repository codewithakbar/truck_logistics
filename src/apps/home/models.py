import datetime
from django.db import models


class Products(models.Model):

    CURRENCY_TYPE = (("uzs", "UZS"), ("usd", "USD"), ("eur", "EUR"))

    TRANSPORT_TYPE = (
        ("truck", "TRUCK"),
        ("trailer", "TRAILER"),
    )

    email = models.EmailField()
    phone = models.CharField(max_length=13)

    olib_ketish = models.CharField(max_length=70)
    tashlab_ketish = models.CharField(max_length=70)
    yuk_turi = models.CharField(max_length=30)
    yuk_vazni = models.IntegerField(verbose_name="Yuk vazni (t)")
    yuk_hajmi = models.IntegerField(verbose_name="Yuk hajmi (m3)")
    transport_turi = models.CharField(max_length=30, choices=TRANSPORT_TYPE)
    yuk_moshina_soni = models.IntegerField(default=1)

    uzunlik = models.IntegerField(verbose_name="Uzunlik (m)")
    kenglik = models.IntegerField(verbose_name="Kenglik (m)")
    balandlik = models.IntegerField(verbose_name="Balandlik (m)")

    price = models.IntegerField()
    price_type = models.CharField(max_length=30, choices=CURRENCY_TYPE, default="uzs")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.olib_ketish + " - " + self.tashlab_ketish
