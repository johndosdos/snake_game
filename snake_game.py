import curses
import time


def main(stdscr):
    stdscr.nodelay(True)
    max_y, max_x = stdscr.getmaxyx()
    x = 0

    while True:
        key = stdscr.getch()
        if key != -1 and chr(key) == "q":
            break

        stdscr.clear()
        stdscr.addstr(max_y // 2, x, "s")

        x += 1
        if x == max_x - 1:
            x = 0

        stdscr.refresh()
        time.sleep(0.1)


curses.wrapper(main)
