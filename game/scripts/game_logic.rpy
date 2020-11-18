init python:
    master_key_active = False

    def activate_master_key():
        master_key_active = True

    def deactivate_master_key():
        master_key_active = False

    def check_restroom_closed(cur_day_part):
        return cur_day_part == "Morning" and not door.is_open()


    class Door:
        def __init__(self):
            self.closed = True

        def open(self):
            self.closed = False

        def is_open(self):
            return not self.closed


init python:
    def cursor(name = None):
        if name:
            config.mouse = {'default' : [(name, 80, 0)]}
        else:
            config.mouse = None
    
    Cursor = renpy.curry(cursor)


label restroom_closed:
    "Ванная закрыта! нужен ключ"
    jump hallway


screen master_key():
    add "images/Интерфейс/Отмычка_Икон.png":
        xalign 0.3 yalign 0.8
        zoom 0.5
        
    button:
        xalign 0.3 yalign 0.8
        xsize 100 ysize 100
        action [
            [Notify("Ты поднял отмычку!"), Hide("master_key"), inventory_bag.add_item(InventoryItem("masterkey", "images/Интерфейс/Отмычка_Икон.png"))]
        ]
        text ""
