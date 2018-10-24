from factory import DjangoModelFactory, Faker, SubFactory

from .boards import BoardFactory
from .users import UserFactory
from ...models import Topic


class TopicFactory(DjangoModelFactory):
    """
    Defines topic factory
    """
    subject = Faker("sentence", nb_words=3)
    board = SubFactory(BoardFactory)
    starter = SubFactory(UserFactory)

    class Meta:
        model = Topic
