import pgzrun
from pgzero.builtins import Actor
from pgzero.builtins import keyboard, sounds
import random
state = 0
WIDTH = 1200
HEIGHT = 750
SIZE_TANK = 25
walls = []
bullets1 = []
bullets_holdoff1 = 0
bullets2 = []
bullets_holdoff2 = 0
enemy_bullets = []
enemy_move_count = 0
game_over = False
enemies = []
bullets_holdofff = 0

# menu button
oneplay = Actor('1player')
oneplay.pos = (WIDTH/2, HEIGHT/2)
oneplay.angle = 0

twoplay = Actor('2player')
twoplay.pos = (WIDTH/2, HEIGHT/2 + 100)
twoplay.angle = 0

exit = Actor('exit')
exit.pos = (WIDTH/2, HEIGHT/2 + 200)
exit.angle = 0


# my team's tank
tank = Actor('tank_blue')
tank.pos = (WIDTH/2-150, HEIGHT-SIZE_TANK)
tank.angle = 90


# my team's tank
tank = Actor('tank_blue')
tank.pos = (WIDTH/2-150, HEIGHT-SIZE_TANK)
tank.angle = 90

# my team2's tank
tank2 = Actor('tank_sand')
tank2.pos = (WIDTH/2-100, HEIGHT-SIZE_TANK)
tank2.angle = 90

# trung
trung = Actor('trung')
trung.pos = (WIDTH/2, HEIGHT-SIZE_TANK)

# enemy's tank
for i in range(6):
    enemy = Actor('tank_red')
    enemy.x = i * 200 + 100
    enemy.y = SIZE_TANK
    enemy.angle = 270
    enemies.append(enemy)

# menu background
mainmenu = Actor('menu')

# set up background and wall
background = Actor('grass')

for x in range(24):
    for y in range(11):
        if random.randint(0, 100) < 50:
            wall = Actor('wall')
            wall.x = x * 50 + SIZE_TANK
            wall.y = y * 50 + SIZE_TANK * 3
            walls.append(wall)

# thành bảo vệ
for x in range(3):
    for y in range(2):
        wall = Actor('wall')
        wall.x = WIDTH/2 + 50 - x * 50
        wall.y = HEIGHT - SIZE_TANK - y * 50
        if wall.pos != trung.pos:
            walls.append(wall)

#tank1
def tank_set():
    original_x = tank.x
    original_y = tank.y
    if keyboard.left:
        tank.x = tank.x - 2
        tank.angle = 180
    elif keyboard.right:
        tank.x = tank.x + 2
        tank.angle = 0
    elif keyboard.up:
        tank.y = tank.y - 2
        tank.angle = 90
    elif keyboard.down:
        tank.y = tank.y + 2
        tank.angle = 270
    if tank.collidelist(walls) != - 1:
        tank.x = original_x
        tank.y = original_y
    if tank.x < SIZE_TANK or tank.x > (WIDTH - SIZE_TANK) or tank.y < SIZE_TANK or tank.y > HEIGHT - SIZE_TANK:
        tank.x = original_x
        tank.y = original_y


def tank_bullets_set():
    global bullets_holdoff1
    if bullets_holdoff1 == 0:
        if keyboard.rshift:
            bullet = Actor('bulletblue2')
            bullet.angle = tank.angle
            if bullet.angle == 0:
                bullet.pos = (tank.x + SIZE_TANK, tank.y)
            if bullet.angle == 180:
                bullet.pos = (tank.x - SIZE_TANK, tank.y)
            if bullet.angle == 90:
                bullet.pos = (tank.x, tank.y - SIZE_TANK)
            if bullet.angle == 270:
                bullet.pos = (tank.x, tank.y + SIZE_TANK)
            bullets1.append(bullet)
            bullets_holdoff1 = 20
    else:
        bullets_holdoff1 = bullets_holdoff1 - 1

    for bullet in bullets1:
        if bullet.angle == 0:
            bullet.x = bullet.x + 5
        if bullet.angle == 180:
            bullet.x = bullet.x - 5
        if bullet.angle == 90:
            bullet.y = bullet.y - 5
        if bullet.angle == 270:
            bullet.y = bullet.y + 5

    for bullet in bullets1:  # destroy walls
        walls_index = bullet.collidelist(walls)
        if walls_index != -1:
            sounds.gun9.play()
            del walls[walls_index]
            bullets1.remove(bullet)
        if bullet.x < 0 or bullet.x > WIDTH or bullet.y < 0 or bullet.y > HEIGHT:
            bullets1.remove(bullet)
        enemy_index = bullet.collidelist(enemies)
        if enemy_index != -1:
            sounds.exp.play()
            bullets1.remove(bullet)
            del enemies[enemy_index]

