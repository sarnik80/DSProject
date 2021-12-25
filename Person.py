import enum


class Gender(enum.Enum):
    Male = 0
    Female = 1


class Person:
    # docstring
    """This is a person class"""

    def __init__(self, name='', iD=None, gender=Gender.Male.value, is_married=False, id_spouse=None, parent='0'):
        self.__name = name,
        self.__i_d = iD,
        self.__gender = gender,
        self.__is_married = is_married,
        self.__id_spouse = id_spouse,
        self.__parent = parent

    def data(self):
        return {"name": self.__name,
                "_id": self.__i_d,
                "gender": self.__gender,
                "is_married": self.__is_married,
                "id_spouse": self.__id_spouse,
                "id_parent": self.id_parent
                }

    @property
    def is_married(self):
        return self.__is_married

    @is_married.setter
    def is_married(self, is_marr):
        if isinstance(is_marr, bool):
            self.__is_married = is_marr
        else:
            raise TypeError(f'Expecting an boolean value, got {type(is_marr)}.')

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, type_p):
        if isinstance(type_p, int):
            self.__gender = Gender(type_p)
        elif isinstance(type_p, Gender):
            self.__gender = type_p
        else:
            raise TypeError(f'Expecting an {type(Gender)} or integer, got {type(type_p)}.')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_person):
        if not isinstance(name_person, str):
            raise TypeError(f'Expecting an string, got {type(name_person)}.')
        elif len(name_person) <= 2:
            raise ValueError(f'length of name must be bigger than {len(name_person)}')
        else:
            self.__name = name_person

    @property
    def id(self):
        return self.__i_d

    @id.setter
    def id(self, id_user):
        if not isinstance(id_user, str):
            raise TypeError(f'Expecting an string, got {type(id_user)}.')
        else:
            self.__i_d = id_user

    @property
    def id_spouse(self):
        return self.__id_spouse

    @id_spouse.setter
    def id_spouse(self, id_sp):
        if not isinstance(id_sp, str):
            raise TypeError(f'Expecting an string, got {type(id_sp)}.')
        else:
            self.id_spouse = id_sp

    @property
    def id_parent(self):
        return self.__parent

    @id_parent.setter
    def id_parent(self, parent):
        if not isinstance(parent, str):
            raise TypeError(f'Expecting an string, got {type(parent)}.')
        else:
            self.id_spouse = parent
