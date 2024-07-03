import curses
import time
import random


def random_food_placement(max_x, max_y):
    rnd_x = (random.randint(1, max_x - 1) // 2) * 2
    rnd_y = random.randint(1, max_y - 1)

    return rnd_x, rnd_y


def update_snake_body(x, y, snake_body, is_food_eaten=False):
    new_snake_body = [(x, y)]
    new_snake_body.extend(snake_body)
    if not is_food_eaten:
        new_snake_body.pop()

    return new_snake_body


def change_direction(unicode_key, x, y, max_x, max_y):
    if unicode_key == curses.KEY_UP and y > 0:
        y -= 1
    elif unicode_key == curses.KEY_RIGHT and x < max_x - 2:
        x += 2
    elif unicode_key == curses.KEY_DOWN and y < max_y - 1:
        y += 1
    elif unicode_key == curses.KEY_LEFT and x > 1:
        x -= 2

    return x, y


def detect_body_collision(old_snake_body, new_snake_body):
    return len(set(old_snake_body)) != len(set(new_snake_body))


def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    prev_key = None

    max_y, max_x = stdscr.getmaxyx()
    snake_x = ((max_x // 2) // 2) * 2
    snake_y = max_y // 2

    snake_body = [(snake_x, snake_y)]
    food_x, food_y = random_food_placement(max_x, max_y)

    frame_rate = 1 / 6

    while True:
        key = stdscr.getch()

        if key != -1 and chr(key) == "q":
            break

        if prev_key and key == -1:
            key = prev_key

        stdscr.clear()

        stdscr.addstr(food_y, food_x, "*")

        for coor_x, coor_y in snake_body:
            stdscr.addstr(coor_y, coor_x, "s")

        stdscr.refresh()

        snake_x, snake_y = change_direction(key, snake_x, snake_y, max_x, max_y)

        if snake_x == food_x and snake_y == food_y:
            snake_body = update_snake_body(snake_x, snake_y, snake_body, True)
            food_x, food_y = random_food_placement(max_x, max_y)
            frame_rate -= frame_rate * 0.01
        else:
            old_snake_body = snake_body
            snake_body = update_snake_body(snake_x, snake_y, snake_body)
            new_snake_body = snake_body

            if detect_body_collision(old_snake_body, new_snake_body):
                break

        prev_key = key
        time.sleep(frame_rate)


curses.wrapper(main)
