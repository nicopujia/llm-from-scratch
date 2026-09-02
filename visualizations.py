import pyglet

RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255

window = pyglet.window.Window(512, 512, "Build an LLM (From Scratch)")

WIDTH, HEIGHT = window.get_framebuffer_size()
X_CENTER = WIDTH // 2
Y_CENTER = HEIGHT // 2


circle = pyglet.shapes.Circle(
    x=X_CENTER,
    y=Y_CENTER,
    radius=512,
    color=RED,
)


def main():
    pyglet.app.run()


@window.event
def on_draw():
    window.clear()
    circle.draw()


if __name__ == "__main__":
    main()
