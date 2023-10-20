import webbrowser
import tkinter as tk
from tkinter import messagebox

import folium

import database as db
import mapapi as m

root = tk.Tk()
root.geometry('1000x500')
root.title("Приложение для Властелина Колец")


def add_character_window():
    def add_character_to_db():
        character_name = character_name_entry.get()
        db.add_character(character_name)
        window.destroy()

    window = tk.Toplevel(root)
    window.title("Добавить персонажа")

    character_name_label = tk.Label(window, text="Имя персонажа:")
    character_name_label.pack(pady=10)
    character_name_entry = tk.Entry(window)
    character_name_entry.pack(pady=10)

    submit_button = tk.Button(window, text="Добавить", command=add_character_to_db)
    submit_button.pack(pady=5)


def add_geo_data_window():
    def add_geo_data_to_db():
        character_name = character_name_entry.get()
        measurement_datetime = measurement_datetime_entry.get()
        latitude = latitude_entry.get()
        longitude = longitude_entry.get()

        character_id = db.get_character_id_by_name(character_name)
        if character_id:
            db.add_geo_data(character_id, measurement_datetime, latitude, longitude)
            db.add_trajectory_point(character_id, measurement_datetime, latitude, longitude)
            window.destroy()
        else:
            messagebox.showinfo("Ошибка", f"Персонаж с именем {character_name} не найден.")

    window = tk.Toplevel(root)
    window.title("Добавить гео данные")

    character_name_label = tk.Label(window, text="Имя персонажа:")
    character_name_label.pack(pady=5)
    character_name_entry = tk.Entry(window)
    character_name_entry.pack(pady=5)

    measurement_datetime_label = tk.Label(window, text="Дата и время измерения:")
    measurement_datetime_label.pack(pady=5)
    measurement_datetime_entry = tk.Entry(window)
    measurement_datetime_entry.pack(pady=5)

    latitude_label = tk.Label(window, text="Широта:")
    latitude_label.pack(pady=5)
    latitude_entry = tk.Entry(window)
    latitude_entry.pack(pady=5)

    longitude_label = tk.Label(window, text="Долгота:")
    longitude_label.pack(pady=5)
    longitude_entry = tk.Entry(window)
    longitude_entry.pack(pady=5)

    submit_button = tk.Button(window, text="Добавить", command=add_geo_data_to_db)
    submit_button.pack(pady=5)


def display_characters_window():
    window = tk.Toplevel(root)
    window.title("Список персонажей")

    characters = db.get_all_characters()
    if characters:
        characters_text = '\n'.join([f"Имя: {char[1]}" for char in characters])
        characters_label = tk.Label(window, text=characters_text)
        characters_label.pack(pady=10)


def delete_character(name):
    character_id = db.get_character_id_by_name(name)
    if character_id:
        db.delete_character(character_id)
    else:
        messagebox.showinfo("Ошибка", f"Персонаж с именем {name} не найден.")

def delete_character_window():
    def delete_character_from_db():
        character_name = character_name_entry.get()
        delete_character(character_name)
        window.destroy()

    window = tk.Toplevel(root)
    window.title("Удалить персонажа")

    character_name_label = tk.Label(window, text="Имя персонажа:")
    character_name_label.pack(pady=5)
    character_name_entry = tk.Entry(window)
    character_name_entry.pack(pady=5)

    submit_button = tk.Button(window, text="Удалить", command=delete_character_from_db)
    submit_button.pack(pady=5)


def display_character_movement_window():
    def display_character_movement_on_map():
        character_name = character_name_entry.get()
        character_id = db.get_character_id_by_name(character_name)
        if character_id:
            m.display_character_movement(character_id)
        else:
            messagebox.showinfo("Ошибка", f"Персонажа с именем {character_name} не найден")

    window = tk.Toplevel(root)
    window.title("Отобразить передвижения персонажа")

    character_name_label = tk.Label(window, text="Имя персонажа:")
    character_name_label.pack(pady=5)
    character_name_entry = tk.Entry(window)
    character_name_entry.pack(pady=5)

    submit_button = tk.Button(window, text="Отобразить", command=display_character_movement_on_map)
    submit_button.pack(pady=5)


def display_current_positions_window():
    characters = db.get_all_characters_with_current_position()
    if characters:
        characters_map = folium.Map(location=[characters[0][2], characters[0][3]], zoom_start=5)
        for character in characters:
            folium.Marker(location=[character[2], character[3]], popup=character[1]).add_to(characters_map)
        characters_map.save('current_positions.html')
        webbrowser.open_new_tab("current_positions.html")
    else:
        messagebox.showinfo("Ошибка", "Позиции не найдены")