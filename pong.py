import pygame

pygame.init()
font = pygame.font.SysFont('comicsans', 45, True)
screen_width = 700
screen_height = 500
win = pygame.display.set_mode((screen_width, screen_height))
white = (255, 255, 255)
red = (238, 59, 59)
black = (0, 0, 0)
green = (127, 255, 0)
blue = (0, 255, 255)
clock = pygame.time.Clock()
score1 = 0
score2 = 0
FPS = 30
won = False


class Paddle(object):
    width = 20
    height = 50

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.vel = 7

    def getRect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    def move_up(self):
        if self.y >= (0 + self.vel) and (self.y + self.height) <= screen_height:
            self.y -= self.vel

    def move_down(self):
        if self.y >= 0 and (self.y + self.height + self.vel) <= screen_height:
            self.y += self.vel


class Ball(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.vel = 6
        self.xv = self.vel
        self.yv = self.vel
        self.width = width
        self.height = height

    def getRect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win):
        pygame.draw.rect(win, red, (self.x, self.y, self.width, self.height))

    def move(self):
        global score1
        global score2
        global won
        self.x += self.xv
        self.y += self.yv
        if self.y + self.height > screen_height or self.y < 0:
            self.yv *= -1
        elif self.getRect().colliderect(paddle2.getRect()):
            self.xv *= -1
        elif self.getRect().colliderect(paddle1.getRect()):
            self.xv *= -1
        if not won:
            if self.x < paddle1.x:
                score2 += 1
                won = True
            elif self.x > paddle2.x:
                score1 += 1
                won = True


def retry():
    global won
    if ball.x < paddle1.x:
        ball.x, ball.y = int(screen_width / 2), int(screen_height / 2)
        won = False
    elif ball.x > paddle2.x:
        ball.x, ball.y = int(screen_width / 2), int(screen_height / 2)
        won = False


def redrawWin():
    paddle1.draw(win)
    paddle2.draw(win)
    ball.draw(win)
    score1_text = font.render('P1: ' + str(score1), 1, blue)
    win.blit(score1_text, (260, 30))
    score2_text = font.render('P2: ' + str(score2), 1, green)
    win.blit(score2_text, (360, 30))
    pygame.display.update()


paddle1 = Paddle(0, (screen_height / 2), blue)
paddle2 = Paddle((screen_width - Paddle.width), (screen_height / 2), green)
ball = Ball(int(screen_width / 2), int(screen_height / 2), 15, 15)
run = True

while run:
    win.fill(black)
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1.move_up()
    if keys[pygame.K_s]:
        paddle1.move_down()
    if keys[pygame.K_UP]:
        paddle2.move_up()
    if keys[pygame.K_DOWN]:
        paddle2.move_down()
    ball.move()
    retry()

    redrawWin()
pygame.quit()
