class Notebook:
    max_people_on_list = 10

    @classmethod
    def get_max_people(cls):
        return cls.max_people_on_list

    @staticmethod
    def message_success():
        return f"Operation performed successfully."

    def __init__(self):
        self.__people_list = list()

    @property
    def get_people_on_list(self):
        return self.__people_list

    def append_people(self, value):
        if len(self.__people_list) < Notebook.max_people_on_list:
            self.__people_list.append(value)
            print(self.message_success())
        else:
            print("This person was not appended on the list.")

    def remove_people(self, value):
        if self.__people_list:
            try:
                self.__people_list.remove(value)
            except (ValueError, TypeError) as err:
                print(f"This value is not present: {err}")
            else:
                print(self.message_success())

    def get_index_person(self, value):
        return self.__people_list.index(value)

    def print_notebook(self):
        if len(self.__people_list) > 0:
            for people in self.__people_list:
                print(f"Name: {people.name}\n"
                      f"Age: {people.age}\n"
                      f"Height: {people.heigth}")
    # como python não é tipado, ele não sabe o tipo de objeto que vai receber
    # dessa forma, ele também não sabe os métodos que tal objeto possui, assim sendo
    # é necessário colocar os métodos no objeto "na mão", diferente de JAVA, que a
    # liguagem já sabe os métodos que podem ser usados e a IDE recomenda.
