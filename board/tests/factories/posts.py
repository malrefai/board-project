from factory import DjangoModelFactory, Faker, SubFactory

from .topics import TopicFactory
from .users import UserFactory
from ...models import Post


class PostFactory(DjangoModelFactory):
    """
    Defines post factory
    """
    message = Faker("sentence", nb_words=5)
    topic = SubFactory(TopicFactory)

    created_by = SubFactory(UserFactory)
    updated_by = SubFactory(UserFactory)

    class Meta:
        model = Post