#tank2
def tank2_set():
    original_x = tank2.x
    original_y = tank2.y
    if keyboard.a:
        tank2.x = tank2.x - 2
        tank2.angle = 180
    elif keyboard.d:
        tank2.x = tank2.x + 2
        tank2.angle = 0
    elif keyboard.w:
        tank2.y = tank2.y - 2
        tank2.angle = 90
    elif keyboard.s:
        tank2.y = tank2.y + 2
        tank2.angle = 270
    if tank2.collidelist(walls) != - 1:
        tank2.x = original_x
        tank2.y = original_y
    if tank2.x < SIZE_TANK or tank2.x > (WIDTH - SIZE_TANK) or tank2.y < SIZE_TANK or tank2.y > HEIGHT - SIZE_TANK:
        tank2.x = original_x
        tank2.y = original_y


def tank2_bullets_set():
    global bullets_holdoff2
    if bullets_holdoff2 == 0:
        if keyboard.g:
            bullet = Actor('bulletsand2')
            bullet.angle = tank2.angle
            if bullet.angle == 0:
                bullet.pos = (tank2.x + SIZE_TANK, tank2.y)
            if bullet.angle == 180:
                bullet.pos = (tank2.x - SIZE_TANK, tank2.y)
            if bullet.angle == 90:
                bullet.pos = (tank2.x, tank2.y - SIZE_TANK)
            if bullet.angle == 270:
                bullet.pos = (tank2.x, tank2.y + SIZE_TANK)
            bullets2.append(bullet)
            bullets_holdoff2 = 20
    else:
        bullets_holdoff2 = bullets_holdoff2 - 1

    for bullet in bullets2:
        if bullet.angle == 0:
            bullet.x = bullet.x + 5
        if bullet.angle == 180:
            bullet.x = bullet.x - 5
        if bullet.angle == 90:
            bullet.y = bullet.y - 5
        if bullet.angle == 270:
            bullet.y = bullet.y + 5

    for bullet in bullets2:  # destroy walls
        walls_index = bullet.collidelist(walls)
        if walls_index != -1:
            sounds.gun9.play()
            del walls[walls_index]
            bullets2.remove(bullet)
        if bullet.x < 0 or bullet.x > WIDTH or bullet.y < 0 or bullet.y > HEIGHT:
            bullets2.remove(bullet)
        enemy_index = bullet.collidelist(enemies)
        if enemy_index != -1:
            sounds.exp.play()
            bullets2.remove(bullet)
            del enemies[enemy_index]


def enemy_set():
    global enemy_move_count, bullets_holdofff

    for enemy in enemies:
        original_x = enemy.x
        original_y = enemy.y
        choice = random.randint(0, 100)
        if enemy_move_count > 0:
            enemy_move_count = enemy_move_count - 1
            if enemy.angle == 0:
                enemy.x = enemy.x + 2
            elif enemy.angle == 180:
                enemy.x = enemy.x - 2
            elif enemy.angle == 90:
                enemy.y = enemy.y - 2
            elif enemy.angle == 270:
                enemy.y = enemy.y + 2
            if enemy.x < SIZE_TANK or enemy.x > (WIDTH-SIZE_TANK) or enemy.y < SIZE_TANK or enemy.y > (HEIGHT-SIZE_TANK):
                enemy.x = original_x
                enemy.y = original_y
                enemy_move_count = 0
            if enemy.collidelist(walls) != -1:
                enemy.x = original_x
                enemy.y = original_y
                enemy_move_count = 0
        if choice < 70:  # enemy's tank move
            enemy_move_count = 30
        elif choice >= 70 and choice <= 72:  # enemy's tank change direction
            enemy.angle = random.randint(0, 3) * 90
        else:  # enemy's tank shoot
            if bullets_holdofff == 0:
                bullet = Actor('bulletred2')
                bullet.angle = enemy.angle
                if bullet.angle == 0:
                    bullet.pos = (enemy.x+SIZE_TANK, enemy.y)
                elif bullet.angle == 180:
                    bullet.pos = (enemy.x-SIZE_TANK, enemy.y)
                elif bullet.angle == 90:
                    bullet.pos = (enemy.x, enemy.y-SIZE_TANK)
                elif bullet.angle == 270:
                    bullet.pos = (enemy.x, enemy.y+SIZE_TANK)
                enemy_bullets.append(bullet)
                bullets_holdofff = 40
            else:
                bullets_holdofff = bullets_holdofff - 1


