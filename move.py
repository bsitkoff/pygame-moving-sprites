import pgzrun

WIDTH = 800
HEIGHT = 600

# Actor is a sprite — the name matches the image file in images/
player = Actor('happy')
player.pos = (WIDTH // 2, HEIGHT // 2)

alien = Actor('alien')
alien.pos = (100, 100)


def update():
    # Check which keys are held down and move the player
    if keyboard.right:
        player.x += 5

    # TODO: add keyboard.left, keyboard.up, keyboard.down

    # Wrap around the screen edges (disappear one side, appear the other)
    if player.x > WIDTH:
        player.x = 0
    if player.x < 0:
        player.x = WIDTH

    # TODO: add wrapping for the y axis too


def draw():
    screen.fill((0, 0, 0))

    player.draw()
    alien.draw()

    screen.draw.text("Use arrow keys to move", (10, 10), fontsize=24, color="white")


pgzrun.go()
