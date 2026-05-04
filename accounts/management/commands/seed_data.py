import random
from faker import Faker
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from locations.models import Country, City
from accounts.models import User, UserProfile, Agency, Agent

User = get_user_model()
faker = Faker()


class Command(BaseCommand):
    help = "Seed full travel data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding data...")

        # Country and city
        countries = []
        used_codes = set()

        for _ in range(5):
            code = faker.country_code()

            if code in used_codes:
                continue
            used_codes.add(code)

            country = Country.objects.create(name=faker.country(), code=code)
            countries.append(country)

            for _ in range(3):
                City.objects.create(country=country, name=faker.city())
        cities = list(City.objects.all())

        agency = Agency.objects.create(
            name=faker.name(),
            slug=faker.slug(),
            email=faker.email(),
            phone=faker.phone_number(),
            address=faker.address()
        )

        for i in range(5):
            user = User.objects.create(
                email=f"user{i}@example.com",
                password="123456",
                phone = faker.phone_number(),
                first_name = faker.first_name(),
                last_name = faker.last_name(),
            )

            user_profile = UserProfile.objects.create(
                user = user,
                date_of_birth = faker.date_of_birth(),
                nationality = faker.country(),
                address = faker.address(),
                passport_number = faker.passport_number(),
            )

            agent = Agent.objects.create(
                user = user,
                company_name = agency,
                license_number = faker.random_number()
            )