import curses
import time


def move_snake(unicode_key, x, y, max_x, max_y):
    if unicode_key == curses.KEY_UP and y > 0:
        y -= 1
    if unicode_key == curses.KEY_RIGHT and x < max_x - 2:
        x += 2
    if unicode_key == curses.KEY_DOWN and y < max_y - 1:
        y += 1
    if unicode_key == curses.KEY_LEFT and x > 0:
        x -= 2

    return x, y


def main(stdscr):
    stdscr.nodelay(True)
    max_y, max_x = stdscr.getmaxyx()
    x = max_x // 2
    y = max_y // 2

    prev_key = None

    while True:
        key = stdscr.getch()

        if key != -1 and chr(key) == "q":
            break

        if prev_key and key == -1:
            key = prev_key

        stdscr.clear()
        stdscr.addstr(y, x, "s")
        x, y = move_snake(key, x, y, max_x, max_y)
        stdscr.refresh()

        prev_key = key

        time.sleep(0.09)


curses.wrapper(main)
