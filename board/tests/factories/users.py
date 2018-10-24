from django.contrib.auth.models import User

from factory import DjangoModelFactory, Faker


class UserFactory(DjangoModelFactory):
    """
    Define user factory
    """
    first_name = Faker("first_name")
    last_name = Faker("last_name")
    username = Faker("name")
    email = Faker("email")

    class Meta:
        model = User
