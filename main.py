# Задание 1
# Создайте новое приложение Flask, которое будет отображать текущие дату и время на главной странице.

# Задание 2
# Создайте новое приложение Flask, создайте структуру проекта с папками static и templates,
# в папке templates должны быть 3 html файла: index, blog, contacts (главная страница, страница блога и контакты).
# Заполните их информацией и выведите силами flask сервера, используя функцию render_template()
# Обязательно на всех страницах сделайте меню, которое будет работать именно при запуске проекта через flask

from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__) # переменная app с обьектом класса Flask

@app.route("/")
def index():
    current_time = datetime.now().strftime("%H:%M")  # Получаем текущее время
    return render_template("time.html", time=current_time)  # Передаём время в шаблон

if __name__ == "__main__":
    app.run(debug=True)