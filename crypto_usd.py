#
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import requests


# Функция для получения цены криптовалюты
def get_price():
    currency = currency_var.get()

    # Проверяем, выбрана ли валюта
    if currency == "":
        messagebox.showerror("Ошибка", "Пожалуйста, выберите криптовалюту.")
        return

    url = f"https://api.coingecko.com/api/v3/simple/price?ids={currency}&vs_currencies=usd"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки ответа
        data = response.json()
        price = data[currency]['usd']
        result_label.config(text=f"Цена {currency.capitalize()}: ${price:.2f}")
    except requests.exceptions.RequestException:
        messagebox.showerror("Ошибка", "Не удалось получить данные.")
    except KeyError:
        messagebox.showerror("Ошибка", "Некорректный ответ от API.")


# Создание основного окна
root = tk.Tk()
root.title("Курс обмена криптовалюты")
root.geometry("330x200")

# Выбор криптовалюты
currencies = [''] + ['bitcoin', 'ethereum', 'ripple', 'litecoin', 'cardano']  # Пустая строка для отсутствия валюты
currency_var = tk.StringVar()

# Метка для пояснения выбора
label = tk.Label(root, text="Выберите криптовалюту:")
label.pack(pady=10)

# Стандартный комбо-бокс для выбора валют
dropdown = ttk.Combobox(root, textvariable=currency_var, values=currencies, state='readonly')
dropdown.pack(pady=10)

# Кнопка для получения цены
get_price_button = tk.Button(root, text="Получить курс обмена", command=get_price)
get_price_button.pack(pady=10)

# Метка для отображения результата
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Запуск приложения
root.mainloop()

