import curses
import time


def main(stdscr):
    max_y, max_x = stdscr.getmaxyx()
    x = 0

    while True:
        key = stdscr.getch()
        if key != -1 and chr(key) == "q":
            break

        stdscr.clear()
        stdscr.addstr(max_y // 2, x, "s")
        stdscr.refresh()

        x += 1
        if x == max_x - 1:
            x = 0


curses.wrapper(main)
