
import pygame
from pygame.locals import *
from sys import exit
import random
import time

class Button(object):
    def __init__(self, text, color, x=None, y=None, **kwargs):
        self.surface = FONT.render(text, True, color)

        self.WIDTH = self.surface.get_width()
        self.HEIGHT = self.surface.get_height()

        if 'centered_x' in kwargs and kwargs['centered_x']:
            self.x = SCREEN_WIDTH // 2 - self.WIDTH // 2
        else:
            self.x = x

        if 'centered_y' in kwargs and kwargs['cenntered_y']:
            self.y = SCREEN_HEIGHT // 2 - self.HEIGHT // 2
        else:
            self.y = y

    def display(self):
        screen.blit(self.surface, (self.x, self.y))

    def check_click(self, position):
        x_match = position[0] > self.x and position[0] < self.x + self.WIDTH
        y_match = position[1] > self.y and position[1] < self.y + self.HEIGHT

        if x_match and y_match:
            return True
        else:
            return False


class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                    s = pygame.Surface((500, 500), pygame.SRCALPHA)
                    s.fill((0,0,0))
                    screen.blit(s, (420, 300))
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                    s = pygame.Surface((500, 500), pygame.SRCALPHA)
                    s.fill((0,0,0))
                    screen.blit(s, (420, 300))
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)


