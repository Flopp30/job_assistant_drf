# TODO здесь Андрей пишет заполнения тестовыми данными JSON'ов. Путь /json/*
import json

# Класс тестовых данных, сериализуется в json
class TestData:
    username = ""
    password = ""
    first_name = ""
    last_name = ""
    email = ""
    birthday_date = ""

# класс генерации файла с тестовыми данными
# len_passw         - длинна генерируемого пароля
# email_template    - основа для генерации email адреса
class GenTestData:
    # шаблон для формирования username
    user_names = (
        "Dvin", "Stark", "Bull", "Puma", "Askon", "Truck", "Bomb", "Bato", "Lars", "Sky", "Bart", "Brin",
        "Coala", "Spaceman", "Drozd", "Gulf", "BobrDobr", "Pank", "Urgen", "Ilya", "Parnat", "Hazar", "Korn",
        "Dorn", "Dumb", "Tesak", "Tor", "Gor", "Kramp", "Bud", "Crash", "Burn", "Temp", "Jok", "Doc", "Cult",
        "Pick", "Zak", "Zuma", "Quick", "Snack", "Spike", "Tomb", "Halk", "Frost", "Freeze", "Fara", "Mond",
        "Jorg", "Looter", "Splik", "Yorg", "Rust", "Riko", "Dona", "Bark", "Cypro", "Mona", "Nutic", "Nask"
    )

    # шаблон для формирования мужских фио
    first_names_m = [(
        "Artem", "Aleksey", "Andrey", "Anton", "Afanasiy", "Alexandr", "Anatoliy",
        "Boris", "Boleslav", "Bogdan", "Vasiliy", "Vaicheslav", "Vsevolod", "Vladimir", "Viktor",
        "Georgiy", "Gennadiy", "Gleb", "German", "Dmitriy", "Denis", "Daniil", "Evgeniy", "Egor", "Jora", "Zenon", "Zakhar",
        "Igor", "Ibragim", "Ivan", "Ignat", "Konstantin", "Kirill", "Kondrat", "Lev", "Leonid", "Lavrentiy", "Makar",
        "Maksim", "Matvey", "Marat", "Miron", "Mikhail", "Murat", "Nikolay", "Nikodim", "Natan", "Nazar",
        "Oleg", "Osip", "Pavel", "Petr", "Potap", "Ruslan", "Robert", "Rail", "Rustam", "Rinat", "Sergey", "Stanislav",
        "Saveliy", "Stepan", "Semen", "Stanislav", "Spiridon", "Timofey", "Taras", "Timur", "Tixon", "Trofim",
        "Fedot", "Fedor", "Filipp", "Foma", "Edvard", "Eduard", "Ernest", "Yuriy", "Yan", "Yaroslav", "Yakov"
    ), (
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
    )]
    # шаблон для формирования женских фио

    # формирование тестового файла
    def __init__(self, len_passw=5, email_template='test'):
        self.len_passw = len_passw
        self.email_template = email_template

    # Формирование файла с тестовыми данными
    # file_name - имя файла с генерируемыми данными, по умолчанию test.json в каталоге
    def generate_json(self, file_name='/json/test.json'):
        pass

    # генерация username
    def _get_username(self):
        pass

    # генерация пароля
    def _get_password(self):
        pass

    # генерация first_name
    def _get_first_name(self):
        pass

    # генерация last_name
    def _get_last_name(self):
        pass

    # генерация
    def _get_email(self):
        pass

    # генерация
    def _get_birthday_date(self):
        pass

def main():
    pass


if __name__ == '__main__':
    main()
