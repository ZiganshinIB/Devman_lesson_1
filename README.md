# Проект "Яндекс.Афиша"
Пример проекта можно увидеть по следующей [ссылке](https://ziganshinib.pythonanywhere.com/)
![img.png](git_media/img.png)
![img.png](git_media/img2.png)
## Как запустить проект 
1. Необходимо Скачать проект  
```shell
git clone https://github.com/ZiganshinIB/Devman_lesson_1
```
2. Необходимо установить зависимости
```shell
pip install -r Devman_lesson_1/requirements.txt
```
3. Необходимо мигрировать 
```shell
python3 manage.py migrate
```
* Соберите все статик файлы
```shell
python3 manage.py collectstatic
```
* Запустите проект
```shell
python3 manage.py runserver
```
## Админка 
Для входа в админ панел неоходимо создать супер пользователя
```shell
pyhton3 manage.py createsuperuser
```
Входи в админ панел 
`http://localhost:8000/admin/`
![img.png](git_media/img3.png)
![img.png](git_media/admin_panel2.png)

_Данные для демонстрации были взяты `https://github.com/devmanorg/where-to-go-frontend/`_  