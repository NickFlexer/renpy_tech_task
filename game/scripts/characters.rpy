define milf = Character("MILF", image="images/Персонажи/M1.png")
image  milf usual = "images/Персонажи/M1.png"

define gg = Character("ГГ", image="images/Персонажи/GG1.png")
image  gg usual = "images/Персонажи/GG1.png"


init python:
    def check_milf_schedule(cur_location, day_part):
        if day_part == "Afternoon" and cur_location == "kitchen":
            return True
        elif day_part == "Morning" and cur_location == "restroom":
            return True
        elif day_part == "Evening" and cur_location == "hall":
            return True

        return False


screen milfpresent():
    add "images/Персонажи/M1.png":
        xalign 0.7 ypos 100
        zoom 0.7

    button:
        xalign 0.6 yalign 100
        xsize 200 ysize 800
        action [
            [Call("conversation")]
        ]
        text ""


label conversation:
    show gg usual:
        xalign 0.2 ypos 100
        zoom 0.7

    gg "Привет"
    milf "Рада тебя видеть"
    gg "Хорошего дня"
    milf "И тебе того же"
