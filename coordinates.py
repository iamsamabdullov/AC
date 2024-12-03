#This application allows you to get the coordinates of the city that the user enters. It also displays its region, country and currency.
#The application allows you to open a city map in the browser.

from opencage.geocoder import OpenCageGeocode
from tkinter import *
import webbrowser

def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru')
        if results:
            lat = round(results[0]["geometry"]["lat"], 2)
            lon = round(results[0]["geometry"]["lng"], 2)
            country = results[0]['components']['country']
            currency_name = results[0]['annotations']['currency']['name']
            osm_url = f"https://www.openstreetmap.org/?mlat={lat}&mlon={lon}"

            if 'state' in results[0]['components']:
                region = results[0]['components']['state']
                return {"coordinates": f"Широта: {lat}, Долгота: {lon}\n Страна: {country} \n Регион: {region} \n Валюта: {currency_name}",
                        "map_url": osm_url}
            else:
                return {"coordinates": f"Широта: {lat}, Долгота: {lon}\n Страна: {country} \n Валюта: {currency_name}",
                        "map_url": osm_url}

        else:
            return "Город не найден"
    except Exception as e:
        return f"Возникла ошибка {e}"

def show_coordinates(event=None):
    global map_url
    city = entry.get()
    result = get_coordinates(city, key)
    if isinstance(result, dict):
        label.config(text=f"Координаты города {city}:\n {result['coordinates']}")
        map_url = result['map_url']
    else:
        label.config(text=result)

def show_map():
    if map_url:
        webbrowser.open(map_url)

def clear_fields():
    entry.delete(0, END)
    label.config(text="Введите город и нажмите кнопку")
    global map_url
    map_url = ""

key = '***'
map_url = ""

window = Tk()
window.title("Координаты городов")
window.geometry("320x200")

entry = Entry()
entry.pack()
entry.bind("<Return>", show_coordinates)

button_search = Button(text="Поиск координат", command=show_coordinates)
button_search.pack()

label = Label(text="Введите город и нажмите кнопку")
label.pack()

button_map = Button(text="Показать карту", command=show_map)
button_map.pack()

button_clear = Button(text="Очистить", command=clear_fields)
button_clear.pack()

window.mainloop()

