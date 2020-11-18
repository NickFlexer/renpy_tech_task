# Вы можете расположить сценарий своей игры в этом файле.


# Игра начинается здесь:
label start:    
    $ inventory_bag = Inventory()
    $ door = Door()
    
    show screen timelapse with dissolve
    show screen hud
    jump hallway

    return