def main():
    pos=[10,110,210,310,410,510,610,710,810,910]
    pos3 = [60,260,460,660,860]
    input_box2 = InputBox(420, 300, 140, 32)
    input_boxes = [input_box2]
    change_color = Button('Change color', (255, 0, 0), 350, 350)
    change_num = Button('Change num', (255, 0, 0), 350, 100)
    Submit = Button('Submit', (255, 0, 0), 350, 100)
    Reset = Button('Reset', (255, 0, 0), 350, 100)
    twocolorans = [-1,0,1]
    tencolorans = [0,1,2,3,4,5,6,7,8,9]
    mode_color = 1
    mode_num = 0
    two_answer=[]
    ten_answer = ''
    test = 0
    while True:
        pos2 = [10, 110, 210, 310, 410, 510, 610, 710, 810, 910]
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            for box in input_boxes:
                box.handle_event(event)
        for box in input_boxes:
            box.update()

        for box in input_boxes:
            box.draw(screen)
        # pygame.display.flip()
        mykeyslist = pygame.key.get_pressed()
        s = pygame.Surface((1000, 300), pygame.SRCALPHA)
        s.fill((0, 0, 0))
        screen.blit(s, (0, 0))
        s = pygame.Surface((1000, 500), pygame.SRCALPHA)
        s.fill((0, 0, 0))
        screen.blit(s, (0, 340))
        s = pygame.Surface((1000, 500), pygame.SRCALPHA)
        s.fill((0, 0, 0))
        screen.blit(s, (680, 0))
        s = pygame.Surface((250, 1000), pygame.SRCALPHA)
        s.fill((0, 0, 0))
        screen.blit(s, (0, 0))
        if change_num.check_click(pygame.mouse.get_pos()):
            change_num = Button('Change num', (255, 0, 0), 100, 300)
        else:
            change_num = Button('Change num', (255, 255, 255), 100, 300)
        if change_color.check_click(pygame.mouse.get_pos()):
            change_color = Button('Change color', (255, 0, 0), 100, 350)
        else:
            change_color = Button('Change color', (255, 255, 255), 100, 350)
        if Submit.check_click(pygame.mouse.get_pos()):
            Submit = Button('Submit', (255, 0, 0), 480, 350)
        else:
            Submit = Button('Submit', (255, 255, 255), 480, 350)
        if Reset.check_click(pygame.mouse.get_pos()):
            Reset = Button('Order remake', (255, 0, 0), 100, 400)
        else:
            Reset = Button('Order remake', (255, 255, 255), 100, 400)
        change_color.display()
        change_num.display()
        Submit.display()
        Reset.display()
        x, y = pygame.mouse.get_pos()  # 获取鼠标在窗口中的位置
        if mykeyslist[pygame.K_0] and pygame.mouse.get_pressed()[0]:
            pos[0]=x
        if mykeyslist[pygame.K_1] and pygame.mouse.get_pressed()[0]:
            pos[1]=x
        if mykeyslist[pygame.K_2] and pygame.mouse.get_pressed()[0]:
            pos[2]=x
        if mykeyslist[pygame.K_3] and pygame.mouse.get_pressed()[0]:
            pos[3]=x
        if mykeyslist[pygame.K_4] and pygame.mouse.get_pressed()[0]:
            pos[4]=x
        if mykeyslist[pygame.K_5] and pygame.mouse.get_pressed()[0]:
            pos[5]=x
        if mykeyslist[pygame.K_6] and pygame.mouse.get_pressed()[0]:
            pos[6]=x
        if mykeyslist[pygame.K_7] and pygame.mouse.get_pressed()[0]:
            pos[7]=x
        if mykeyslist[pygame.K_8] and pygame.mouse.get_pressed()[0]:
            pos[8]=x
        if mykeyslist[pygame.K_9] and pygame.mouse.get_pressed()[0]:
            pos[9]=x
        if Reset.check_click(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            pos = pos2
            print(pos2)
        if change_color.check_click(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            if mode_color == 1:
                mode_color = 0
            elif mode_color == 0:
                mode_color = 1
            time.sleep(0.3)
        if change_num.check_click(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            if mode_num == 1:
                mode_num = 0
            elif mode_num == 0:
                mode_num = 1
            time.sleep(0.3)
        if mode_color == 0:
            if mode_num == 1:
                for component in range(10):
                    pygame.draw.rect(screen, colorset_10[component], (pos[component], 10, 90, 200))
                    text = FONT.render(str(component), True, (255, 255, 255))
                    screen.blit(text, (45+pos[component],210))
            if mode_num == 0:
                for component in range(10):
                    pygame.draw.rect(screen, colorset_2[component], (pos[component], 10, 90, 200))
                    if component < 5:
                        text = FONT.render(str(component), True, (255, 255, 255))
                        screen.blit(text, (40+pos3[component],210))
        elif mode_color == 1:
            if mode_num == 0:
                colorset_10.clear()
                colorset_2.clear()
                two_answer.clear()
                for i in range(5):
                    ans = random.sample(twocolorans, 1)
                    a = random.randint(0, 255)
                    b = random.randint(0, 255)
                    c = random.randint(0, 255)
                    if a == min(a, b, c):
                        a2 = (a - i * 8 * ans[0] + 30 * ans[0]) % 255
                        colorss= tuple(([a2, b, c]))
                    if b == min(a, b, c):
                        b2 = (b - i * 8 * ans[0] + 30 * ans[0]) % 255
                        colorss = tuple(([a, b2, c]))
                    if c == min(a, b, c):
                        c2 = (c - i * 8 * ans[0] + 30 * ans[0]) % 255
                        colorss = tuple(([a, b, c2]))
                    colorset_2.append(tuple(([a, b, c])))
                    colorset_2.append(colorss)
                    two_answer.append(ans[0])
                print(two_answer)
                for i in range(10):
                    c2 = (c + 10 * i) % 255
                    color = tuple(([a, b, c2]))
                    colorset_10.append(color)
                for component in range(10):
                    pygame.draw.rect(screen, colorset_2[component], (pos[component], 10, 90, 200))
                    # text = FONT.render(str(component), True, (255, 255, 255))
                    # screen.blit(text, (45+pos[component],210))
            if mode_num == 1:
                colorset_10.clear()
                a = random.randint(0, 255)
                b = random.randint(0, 255)
                c = random.randint(0, 255)
                ans = random.sample(tencolorans, 10)
                sorted_nums = sorted(enumerate(ans), key=lambda x: x[1])
                idx = [i[0] for i in sorted_nums]
                ten_answer = str(idx)
                print(idx)
                for i in range(10):
                    if a == min(a, b, c):
                        a2 = (a + 10 * ans[i])%255
                        colorss= tuple(([a2, b, c]))
                    if b == min(a, b, c):
                        b2 = (b + 10 * ans[i])%255
                        colorss = tuple(([a, b2, c]))
                    if c == min(a, b, c):
                        c2 = (c + 10 * ans[i])%255
                        colorss = tuple(([a, b, c2]))
                    colorset_10.append(colorss)
                for component in range(10):
                    # pos = [int((color[component] / 255) * 639), component * 80 + 40]
                    pygame.draw.rect(screen, colorset_10[component], (pos[component], 10, 90, 200))  # 绘制白色圆点.pos圆心坐标，20为圆半径大小
                    text = FONT.render(str(component), True, (255, 255, 255))
                    screen.blit(text, (45 + pos[component], 210))
            mode_color = 0



        pygame.draw.rect(screen, (255,255,255), (10, 250, 325, 230),2)
        pygame.draw.rect(screen, (255, 255, 255), (345, 250, 325, 230),2)
        pygame.draw.rect(screen, (255, 255, 255), (680, 250, 340, 230),2)
        text = FONT2.render('Function', True, (255, 255, 255))
        screen.blit(text, (15, 255))
        text = FONT2.render('Result', True, (255, 255, 255))
        screen.blit(text, (350, 255))
        text = FONT2.render('Tips', True, (255, 255, 255))
        screen.blit(text, (685, 255))
        text = FONT3.render('Press <Enter> to clear', True, (180, 180, 180))
        screen.blit(text, (380, 380))
        text = FONT3.render('Press <Backspace> to delete', True, (180, 180, 180))
        screen.blit(text, (380, 400))
        text = FONT3.render('Press <Submit> to confirm', True, (180, 180, 180))
        screen.blit(text, (380, 420))
        text = FONT2.render('1. Choose to display five groups of two', True, (180, 180, 180))
        screen.blit(text, (690, 280))
        text = FONT2.render('or one group of ten similar colors.', True, (180, 180, 180))
        screen.blit(text, (690, 300))
        if mode_num == 0:
            text = FONT2.render('2. Brightness comparison of two colors:', True, (180, 180, 180))
            screen.blit(text, (690, 330))
            text = FONT2.render('Enter "1" means left is brighter than right', True, (180, 180, 180))
            screen.blit(text, (690, 350))
            text = FONT2.render('Enter "0" means two colors are same', True, (180, 180, 180))
            screen.blit(text, (690, 370))
            text = FONT2.render('Enter "-1" means right is brighter than left', True, (180, 180, 180))
            screen.blit(text, (690, 390))
            text = FONT2.render('3. Enter five groups of color comparison', True, (180, 180, 180))
            screen.blit(text, (690, 420))
            text = FONT2.render('results in the box, represented by -1, 1, 0', True, (180, 180, 180))
            screen.blit(text, (690, 440))
        if mode_num == 1:
            text = FONT2.render('2. Brightness comparison of ten colors:', True, (180, 180, 180))
            screen.blit(text, (690, 330))
            text = FONT2.render('You can drag any color with the mouse,', True, (180, 180, 180))
            screen.blit(text, (690, 350))
            text = FONT2.render('press and hold the number on keyboard', True, (180, 180, 180))
            screen.blit(text, (690, 370))
            text = FONT2.render('drag the corresponding color to anywhere', True, (180, 180, 180))
            screen.blit(text, (690, 390))
            text = FONT2.render('3. After sorting, enter the number', True, (180, 180, 180))
            screen.blit(text, (690, 420))
            text = FONT2.render('corresponding to the color into the box', True, (180, 180, 180))
            screen.blit(text, (690, 440))
        pygame.display.flip()
        if Submit.check_click(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            f = open('test.txt', 'a')
            if mode_num == 1:
                print("Test " + str(test) + " for ten colors: " + "Real answer:"+str(ten_answer)+"   type answer:"+input_box2.text,file=f)
            if mode_num == 0:
                print("Test " + str(test) + " for two colors: " + "Real answer:"+str(two_answer)+"   type answer:"+input_box2.text,file=f)
            test = test + 1
            time.sleep(0.3)
            text = FONT.render('Success!', True, (255, 0, 0))
            screen.blit(text, (480, 270))
            pygame.display.flip()
            time.sleep(0.5)
        pygame.display.update()  # 不断刷新画面


if __name__ == "__main__":
    # 设置非全屏模式下窗口分辨率
    global RESULT
    SCREEN_WIDTH = 1030
    SCREEN_HEIGHT = 510
    pygame.init()
    FONT = pygame.font.Font(None, 32)
    FONT2 = pygame.font.Font(None, 24)
    FONT3 = pygame.font.Font(None, 28)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    colorset_10 = []
    colorset_2 = []
    COLOR_INACTIVE = pygame.Color('lightskyblue3')
    COLOR_ACTIVE = pygame.Color('dodgerblue2')
    a = random.randint(0, 255)
    b = random.randint(0, 255)
    c = random.randint(0, 255)
    for i in range(10):
        c2 = (c + 10*i) % 255
        color = tuple(([a, b, c2]))
        colorset_10.append(color)
    for i in range(5):
        a = random.randint(0, 255)
        b = random.randint(0, 255)
        c = random.randint(0, 255)
        a2 = a
        b2=b
        c2=c
        if a == min(a, b, c):
            a2 = a + i * 5
        elif b == min(a, b, c):
            b2 = b + i * 5
        elif c == min(a, b, c):
            c2 = c + i * 5
        colorset_2.append(tuple(([a, b, c])))
        colorset_2.append(tuple(([a2, b2, c2])))
    main()


