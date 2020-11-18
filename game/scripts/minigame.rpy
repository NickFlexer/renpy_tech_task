init python:

    import pygame

    class MasterKey:
        def __init__(self):
            self.img = Image("images/Мини-игра/Отмычка.png")
            self.x_pos = -1000
            self.y_pos = 300
            self.width = None
            self.height = None
            self.speed = 30

            self.click_state = False

            self.move_forward = True
            self.move_down = True

        def update(self, dt, width, height):
            speed = dt * self.speed

            if self.click_state:
                if self.move_down:
                    self.y_pos += speed * self.speed
                    if self.y_pos > 600:
                        self.move_down = False
                else:
                    self.y_pos -= speed * self.speed
                    if self.y_pos < 300:
                        self.y_pos = 300
                        self.move_down = True
                        self.click_state = False
            else:
                if self.move_forward:
                    self.x_pos += speed * self.speed
                    if self.x_pos + self.width > width:
                        self.move_forward = False
                else:
                    self.x_pos -= speed * self.speed
                    if self.x_pos + self.width < 0:
                        self.move_forward = True

        def click(self):
            self.click_state = True

        def render(self, renderer, width, height, st, at):
            rend = renpy.render(self.img, width, height, st, at)
            renderer.blit(rend, (self.x_pos, self.y_pos))
            self.width, self.height = rend.get_size()

        def det_hook_position(self):
            return self.x_pos + self.width


    class Pin:
        def __init__(self, x_pos, state):
            self.img = Image("images/Мини-игра/Штифт .png")
            self.x_pos = x_pos
            self.y_pos = 500
            self.width = None
            self.height = None
            self.open_state = self.set_state(state)

        def update(self, dt, width, height):
            pass

        def render(self, renderer, width, height, st, at):
            rend = renpy.render(self.img, width, height, st, at)
            renderer.blit(rend, (self.x_pos, self.y_pos))
            self.width, self.height = rend.get_size()

        def set_state(self, state):
            self.open_state = state

            if self.open_state == True:
               self.y_pos = 600    

        def is_hit(self, position):
            return self.x_pos <= position and position <= (self.x_pos + self.width)

        def is_open(self):
            return self.open_state


    class BreakingTheLock(renpy.Displayable):
        def __init__(self, **kwargs):
            super(BreakingTheLock, self).__init__(**kwargs)

            self.lock_bg = Image("images/Мини-игра/Фон_Замка.png")
            self.lock = Image("images/Мини-игра/Замок.png")

            self.master_key = MasterKey()
            self.pin_list = [
                Pin(100, False),
                Pin(220, False),
                Pin(340, False),
                Pin(460, False)
            ]
            cursor()

            self.last_start = None
            self.breaked = False

        def render(self, width, height, st, at):
            delta = self._get_delta(st)

            render = renpy.Render(width, height)

            lock_bg_rend = renpy.render(self.lock_bg, width, height, st, at)
            render.blit(lock_bg_rend, (0, 175))

            self.master_key.render(render, width, height, st, at)
            self.master_key.update(delta, width, height)

            for pin in self.pin_list:
                pin.render(render, width, height, st, at)
                pin.update(delta, width, height)

            lock_rend = renpy.render(self.lock, width, height, st, at)
            render.blit(lock_rend, (-10, -10))

            renpy.redraw(self, 0)

            return render

        def event(self, ev, x, y, st):
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                self.master_key.click()

                self._open_pin(self.master_key.det_hook_position())

                if self._is_lock_open():
                    door.open()
                    renpy.hide_screen("lock_minigame")
                    renpy.notify("Открыто!")
                    cahange_location("restroom")

        def _get_delta(self, st):
            if self.last_start is None:
                self.last_start = st  
                        
            delta = st - self.last_start
            self.last_start = st

            return delta

        def _open_pin(self, hook_position):
            for pin in self.pin_list:
                if pin.is_hit(hook_position):
                    pin.set_state(True)
                    # renpy.notify("Пин!")

        def _is_lock_open(self):
            res = True

            for pin in self.pin_list:
                if not pin.is_open():
                    res = False

            return res



screen lock_minigame():
    modal True
    
    add BreakingTheLock()


label lock:
    "Этот замок нужно открыть!"

    call screen lock_minigame

