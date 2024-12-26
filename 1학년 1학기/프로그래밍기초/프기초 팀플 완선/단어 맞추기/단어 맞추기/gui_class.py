import pygame
from functools import cache


@cache
def font(size):
    return pygame.font.Font('./font/NotoSansKR-Medium.otf', size)


def write(surf, txt, font_size, color, pos, criterion='center'):
    text = font(font_size).render(txt, True, color)
    text_pos = text.get_rect()
    setattr(text_pos, criterion, pos)
    surf.blit(text, text_pos)


def reset_icon(side, icon_color, bg_color):
    icon_surf = pygame.Surface((side, side))
    icon_surf.fill(bg_color)

    arrow_head = ((side * 2 // 3, side // 2), (side, side // 2), (side * 5 // 6, side * 13 // 18))
    circle_width = side // 6

    pygame.draw.circle(icon_surf, icon_color, (side // 2, side // 2), side // 3 + circle_width // 2, circle_width)
    pygame.draw.rect(icon_surf, bg_color, (side // 2, side // 2, side // 2, side // 2))
    pygame.draw.polygon(icon_surf, icon_color, arrow_head)

    icon_surf.set_colorkey(bg_color)

    return icon_surf


def txt_icon(side, txt, icon_color, bg_color):
    icon_surf = pygame.Surface((side, side))
    icon_surf.fill(bg_color)

    write(icon_surf, txt, side, icon_color, (side // 2, side // 2))

    icon_surf.set_colorkey(bg_color)

    return icon_surf


class Button():
    size = ()
    pos = ()
    rect:pygame.Rect = None

    txt = ''
    font_size:int = None
    txt_color = ()
    bg_color = ()

    marked = False
    dark = False

    events:list[pygame.event.Event] = []


    # 버튼 중앙에 작성될 텍스트의 내용, 폰트 크기, 폰트 색상을 입력한다
    def init_txt(self, txt, font_size, txt_color):
        self.txt = txt
        self.font_size = font_size
        self.txt_color = txt_color


    def on_cursor(self):
        cursor_pos = pygame.mouse.get_pos()

        return self.rect.collidepoint(cursor_pos)
    

    def is_clicked(self, mouse_button=0):
        for event in Button.events:
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[mouse_button]:
                if self.on_cursor():
                    return True
        return False
    

    def draw(self, surf:pygame.Surface):
        rect = self.rect

        box_surf = pygame.Surface((rect.width, rect.height))
        box_surf.fill(self.bg_color)

        rect_value = (0, 0, rect.width, rect.height)
        radius = rect.width // 7 if rect.width < rect.height else rect.height // 7

        if self.marked:
            pygame.draw.rect(box_surf, self.txt_color, rect_value, border_radius=radius)
            box_surf.set_colorkey((self.bg_color))
            box_surf.set_alpha(64)
            surf.blit(box_surf, (rect.x, rect.y))
        
        if bool(self.txt):
            text = font(rect.height // 2).render(self.txt, True, self.txt_color)
            text_pos = text.get_rect()
            text_pos.center = rect.center
            surf.blit(text, text_pos)

        if self.dark:
            box_surf.fill(self.bg_color)
            box_surf.set_alpha(192)
            surf.blit(box_surf, (rect.x, rect.y))


class AlphabetButton(Button):
    def __init__(self, size:list, center_pos:list, bg_color:list):
        topleft = (center_pos[0] - size[0] / 2, center_pos[1] - size[1] / 2)
        self.rect = pygame.Rect(int(topleft[0]), int(topleft[1]), size[0], size[1])

        self.bg_color = bg_color


    def get_collided_button(self, button:Button):
        return self.rect.colliderect(button.rect)

    
    def follow_cursor(self):
        self.marked = True

        self.rect.center = pygame.mouse.get_pos()


class QuizButton(Button):
    guessing_word = False

    def __init__(self, size, center_pos, is_covered:bool, txt_highlight_color:list, bg_color):
        topleft = (center_pos[0] - size[0] / 2, center_pos[1] - size[1] / 2)
        self.rect = pygame.Rect(int(topleft[0]), int(topleft[1]), size[0], size[1])

        self.covered = is_covered
        self.input_txt = '_'

        self.txt_highlight_color = txt_highlight_color
        self.bg_color = bg_color


    def draw(self, surf):
        rect = self.rect
        button_marking_color = self.txt_color
        txt_color = self.txt_color
        txt = self.input_txt if self.covered else self.txt

        if self.covered and QuizButton.guessing_word:
            txt_color = self.txt_highlight_color

        box_surf = pygame.Surface((rect.width, rect.height))
        box_surf.fill(self.bg_color)

        rect_value = (0, 0, rect.width, rect.height)
        radius = rect.width // 7 if rect.width < rect.height else rect.height // 7

        if self.marked:
            pygame.draw.rect(box_surf, button_marking_color, rect_value, border_radius=radius)
            box_surf.set_alpha(64)
            surf.blit(box_surf, (rect.x, rect.y))
        
        text = font(rect.height // 2).render(txt, True, txt_color)
        text_pos = text.get_rect()
        text_pos.center = rect.center
        surf.blit(text, text_pos)


class FuncButton():
    events:list[pygame.event.Event] = []

    def __init__(self, icon, radius, center_pos, icon_color, bg_color):
        self.icon = icon

        self.radius = radius
        self.pos = center_pos

        self.selected = False

        self.icon_color = icon_color
        self.bg_color = bg_color


    def on_cursor(self):
        cursor_pos = pygame.mouse.get_pos()
        distance = ((self.pos[0] - cursor_pos[0]) ** 2 + (self.pos[1] - cursor_pos[1]) ** 2) ** 0.5

        return distance <= self.radius


    def is_clicked(self, mouse_button=0):
        for event in FuncButton.events:
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[mouse_button]:
                if self.on_cursor():
                    return True
        return False


    def draw(self, surf:pygame.Surface):
        topleft = (self.pos[0] - self.radius, self.pos[1] - self.radius)

        if not self.selected and self.on_cursor():
            circle_surf = pygame.Surface((self.radius * 2, self.radius * 2))
            circle_surf.fill(self.bg_color)
            pygame.draw.circle(circle_surf, self.icon_color, (self.radius, self.radius), self.radius)
            circle_surf.set_colorkey(self.bg_color)
            circle_surf.set_alpha(64)

            surf.blit(circle_surf, topleft)
        elif self.selected:
            pygame.draw.circle(surf, self.icon_color, self.pos, self.radius)

        surf.blit(self.icon, (topleft[0] + self.radius // 4, topleft[1] + self.radius // 4))