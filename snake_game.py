import curses
import time
import random


def random_food_placement(max_x, max_y):
    rnd_x = random.randint(0, max_x)
    rnd_y = random.randint(0, max_y)

    return rnd_x, rnd_y




def change_direction(unicode_key, x, y, max_x, max_y):
    if unicode_key == curses.KEY_UP and y > 0:
        y -= 1
    elif unicode_key == curses.KEY_RIGHT and x < max_x:
        x += 2
    elif unicode_key == curses.KEY_DOWN and y < max_y:
        y += 1
    elif unicode_key == curses.KEY_LEFT and x > 1:
        x -= 2

    return x, y


def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    max_y, max_x = stdscr.getmaxyx()
    x = max_x // 2
    y = max_y // 2

    prev_key = None

    food_x, food_y = random_food_placement(max_x, max_y)
    food_is_eaten = False

    while True:
        key = stdscr.getch()

        if key != -1 and chr(key) == "q":
            break

        if prev_key and key == -1:
            key = prev_key

        stdscr.clear()

        if food_is_eaten:
            (
                food_x,
                food_y,
            ) = random_food_placement(max_x, max_y)
        stdscr.addstr(food_y, food_x, "*")

        stdscr.addstr(y, x, "s")
        stdscr.refresh()

        prev_key = key

        time.sleep((1 / 6))

        x, y = change_direction(key, x, y, max_x, max_y)


curses.wrapper(main)
