import curses
import time


def move_snake(unicode_key, x, y):
    if unicode_key == curses.KEY_UP:
        y -= 1
    if unicode_key == curses.KEY_RIGHT:
        x += 2
    if unicode_key == curses.KEY_DOWN:
        y += 1
    if unicode_key == curses.KEY_LEFT:
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
        x, y = move_snake(key, x, y)
        stdscr.refresh()

        time.sleep(0.001)
        prev_key = key


curses.wrapper(main)
