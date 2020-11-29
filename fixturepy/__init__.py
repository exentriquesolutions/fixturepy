import random
import uuid


def _string():
    return uuid.uuid4().hex


def _int(fixture_range=(0, 99999)):
    return random.randint(fixture_range[0], fixture_range[1] + 1)


def _email():
    return '%s@%s.com' % (_string(), _string())


def _float(fixture_range=(0, 1)):
    return random.uniform(fixture_range[0], fixture_range[1])


class Email:
    def __init__(self):
        pass


class Fixture:
    factories = {
        str: _string,
        int: _int,
        float: _float,
        Email: _email,
    }

    def __call__(self, cls, **factory_args):
        return self.create(cls, **factory_args)

    def __init__(self):
        pass

    def create(self, cls, **factory_args):
        factory = self.factories.get(cls)
        if factory:
            return factory(**factory_args)
        raise ValueError('Unsupported type %s' % cls)
