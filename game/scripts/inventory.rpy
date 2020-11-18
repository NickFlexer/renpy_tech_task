init python:
    class InventoryItem:
        def __init__(self, name, img_path):
            self.name = name
            self.img_path = img_path

        def get_img_path(self):
            return self.img_path

        def get_name(self):
            return self.name


    class Inventory:
        def __init__(self):
            self.item_list = []

        def add_item(self, item):
            self.item_list.append(item)

        def get_first_item(self):
            return self.item_list[0]

        def has_items(self):
            return len(self.item_list) > 0


screen inventory():
    modal True

    add "images/Интерфейс/Inventory.png"
    add "images/Интерфейс/Grid.png":
        xalign 0.4 yalign 0.4

    if inventory_bag.has_items():
        imagebutton:
            idle inventory_bag.get_first_item().get_img_path()
            xpos 90 ypos 140
            action [Show("inventory_item_manipulation")]

    button:
        xalign 0.9 yalign 0.9
        action [
            [Hide("inventory"), Hide("inventory_item_manipulation")]
        ]
        text "Закрыть"


screen inventory_item_manipulation():
    imagebutton:
        idle "images/Интерфейс/Button_Yes.png"
        xpos 90 ypos 200
        action [
            Cursor(inventory_bag.get_first_item().get_img_path()), 
            SetVariable("master_key_active", True),
            Hide("inventory"), 
            Hide("inventory_item_manipulation")
        ]

    imagebutton:
        idle "images/Интерфейс/Button_No.png"
        xpos 145 ypos 200
        action [Notify("Выбросить предмет - не реализовано!")]
