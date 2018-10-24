from factory import DjangoModelFactory, Faker

from ...models import Board


class BoardFactory(DjangoModelFactory):
    """
    Defines board factory
    """
    name = Faker("sentence", nb_words=1)
    description = Faker("sentence", nb_words=3)

    class Meta:
        model = Board
