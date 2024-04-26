# Проект "Яндекс.Афиша"
Интерактивную карта на которой можно расположить метки популярных мест с подробными описаниями и комментариями
Пример проекта можно увидеть по следующей [ссылке](https://ziganshinib.pythonanywhere.com/)
![img.png](git_media/img.png)
![img.png](git_media/img2.png)
## Требовании:
Для работы проекта требуется Python 3.8 и старше 

## Как запустить проект 
### 1. Скачивания проекта
```shell
git clone https://github.com/ZiganshinIB/Devman_lesson_1
cd Devman_lesson_1
```
### 2. Установка зависимостей
```shell
pip install -r requirements.txt
```
### 3. Объявление переменных среды (необходимо для запуска пректа)
В файле settings.py есть настройка `SECRET_KEY` — это секретный ключ, применяемое для защиты от [CSRF атак](https://learn.javascript.ru/csrf).
<br> По этой причине ключ хранится в переменной окружение. 
<br> Для этого необходимо создать файл `.env` в директории с проектом
```shell
nano .env
```
И прописать переменную `DJANGO_SECRET_KEY`
```shell
export DJANGO_SECRET_KEY='Ваш секретный ключ'
```
так же можно 
### 4. Миграция базы данных
```shell
python3 manage.py migrate
```
### 5. Добаление администратора сайта (superusre) для входа в панель администратора
```shell
pyhton3 manage.py createsuperuser
```
### 6. Запуск проектка
```shell
python3 manage.py runserver
```
## Добавления данных geojson
Добавление данных в geojson формате производится с помощью команды `joad_place` 
```shell
python3 manage.py load_place https://<адресс к geojson>.json
```
*для проекта использовались Геоданные с https://github.com/devmanorg/where-to-go-places/tree/master/places*
 

## Рекомендации
### Добавьте переменные среды
В ранее созданном файле `.env` рекомендуется дописать следующие переменные
- [ ] `DJANGO_DEBUG` - Режим отладки (`true`или`false`)
- [ ] `DJANGO_ALLOWED_HOSTS` - Список строк, представляющих имена хоста / домена, которые может обслуживать этот сайт Django
Пример заполнения файла
```shell
export DJANGO_SECRET_KEY='Ваш секретный ключ'
export DJANGO_DEBUG=true
export DJANGO_ALLOWED_HOSTS=yourhostname.com,127.0.0.1
```
### Создайте виртуальное окружение
Выпольните следующий команду
```shell
python3 -m venv myenv
```
Активируйте виртуальное окружение
```shell
source myenv/bin/activate
```
Установка зависимостей 
```shell
pip install -r requirements.txt
```
### Публикация на сервере
Перед запуском проекта на сервере соберите все `static`:
```shell
python3 manage.py collectstatic
```
