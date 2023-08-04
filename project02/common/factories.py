
import factory

from accounts.models import CustomUser
from authors.models import Author

class UserFactory(factory.django.DjangoModelFactory):
    """
    Factory for users who are NOT authors with SET values
    """
    class Meta:
        model = CustomUser

    username = 'asemineko'
    first_name = 'Anna'
    last_name = 'Seminenko'
    email = 'liyvfliyhvlikv@yandex.com'
    password = '32326363'


class RandomUserFactory(factory.django.DjangoModelFactory):
    """
    Factory for generating users who are not authors wirh RANDOM values 
    """
    class Meta:
        model = CustomUser

    username = factory.Faker('user_name')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    password = factory.Faker('password')   


class UserAuthorFactory(factory.django.DjangoModelFactory):
    """
    Factory for Authors who are users with a foreign key field
    """ 
    class Meta:
        model = Author

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    user = factory.SubFactory(RandomUserFactory)
    

class AuthorFactory(factory.django.DjangoModelFactory):
    """
    Factory for Authors who are NOT users.
    """
    class Meta:
        model = Author
        
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')