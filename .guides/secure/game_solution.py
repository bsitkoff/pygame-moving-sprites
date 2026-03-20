import pgzrun

WIDTH = 800
HEIGHT = 600

# Actor is a sprite — the name matches the image file in images/
# Students should replace 'star' and 'ufo' with their own sprite names
player = Actor('star')
player.pos = (WIDTH // 2, HEIGHT // 2)

alien = Actor('ufo')
alien.pos = (100, 100)


def update():
    # Check which keys are held down and move the player
    if keyboard.right:
        player.x += 5
    if keyboard.left:
        player.x -= 5
    if keyboard.up:
        player.y -= 5
    if keyboard.down:
        player.y += 5

    # Wrap around the screen edges (disappear one side, appear the other)
    if player.x > WIDTH:
        player.x = 0
    if player.x < 0:
        player.x = WIDTH

    # Wrap around the top and bottom edges
    if player.y > HEIGHT:
        player.y = 0
    if player.y < 0:
        player.y = HEIGHT


def draw():
    screen.fill((0, 0, 0))

    player.draw()
    alien.draw()

    screen.draw.text("Use arrow keys to move", (10, 10), fontsize=24, color="white")


pgzrun.go()