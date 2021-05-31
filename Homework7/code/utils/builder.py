from dataclasses import dataclass
import faker
import random
fake = faker.Faker(['en_US'])


@dataclass
class Human:
    id: int = None
    name: str = None
    surname: str = None
    age: int = None


class HumanBuilder:

    @staticmethod
    def generate_human(id=None, name=None, surname=None, age=None):

        if name is None:
            name = fake.name().split(' ')[0]

        if surname is None:
            surname = fake.name().split(' ')[1]

        if age is None:
            age = random.randint(0, 130)

        return Human(id=id, name=name, surname=surname, age=age)


def generate_human_data(id=None, name=None, surname=None, age=None):
    human = HumanBuilder.generate_human(id, name, surname, age)
    return {'id': human.id, 'name': human.name, 'surname': human.surname, 'age': human.age}


def return_human_data_without_name(human):
    return {'id': human['id'], 'surname': human['surname'], 'age': human['age']}
