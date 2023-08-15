import pygame

pygame.init()

# Font that is used to render the text
font20 = pygame.font.Font('freesansbold.ttf', 20)

# RGB values of standard colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Basic parameters of the screen
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()
FPS = 30

game_state = "Start"

# Striker class
class Striker:
    def __init__(self, posx, posy, width, height, speed, color):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.geekRect = pygame.Rect(posx, posy, width, height)

    def display(self):
        pygame.draw.rect(screen, self.color, self.geekRect)

    def update(self, yFac):
        self.posy += self.speed * yFac

        # Restricting the striker to be within the screen bounds
        if self.posy <= 0:
            self.posy = 0
        elif self.posy + self.height >= HEIGHT:
            self.posy = HEIGHT - self.height

        # Updating the rect with the new values
        self.geekRect = pygame.Rect(self.posx, self.posy, self.width, self.height)
    def displayScore(self, text, score, x, y, color):
        text = font20.render(text+str(score), True, color)
        textRect = text.get_rect()
        textRect.center = (x, y)
        screen.blit(text, textRect)
 

    def getRect(self):
        return self.geekRect

# Ball class
class Ball:
    def __init__(self, posx, posy, radius, speed, color):
        self.posx = posx
        self.posy = posy
        self.radius = radius
        self.speed = speed
        self.color = color
        self.xFac = 1
        self.yFac = -1
        self.ball = pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)
        self.firstTime = True

    def display(self):
        pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)

    def update(self):
        self.posx += self.speed * self.xFac
        self.posy += self.speed * self.yFac

        # If the ball hits the top or bottom surfaces, reverse the yFac
        if self.posy <= 0 or self.posy >= HEIGHT:
            self.yFac *= -1

        if self.posx <= 0 and self.firstTime:
            self.firstTime = False
            return 1
        elif self.posx >= WIDTH and self.firstTime:
            self.firstTime = False
            return -1
        else:
            return 0

    def reset(self):
        self.posx = WIDTH // 2
        self.posy = HEIGHT // 2
        self.xFac *= -1
        self.firstTime = True

    def hit(self):
        self.xFac *= -1

    def getRect(self):
        return pygame.Rect(self.posx - self.radius, self.posy - self.radius, 2 * self.radius, 2 * self.radius)

def draw_start_menu():
    screen.fill(BLACK)
    font_1 = pygame.font.Font(None, 50)
    title = font_1.render("Pong-By Rohan", True, (255, 255, 255))
    press= font_1.render("Press Space Bar to Play!", True,(255,255,255))
    start_button = font_1.render('Start', True, (255, 255, 255))
    screen.blit(title, (WIDTH/2 - title.get_width()/2, HEIGHT/2 - title.get_height()/2))
    screen.blit(press, (WIDTH/2 - press.get_width()/2, HEIGHT/2 + press.get_height()/2))
    screen.blit(start_button, (WIDTH/2 - start_button.get_width()/2, HEIGHT/2 +press.get_height() +start_button.get_height()/2))
    pygame.display.update()

def main():
    global game_state
    running = True

    player1 = Striker(20, 0, 10, 100, 10, GREEN)
    player2 = Striker(WIDTH - 30, 0, 10, 100, 10, GREEN)
    ball = Ball(WIDTH // 2, HEIGHT // 2, 7, 7, WHITE)

    listOfPlayers = [player1, player2]

    player1Score, player2Score = 0, 0
    geek1YFac, geek2YFac = 0, 0

    while running:
        if game_state == "Start":
            draw_start_menu()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_state = "Playing"

        elif game_state == "Playing":
            screen.fill(BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        geek2YFac = -1
                    if event.key == pygame.K_DOWN:
                        geek2YFac = 1
                    if event.key == pygame.K_w:
                        geek1YFac = -1
                    if event.key == pygame.K_s:
                        geek1YFac = 1
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        geek2YFac = 0
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        geek1YFac = 0

            # Collision detection
            for geek in listOfPlayers:
                if pygame.Rect.colliderect(ball.getRect(), geek.getRect()):
                    ball.hit()
                    ball.speed+=1 #increases after every collision to make it harder for the players

            # Updating the objects
            player1.update(geek1YFac)
            player2.update(geek2YFac)
            point = ball.update()

            if point == -1:
                player1Score += 1
            elif point == 1:
                player2Score += 1

            if point:
                ball.reset()
                ball.speed=7 #Speed resets after one point

            player1.display()
            player2.display()
            ball.display()

            player1.displayScore("Player_1: ", player1Score, 100, 20, WHITE)
            player2.displayScore("Player_2: ", player2Score, WIDTH - 100, 20, WHITE)

            pygame.display.update()
            clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
