# Проект "Яндекс.Афиша"
Интерактивную карта на которой можно расположить метки популярных мест с подробными описаниями и комментариями
Пример проекта можно увидеть по следующей [ссылке](https://ziganshinib.pythonanywhere.com/)
![img.png](git_media/img.png)
![img.png](git_media/img2.png)
## Как запустить проект 
1. Необходимо Скачать проект  
```shell
git clone https://github.com/ZiganshinIB/Devman_lesson_1
cd Devman_lesson_1
```
2. Необходимо установить зависимости
```shell
pip install -r requirements.txt
```
3. Необходимо мигрировать 
```shell
python3 manage.py migrate
```
4. Запуск проектка
```shell
python3 manage.py runserver
```
## Добавления данных geojson
Добавление данных в geojson формате производится с помощью команды `joad_place` 
```shell
python3 manage.py load_place https://<адресс к geojson>.json
```
*для проекта использовались Геоданные с https://github.com/devmanorg/where-to-go-places/tree/master/places*
## Админка 
Для входа в админ панел неоходимо создать супер пользователя
```shell
pyhton3 manage.py createsuperuser
```
Входи в админ панел 
`http://localhost:8000/admin/`
![img.png](git_media/img3.png)
![img.png](git_media/admin_panel2.png)

## Рекомендации
### Добавьте переменные среды
Создайте файл `.env` в директории с проектом
```shell
nano .env
```
пропишите туда переменные 

- [ ] `DJANGO_SECRET_KEY` - Это случайный ключ, применяемое для защиты от CSRF
- [ ] `DJANGO_DEBUG` - Режим отладки (`true`или`false`)
- [ ] `DJANGO_ALLOWED_HOSTS` - Список строк, представляющих имена хоста / домена, которые может обслуживать этот сайт Django
прописывать необходимо следующим оброзом
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

_Данные для демонстрации были взяты `https://github.com/devmanorg/where-to-go-frontend/`_  