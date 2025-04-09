# Problem Statement

# Implement an 'eraser' on a canvas.
# The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white.

# Solution

from graphics import Canvas
import time

# 🌍 Canvas Setup
CANVAS_W = 400
CANVAS_H = 400

# 🔲 Grid + Eraser
SQUARE_SIZE = 40
ERASER_DIM = 20

def clear_cells(canvas, sweeper):
    "🧼 Clear blocks where sweeper overlaps."
    x = canvas.get_mouse_x()
    y = canvas.get_mouse_y()

    x1 = x
    y1 = y
    x2 = x + ERASER_DIM
    y2 = y + ERASER_DIM

    contacts = canvas.find_overlapping(x1, y1, x2, y2)

    for item in contacts:
        if item != sweeper:
            canvas.set_color(item, 'white')  

def main():
    board = Canvas(CANVAS_W, CANVAS_H)

    for y in range(0, CANVAS_H, SQUARE_SIZE):
        for x in range(0, CANVAS_W, SQUARE_SIZE):
            board.create_rectangle(x, y, x + SQUARE_SIZE, y + SQUARE_SIZE, 'deepskyblue')

    board.create_text(CANVAS_W // 2, 20, "🧽 Click anywhere to drop your eraser!", "black")
    board.wait_for_click()

    start_x, start_y = board.get_last_click()

    # ✏️ Create the eraser
    sweeper = board.create_rectangle(
        start_x,
        start_y,
        start_x + ERASER_DIM,
        start_y + ERASER_DIM,
        'pink'
    )

    # ♻️ Eraser in action!
    while True:
        pointer_x = board.get_mouse_x()
        pointer_y = board.get_mouse_y()
        board.moveto(sweeper, pointer_x, pointer_y)
        clear_cells(board, sweeper)
        time.sleep(0.05)

if __name__ == "__main__":
    main()
