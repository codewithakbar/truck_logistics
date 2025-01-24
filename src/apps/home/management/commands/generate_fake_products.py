from django.core.management.base import BaseCommand
from faker import Faker
from apps.home.models import Products
import random

class Command(BaseCommand):
    help = "Generate fake products for testing with Uzbekistan-specific data"

    def handle(self, *args, **kwargs):
        # Initialize Faker instance
        fake = Faker()

        # O‘zbekiston shaharlarining ro‘yxati
        uzbek_cities = [
            "Toshkent", "Samarqand", "Buxoro", "Andijon", "Namangan",
            "Farg‘ona", "Xiva", "Urganch", "Qo‘qon", "Navoiy",
            "Qarshi", "Termiz", "Guliston", "Jizzax", "Nukus",
            "Chirchiq", "Angren", "Bekobod", "Olmaliq", "Marg‘ilon"
        ]

        # Number of products to create
        num_products = 50  # You can adjust this number

        for _ in range(num_products):
            # Generate fake Uzbek-specific data
            email = fake.email()
            phone = f"+998{random.randint(90, 99)}{random.randint(1000000, 9999999)}"  # Uzbek phone format
            olib_ketish = random.choice(uzbek_cities)
            tashlab_ketish = random.choice(uzbek_cities)
            yuk_turi = fake.word()
            yuk_vazni = random.randint(1, 100)  # Random weight in tons
            yuk_hajmi = random.randint(1, 100)  # Random volume in m3
            transport_turi = random.choice(["truck", "trailer"])
            yuk_moshina_soni = random.randint(1, 10)  # Random number of transport units
            uzunlik = random.randint(1, 20)
            kenglik = random.randint(1, 10)
            balandlik = random.randint(1, 10)
            price = random.randint(1000000, 100000000)  # Price in UZS
            price_type = random.choice(["uzs", "usd", "eur"])  # Random currency type

            # Create and save the product
            product = Products(
                email=email,
                phone=phone,
                olib_ketish=olib_ketish,
                tashlab_ketish=tashlab_ketish,
                yuk_turi=yuk_turi,
                yuk_vazni=yuk_vazni,
                yuk_hajmi=yuk_hajmi,
                transport_turi=transport_turi,
                yuk_moshina_soni=yuk_moshina_soni,
                uzunlik=uzunlik,
                kenglik=kenglik,
                balandlik=balandlik,
                price=price,
                price_type=price_type
            )

            product.save()

        self.stdout.write(self.style.SUCCESS(f"{num_products} products created successfully with Uzbekistan-specific data!"))
