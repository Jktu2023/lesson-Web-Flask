# Задание 1
# Создайте новое приложение Flask, которое будет отображать текущие дату и время на главной странице.

# Задание 2
# Создайте новое приложение Flask, создайте структуру проекта с папками static и templates,
# в папке templates должны быть 3 html файла: index, blog, contacts (главная страница, страница блога и контакты).
# Заполните их информацией и выведите силами flask сервера, используя функцию render_template()
# Обязательно на всех страницах сделайте меню, которое будет работать именно при запуске проекта через flask

# Задание 3
# Создайте свой HTML-шаблон (файл base.html).
# Создайте страницы home.html и about.html, которые будут расширять шаблон и заполнять его контентом.

from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__) # переменная app с обьектом класса Flask

@app.route("/")
def index():
    current_time = datetime.now().strftime("%H:%M")  # Получаем текущее время
    return render_template("index.html", time=current_time)  # Передаём время в шаблон
@app.route("/blog")
def blog():
        return render_template("blog.html")
@app.route("/contacts")
def contacts():
        return render_template("contacts.html")


if __name__ == "__main__":
    app.run(debug=True)