def enemy_bullets_set():
    global game_over, enemies
    for bullet in enemy_bullets:
        if bullet.angle == 0:
            bullet.x = bullet.x + 5
        if bullet.angle == 180:
            bullet.x = bullet.x - 5
        if bullet.angle == 90:
            bullet.y = bullet.y - 5
        if bullet.angle == 270:
            bullet.y = bullet.y + 5
        # dan dich pha tuong pha xe
        for bullet in enemy_bullets:
            wall_index = bullet.collidelist(walls)
            if wall_index != -1:
                sounds.gun10.play()
                del walls[wall_index]
                enemy_bullets.remove(bullet)
            if bullet.x < 0 or bullet.x > WIDTH or bullet.y < 0 or bullet.y > HEIGHT:
                enemy_bullets.remove(bullet)
            if bullet.colliderect(tank):
                sounds.exp.play()
                game_over = True
                enemies = []
            if bullet.colliderect(tank2):
                sounds.exp.play()
                game_over = True
                enemies = []
            if bullet.colliderect(trung):
                sounds.exp.play()
                game_over = True
                enemies = []


def on_mouse_down(pos):
    global state
    if oneplay.collidepoint(pos):
        state = 1
    elif exit.collidepoint(pos):
        state = 2
    elif twoplay.collidepoint(pos):
        state = 3


def update():
    if state == 1:
        tank_set()
        tank_bullets_set()
        enemy_set()
        enemy_bullets_set()
    elif state == 3:
        tank_set()
        tank_bullets_set()
        enemy_set()
        enemy_bullets_set()
        tank2_set()
        tank2_bullets_set()


def draw():
    if state == 0:
        mainmenu.draw()
        oneplay.draw()
        twoplay.draw()
        exit.draw()
    elif state == 1:
        global game_over
        if game_over:
            screen.fill((0, 0, 0))
            screen.draw.text('YOU LOSE', centerx=WIDTH/2, centery=HEIGHT/2,
                             color=(255, 255, 255), fontsize=100)
            oneplay.draw()
        elif len(enemies) == 0:
            screen.fill((0, 0, 0))
            screen.draw.text('YOU WIN', centerx=WIDTH/2, centery=HEIGHT/2,
                             color=(255, 255, 255), fontsize=100)
        else:
            background.draw()
            tank.draw()
            trung.draw()
            for wall in walls:
                wall.draw()
            for bullet in bullets1:
                bullet.draw()
            for bullet in bullets2:
                bullet.draw()
            for enemy in enemies:
                enemy.draw()
            for bullet in enemy_bullets:
                bullet.draw()
    elif state == 2:
        mainmenu.draw()
        exit.draw()
        quit()
    elif state == 3:
        if game_over:
            screen.fill((0, 0, 0))
            screen.draw.text('YOU LOSE', centerx=WIDTH/2, centery=HEIGHT/2,
                             color=(255, 255, 255), fontsize=100)
        elif len(enemies) == 0:
            screen.fill((0, 0, 0))
            screen.draw.text('YOU WIN', centerx=WIDTH/2, centery=HEIGHT/2,
                             color=(255, 255, 255), fontsize=100)
        else:
            background.draw()
            tank.draw()
            trung.draw()
            tank2.draw()
            for wall in walls:
                wall.draw()
            for bullet in bullets1:
                bullet.draw()
            for bullet in bullets2:
                bullet.draw()
            for enemy in enemies:
                enemy.draw()
            for bullet in enemy_bullets:
                bullet.draw()

pgzrun.go()
