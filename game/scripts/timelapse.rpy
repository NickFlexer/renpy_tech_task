init python:
    day_part = ["Morning", "Afternoon", "Evening", "Night"]
    current_part = 1


screen timelapse():
        add "images/Интерфейс/Time_%s.png"%(day_part[current_part]):
            xalign 0.5 ypos 0
        
        button:
            xalign 0.5 ypos 0
            xsize 150 ysize 150
            action [
                If(current_part < len(day_part) - 1, SetVariable("current_part", current_part + 1), SetVariable("current_part", 0))
            ]
            text ""
