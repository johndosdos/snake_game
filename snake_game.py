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
    max_y, max_x = stdscr.getmaxyx()
    x = 0

    while True:
        key = stdscr.getch()
        if key != -1 and chr(key) == "q":
            break

        stdscr.clear()
        stdscr.addstr(max_y // 2, x, "s")
        x, y = move_snake(key, x, y)
        stdscr.refresh()

        x += 1
        if x == max_x - 1:
            x = 0


curses.wrapper(main)
