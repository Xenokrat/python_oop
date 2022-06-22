# Difference to use class / static methods ?

class Item:
    @staticmethod
    def is_integer():
        '''
        This should do something that has a relationship
        with the class, but not something that must be unique
        per instance!
        '''

    @classmethod
    def instance_from_something(cls):
        '''
        This should also do something that has a relationship
        with the class, but usually, those are used to
        manipulate different structures of data to instance
        objects, like we have done with CSV.
        '''


# However, those could by also called from instances.

item1 = Item()
item1.is_integer(5)
item1.instance_from_something()