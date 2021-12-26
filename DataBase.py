import pymongo


# to create a database in MongoDB , We have to create a MongoClient object
def create_mongo_client_object():
    my_client = pymongo.MongoClient("mongodb://localhost:27017/")

    return my_client


# to create a database
def create_data_base(url):
    if not isinstance(url, str):
        raise TypeError(f'Expecting an integer, got {type(url)}.')
    return create_mongo_client_object()[url]


# to create collection
def create_collection(name, database):
    return database[name]


class data_base:
    """class to create my database and Define required functions """

    def __init__(self, name_db='MyDATA', name_collection='person'):
        self.data_base = create_data_base(name_db)
        self.collection = create_collection(name_collection, self.data_base)

        return
    def insert_list_of_person(self, list_person):
        list_person = [item.data() for item in list_person]
        return self.collection.insert_many(list_person)

    def find_all_person(self):
        all_person = [item for item in self.collection.find()]

        return all_person
