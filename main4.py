import tkinter as tk
import random
import string

def generate_password():
    # Получение значений чекбоксов
    include_lowercase = lowercase_var.get()
    include_digits = digits_var.get()
    include_special_chars = special_var.get()

    characters = ""
    # Формирование строки допустимых символов в зависимости от выбранных опций
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += "!@$%^&*()"

    # Проверка на наличие выбранных символов
    if not characters:
        password_label.config(text="Выберите хотя бы один параметр!")
        return

    # Генерация пароля длиной 12 символов
    password = ''.join(random.choice(characters) for _ in range(12))
    password_label.config(text=f"Сгенерированный пароль: {password}")

def copy_to_clipboard():
    password = password_label.cget("text").replace("Сгенерированный пароль: ", "")
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        password_label.config(text="Пароль скопирован, используй!")

# Основное окно
root = tk.Tk()
root.title("Генератор надёжных паролей")

# Установка темной темы
root.configure(bg='black')

# Переменные для хранения состояния чекбоксов
lowercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
special_var = tk.BooleanVar()

# Создание интерфейса
label = tk.Label(root, text="Выберите параметры для генерации пароля:", bg='black', fg='green')
label.pack()

lowercase_check = tk.Checkbutton(root, text="Включить [a-z]", variable=lowercase_var, bg='black', fg='green', selectcolor='black')
lowercase_check.pack()

digits_check = tk.Checkbutton(root, text="Включить [0-9]", variable=digits_var, bg='black', fg='green', selectcolor='black')
digits_check.pack()

special_check = tk.Checkbutton(root, text="Включить специальные символы [!@#$%^&*]", variable=special_var, bg='black', fg='green', selectcolor='black')
special_check.pack()

generate_button = tk.Button(root, text="Генерировать пароль", command=generate_password, bg='black', fg='green')
generate_button.pack()

password_label = tk.Label(root, text="", bg='black', fg='green')
password_label.pack()

copy_button = tk.Button(root, text="Копировать пароль", command=copy_to_clipboard, bg='black', fg='green')
copy_button.pack()

# Запуск главного цикла приложения
root.mainloop()