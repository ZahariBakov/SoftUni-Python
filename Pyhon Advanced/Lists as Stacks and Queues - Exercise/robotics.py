from collections import deque


def read_robots():
    result = {}
    robots_input = input().split(";")

    for robot in robots_input:
        name, processing_time = robot.split("-")
        result[name] = int(processing_time)

    return result


def input_products():
    result = deque()

    while True:
        command = input()

        if command == "End":
            break
        else:
            result.append(command)

    return result


def time_in_hours(seconds):
    hours = seconds // (60 * 60)
    seconds %= (60 * 60)
    minutes = seconds // 60
    seconds %= 60

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


robots = read_robots()
available_robots = [y for y in robots.keys()]
processing_robots = {}

starting_time = [int(x) for x in input().split(":")]
time_in_seconds = starting_time[0] * 3600 + starting_time[1] * 60 + starting_time[2]

products = input_products()

while products:
    time_in_seconds = (time_in_seconds + 1) % (24 * 60 * 60)

    for robot_name in [k for k in processing_robots]:
        processing_robots[robot_name] -= 1

        if processing_robots[robot_name] == 0:
            processing_robots.pop(robot_name)

    current_product = products.popleft()

    for robot_name in available_robots:
        if robot_name not in processing_robots:
            print(f"{robot_name} - {current_product} [{time_in_hours(time_in_seconds)}]")
            processing_robots[robot_name] = robots[robot_name]
            break

    else:
        products.append(current_product)
