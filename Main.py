from Person import Person

from DataBase import data_base

all_person = []
all_id = []
person = None
my_bd = None
error_str = 'error!'
done_str = 'done!'


def get_id(item):
    return item['id_user']


def get_all_id():
    if len(all_person) != 0:
        return list(map(get_id, all_person))


def get_something(string):
    name = input(string)
    if not name.isalpha():
        raise TypeError
    return name


def create_db():
    try:
        nameDB = get_something('Enter name of db : ')
        my_bd = data_base(name_db=nameDB)
    except:
        create_db()
        print(error_str)
    else:
        return my_bd


def create_or_use_database():
    global my_bd
    my_bd = create_db()
    global all_person
    global all_id
    all_person = my_bd.find_all_person()
    all_id = get_all_id()
    # create tree with all person function


def get_name_person():
    if person:

        try:
            name_person = get_something('enter name of Person : ')
            person.name = name_person
            print(done_str)
        except:
            get_name_person()
            print(error_str)


def get_id_person():
    if person:

        try:
            id_person = int(input('enter id of person : '))
            if len(all_id) != 0:
                if id_person in all_id:
                    raise ValueError
                else:
                    person.id = str(id_person)
        except:
            print(error_str)
            get_id_person()
        else:
            print(done_str)


def get_gender():
    if person:
        try:
            gender = int(input('enter  gender of person [ Male (0) | Female (1)] : '))
            if not gender in [0, 1]:
                raise ValueError
            else:
                person.gender = gender
        except:
            print(error_str)
            get_gender()
        else:
            print(done_str)


def get_id_spouse():
    if person:

        try:
            spouse = 'wife' if person.gender[0] == 0 else 'husband'
            id_person = int(input(f'enter id of your {spouse} : '))
            if len(all_id) != 0:
                if id_person in all_id:
                    raise ValueError
                else:
                    person.id_spouse = str(id_person)
        except:
            print(error_str)
            get_id_spouse()
        else:
            print(done_str)


# sample
def add_tree_to_db():
    pass
    # if my_bd and all_person:
    #     my_bd.insert_list_of_person(all_person)


def add_person():
    global person
    person = Person()
    all_person.append(person)
    print('done!')
