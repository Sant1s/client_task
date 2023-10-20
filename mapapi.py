import webbrowser
from tkinter import messagebox

import folium
import database as db

def display_character_movement(character_id):
    points = db.get_character_trajectory_points(character_id)
    if points:
        characters_map = folium.Map(location=[points[0][3], points[0][4]], zoom_start=12)
        for point in points:
            folium.Marker(location=[point[3], point[4]], popup=f"Дата и время: {point[2]}").add_to(
                characters_map)
        characters_map.add_child(
            folium.PolyLine(locations=[[point[3], point[4]] for point in points], color='blue'))
        characters_map.save('character_movement.html')
        webbrowser.open_new_tab("character_movement.html")
    else:
        messagebox.showinfo("Ошибка", f"Нет траектории")
