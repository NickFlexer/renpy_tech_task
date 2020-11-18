init python:
    current_location = None

    def cahange_location(location_name):
        jump_to = location_name

        if location_name == "restroom" and check_restroom_closed(day_part[current_part]):
            if master_key_active:
                jump_to = "lock" 
            else:
                jump_to = "restroom_closed"

        cursor()
        deactivate_master_key()
        renpy.jump(jump_to)

    ChangeLocation = renpy.curry(cahange_location)


image bg hall = "images/Локации/Hall.jpg"


screen hall_buttons:
    textbutton "Коридор":
        text_style "mytextbutton"
        xpos 1150
        ypos 350
        action [Hide("master_key"), Hide("hall_buttons"), ChangeLocation("hallway")]
        

label hall:
    $ current_location = "hall"

    show screen master_key

    scene bg hall:
        zoom 1.12

    "Зал"

    if check_milf_schedule(current_location, day_part[current_part]):
        show screen milfpresent
    else:
        hide screen milfpresent

    call screen hall_buttons


image bg hallway = "images/Локации/Korridor.jpg"


screen hallway_buttons:
    textbutton "Зал":
        text_style "mytextbutton"
        xpos 1200
        ypos 350
        action [Hide("hallway_buttons"), Jump("hall")]

    textbutton "Ванная":
        text_style "mytextbutton"
        xpos 800
        ypos 350
        action [Hide("hallway_buttons"), ChangeLocation("restroom")]

    textbutton "Кухня":
        text_style "mytextbutton"
        xpos 300
        ypos 350
        action [Hide("hallway_buttons"), ChangeLocation("kitchen")]


label hallway:
    $ current_location = "hallway"

    hide screen milfpresent

    scene bg hallway:
        zoom 1.12

    "Коридор"

    call screen hallway_buttons


image bg kitchen = "images/Локации/Kitchen.jpg"


screen kitchen_buttons:
    textbutton "Коридор":
        text_style "mytextbutton"
        xpos 1150
        ypos 350
        action [Hide("hall_buttons"), ChangeLocation("hallway")]


label kitchen:
    $ current_location = "kitchen"

    scene bg kitchen:
        zoom 1.12

    if check_milf_schedule(current_location, day_part[current_part]):
        show screen milfpresent
    else:
        hide screen milfpresent

    "Кухня"

    call screen kitchen_buttons


image bg restroom = "images/Локации/Restroom.jpg"


screen restroom_buttons:
    textbutton "Коридор":
        text_style "mytextbutton"
        xpos 1150
        ypos 350
        action [Hide("hall_buttons"), ChangeLocation("hallway")]


label restroom:
    $ current_location = "restroom"

    scene bg restroom:
        zoom 1.12

    if check_milf_schedule(current_location, day_part[current_part]):
        show screen milfpresent
    else:
        hide screen milfpresent

    "Ванная"

    call screen restroom_buttons
