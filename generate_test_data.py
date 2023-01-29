"""Module docstring?"""
from string import ascii_letters

import json
import random as rnd
from datetime import timedelta, datetime


# Класс тестовых данных, сериализуется в json
class TestData:  # Too few public methods. 0/2
    username = ""
    password = ""
    first_name = ""
    last_name = ""
    email = ""
    birthday_date = ""


# класс генерации файла с тестовыми данными
class Generator:  # Too few public methods. 1/2
    # шаблон для формирования username
    user_names = (
        "Dvin", "Stark", "Bull", "Puma", "Askon", "Truck", "Bomb", "Bato", "Lars", "Sky", "Bart", "Brin",
        "Coala", "Spaceman", "Drozd", "Gulf", "BobrDobr", "Pank", "Urgen", "Ilya", "Parnat", "Hazar", "Korn",
        "Dorn", "Dumb", "Tesak", "Tor", "Gor", "Kramp", "Bud", "Crash", "Burn", "Temp", "Jok", "Doc", "Cult",
        "Pick", "Zak", "Zuma", "Quick", "Snack", "Spike", "Tomb", "Halk", "Frost", "Freeze", "Fara", "Mond",
        "Jorg", "Looter", "Splik", "Yorg", "Rust", "Riko", "Dona", "Bark", "Cypro", "Mona", "Nutic", "Nask"
    )
    """Line 23, 24, 25, 26, 27 too long.
    https://peps.python.org/pep-0008/#maximum-line-length"""
    # шаблон для формирования мужских фио
    first_names_m = (
        "Artem", "Aleksey", "Andrey", "Anton", "Afanasiy", "Alexandr", "Anatoliy",
        "Boris", "Boleslav", "Bogdan", "Vasiliy", "Vaicheslav", "Vsevolod", "Vladimir", "Viktor",
        "Georgiy", "Gennadiy", "Gleb", "German", "Dmitriy", "Denis", "Daniil", "Evgeniy", "Egor", "Jora", "Zenon",
        "Zakhar",
        "Igor", "Ibragim", "Ivan", "Ignat", "Konstantin", "Kirill", "Kondrat", "Lev", "Leonid", "Lavrentiy", "Makar",
        "Maksim", "Matvey", "Marat", "Miron", "Mikhail", "Murat", "Nikolay", "Nikodim", "Natan", "Nazar",
        "Oleg", "Osip", "Pavel", "Petr", "Potap", "Ruslan", "Robert", "Rail", "Rustam", "Rinat", "Sergey", "Stanislav",
        "Saveliy", "Stepan", "Semen", "Stanislav", "Spiridon", "Timofey", "Taras", "Timur", "Tixon", "Trofim",
        "Fedot", "Fedor", "Filipp", "Foma", "Edvard", "Eduard", "Ernest", "Yuriy", "Yan", "Yaroslav", "Yakov"
    )
    """Line 35, 37, 38, 39, 40, 41 too long.
    https://peps.python.org/pep-0008/#maximum-line-length"""
    # шаблон для формирования женских фио
    first_names_f = (
        "Alla", "Alina", "Alevtina", "Anna", "Anastasya", "Agata", "Alena", "Broneslava", "Barbara", "Viktorya",
        "Valentina",
        "Vasilina", "Vasilisa", "Vera", "Galina", "Gabriella", "Gera", "Gertruda", "Diana", "Darya", "Elena",
        "Elizaveta",
        "Ekaterina", "Evgenya", "Jozefina", "Janna", "Zoya", "Zara", "Zarina", "Irina", "Klavdya", "Klementina",
        "Karina", "Lera", "Laura", "Lana", "Lusia", "Ludmila", "Lara", "Larisa", "Marya", "Marta", "Natalya", "Olga",
        "Oksana", "Polina", "Paranya", "Pelageya", "Rita", "Raisa", "Ruslana", "Roza", "Rimma", "Svetlana", "Stefanya",
        "Snejanna", "Tatyana", "Tamara", "Tonya", "Uliana", "Ustina", "Faina", "Fedora", "Hloya", "Evelina", "Ella",
        "Emma", "Yana", "Yanina", "Yaroslava", "Yadviga"
    )
    """Line 47, 49, 51, 52, 53, 54 too long.
    https://peps.python.org/pep-0008/#maximum-line-length"""
    # шаблон для формирования фамилий
    last_names = (
        "Ivanov", "Smirnov", "Kuznetsov", "Popov", "Vasilev", "Petrov", "Sokolov", "Mikhaylov", "Novikov", "Fedorov",
        "Morozov", "Volkov", "Alekseev", "Lebedev", "Semenov", "Egorov", "Pavlov", "Kozlov", "Stepanov", "Nikolaev",
        "Orlov", "Andreev", "Makarov", "Nikitin", "Zakharov", "Zaytsev", "Solovev", "Borisov", "Yakovlev", "Grigorev",
        "Romanov", "Vorobev", "Sergeev", "Frolov", "Aleksandrov", "Dmitriev", "Korolev", "Gusev", "Kiselev",
        "Ilin", "Maksimov", "Polyakov", "Sorokin", "Vinogradov", "Kovalev", "Belov", "Medvedev", "Antonov", "Tarasov",
        "Zhukov", "Baranov", "Filippov", "Komarov", "Davydov", "Belyaev", "Gerasimov", "Bogdanov", "Osipov", "Sidorov",
        "Matveev", "Titov", "Markov", "Mironov", "Krylov", "Kulikov", "Karpov", "Vlasov", "Melnikov", "Gavrilov",
        "Tikhonov", "Kazakov", "Afanasev", "Danilov", "Savelev", "Timofeev", "Fomin", "Chernov", "Abramov", "Martynov",
        "Efimov", "Fedotov", "Scherbakov", "Nazarov", "Kalinin", "Isaev", "Chernyshev", "Bykov", "Maslov", "Rodionov",
        "Konovalov", "Lazarev", "Voronin", "Klimov", "Filatov", "Ponomarev", "Golubev", "Kudryavtsev", "Prokhorov",
        "Naumov", "Potapov", "Zhuravlev", "Ovchinnikov", "Trofimov", "Leonov", "Sobolev", "Ermakov", "Kolesnikov",
        "Goncharov", "Emelyanov", "Nikiforov", "Grachev"
    )
    """Line 61-71 too long.
    https://peps.python.org/pep-0008/#maximum-line-length"""
    # формирование тестового файла
    def __init__(self, len_passwd=5):
        self.len_passwd = len_passwd  # длина пароля
        self.dict_names = {}

    # генерация словаря использования user_name
    def _dict_gen(self):
        self.dict_names = {x: 0 for x in self.user_names}

    # Формирование файла с тестовыми данными
    # file_name - имя файла с генерируемыми данными
    # count_person - кол-во генерируемых записей (по умолчанию 500)
    # restart - сбросить счетчик аккаунтов для предыдущей генерации
    def generate_json(self, file_name, count_person, restart):
        """Method docstring?"""
        data_list = []

        # сформировать словарь генерации, если указано или словарь пуст
        if restart or len(self.dict_names) == 0:
            self._dict_gen()

        for i in range(0, count_person):
            data = TestData()
            user_name = self._get_username()
            data.first_name, data.last_name = self._get_name()
            data.username = user_name
            data.email = user_name + "@mail.ru"
            data.password = self._get_password()
            data.birthday_date = self._get_birthday_date()

            data_list.append(data)

        try:
            with open(file_name, "w") as json_file:
                json.dump(data_list, json_file, default=lambda x: x.__dict__, sort_keys=True, indent=2)
                """Line 109 too long.
                https://peps.python.org/pep-0008/#maximum-line-length"""
        except:
            print("Write json-file error!")

    # генерация username
    def _get_username(self):
        user_name = rnd.choice(self.user_names)
        count = self.dict_names[user_name]
        count += 1
        self.dict_names[user_name] = count
        return f'{user_name}{count}'

    # генерация пароля
    def _get_password(self):
        return ''.join(rnd.choice(ascii_letters) for i in range(self.len_passw))

    # генерация имени, возвращает first_name, last_name
    def _get_name(self):
        # определим пол
        gender = rnd.choice(('m', 'f'))
        if gender == 'm':
            return rnd.choice(self.first_names_m), rnd.choice(self.last_names)

        return rnd.choice(self.first_names_f), rnd.choice(self.last_names) + "a"

    # генерация
    def _get_birthday_date(self):
        days_diff = timedelta(rnd.choice(range(20, 60)) * 365 + rnd.randint(0, 365))
        date_new = datetime.now() - days_diff
        return date_new.strftime("%Y-%m-%d")


def main():
    """Function docstring?"""
    generator = Generator(8)
    generator.generate_json("json/users.json", 100, True)


if __name__ == '__main__':
    main()
