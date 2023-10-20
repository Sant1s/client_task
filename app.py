import buttons
import database


def start():
    database.start()

    add_character_button = buttons.tk.Button(buttons.root, text="Добавить персонажа",
                                             command=buttons.add_character_window)
    add_character_button.pack(pady=10)

    add_geo_data_button = buttons.tk.Button(buttons.root, text="Добавить гео данные",
                                            command=buttons.add_geo_data_window)
    add_geo_data_button.pack(pady=10)

    get_characters_button = buttons.tk.Button(buttons.root, text="Получить всех персонажей",
                                              command=buttons.display_characters_window)
    get_characters_button.pack(pady=10)

    delete_character_button = buttons.tk.Button(buttons.root, text="Удалить персонажа",
                                                command=buttons.delete_character_window)
    delete_character_button.pack(pady=10)

    display_movement_button = buttons.tk.Button(buttons.root, text="Отобразить передвижения персонажа",
                                                command=buttons.display_character_movement_window)
    display_movement_button.pack(pady=10)

    display_positions_button = buttons.tk.Button(buttons.root, text="Отобразить текущие положения персонажей",
                                                 command=buttons.display_current_positions_window)
    display_positions_button.pack(pady=10)

    buttons.root.mainloop()
