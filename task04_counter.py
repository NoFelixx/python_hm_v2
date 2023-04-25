import functools


def instances_counter(cls):

    @functools.wraps(cls, updated=())
    class DecoratedClass(cls):
        counter = 0

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            DecoratedClass.counter += 1

        @classmethod
        def get_created_instances(cls):
            return cls.counter

        @classmethod
        def reset_instances_counter(cls):
            memorized_counter = cls.counter
            cls.counter = 0
            return memorized_counter
    return DecoratedClass


@instances_counter
class User:
    pass
