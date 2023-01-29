# Сайт + back к нему.

## Развертывание проекта на локальной машине
Все рекомендации написаны под **Ubuntu 22.04**, на **windows** не проверял.
По всем вопросам стучите https://t.me/Flopp

#### **Ubuntu**
1) Скопируйте репозиторий на локальный компьютер ```git clone *ssh ссылка на репо*```
2) Установите python 3.11 
    ``` 
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install python3.11
    ```
3) Создайте виртуальное окружение в корне проекта ```python3 -m venv env``` 
4) Установите pip ```sudo apt install pip```
5) Загрузите зависимости ```pip3 install -r requirements.txt```
6) Создайте файл в корне проекте ```.env``` и перенесите в него переменные из файла ```.env.sample``` (за тем, что ставить на место значений - в тг)
7) Выполните миграции в базу данных ```python3 manage.py migrate```
8) Заполните базу тестовыми данными ```python3 manage.py filling_test_data```
9) Запустите DRF приложение ```python3 manage.py runserver``` (по умолчанию запускается 127.0.0.1:8000)


***Будет дополняться в процессе***

#### **Windows**
1) Скопируйте репозиторий на локальный компьютер ```git clone *ssh ссылка на репо*```
2) Установите python 3.11 https://www.python.org/downloads/
3) Создайте виртуальное окружение в корне проекта ```python -m venv env``` 
4) Проверьте, установлен ли pip (менеджер пакетов). Проверить командой ```pip --version```. Если нет - вот ссылка https://www.dataquest.io/blog/install-pip-windows/)
5) Загрузите зависимости ```pip install -r requirements.txt```
6) Создайте файл в корне проекте ```.env``` и перенесите в него переменные из файла ```.env.sample``` (за тем, что ставить на место значений - в тг)
7) Выполните миграции в базу данных ```python manage.py migrate```
8) Заполните базу тестовыми данными ```python manage.py filling_test_data```
9) Запустите DRF приложение ```python manage.py runserver``` (по умолчанию запускается 127.0.0.1:8000)

***Будет дополняться в процессе***


## Main back TODO
- [x] Создать приложение
- [x] Создать модель пользователя
- [x] Дополнить json тестовыми данными для пользователей (json/users.json)
- [ ] Создать модель резюме
- [ ] Создать json с тестовыми данными для резюме
- [ ] Создать модель вакансии
- [ ] Создать json с тестовыми данными для вакансий
- [ ] Реализовать заполнение тестовыми данные
- [ ] Запустить react приложение
- [ ] Реализовать функционал авторизации
- [ ] Реализовать систему прав/ доступов
- [ ] Реализовать функционал авторизации через сторонние ресурсы? (уточнить у фронта / ресерч информации, как делается на стеке react + drf)


## Main front TODO
- [ ] Заполнить TODO 

## Генератор тестовых данных - GenTestData

Готовит json-файл согласно заданной структуры:

```json
[
  {
    "username": "DarkSide",
    "password": "1111",
    "first_name": "Daniil",
    "last_name": "Gusevskii",
    "email": "test@django.local",
    "birthday_date": "1993-12-11"
  },
  . . .
]
```
Для генерации использует предопределенные наборы ников пользователей, мужских и женских имен, фамилий. 
Женскине фамилии формируются путем присоединеняи символа 'a' к фамилии из предопределенного набора.

При инициализации генератора можно задать длину получаемого пользовательского пароля (по умолчаниб - 5 символов).

Во время генерации для получения уникальных значений **username** и **email** используются счетчики. Значение которых 
увеличивается на 1 и добавляется к выбранному случайным образом пользовательскому нику. Адрес электронной почты получается 
из username + "@mail.ru".

Для получения файла следует используется метод ```generate_json(file_name, count_person, restart)```, где:
+ **_file_name_** - имя генерируемого json-файла 
+ **_count_person_** - количество json-записей в файле
+ **_restart_** - признак сброса счетчиков генерации 

GenTestData можно использовать для получения нескольких тестовых фалов, с неповторяющимися значениями username. Для этого 
следует установить параметр ```restart = false```. В данном случае генерация будет проходить без сброса счетчиков использования 
значенией username.

Пример:

```python
    # Данный вызов сгенерирует файл testdata.json
    # содержащий даные о 100 пользователях 
    # нумерация usernames будет начата с начала

    generator = GenTestData(8)
    generator.generate_json("testdata.json", 100, True)
```

