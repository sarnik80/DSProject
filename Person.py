import enum

class Person:
    # docstring
    """This is a person class"""

    def __init__(self, name='', iD=None, gender=0, id_spouse=None, parent='0', level=0):
        self.__name = name,
        self.__i_d = iD,
        self.__gender = gender,
        self.__id_spouse = id_spouse,
        self.__parent = parent
        self.__level = level

    def data(self):
        return {"name": self.__name,
                "id_user": self.__i_d,
                "gender": self.__gender,
                "id_spouse": self.__id_spouse,
                "id_parent": self.id_parent,
                'level': self.__level
                }

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, lvl):
        if not isinstance(lvl, int):
            raise TypeError(f'Expecting an integer, got {type(lvl)}.')
        else:
            self.__level = lvl

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, type_p):
        if not isinstance(type_p, int):
            raise TypeError(f'Expecting an integer, got {type(type_p)}.')
        else:
            self.__gender = type_p


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
