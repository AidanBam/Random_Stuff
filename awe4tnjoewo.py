import time
import math
import random
import threading
starting_yaw = -33
pos_yaw = -33
measured_distance, yaw, scanning = [], [], True


def spin():
    print("yep")
    global scanning, starting_yaw
    starting_yaw = -33
    threading.Thread(target = scan).start()
    scanning = True
    time.sleep(1)
    scanning = False
    big_math()


def scan():
    global scanning, measured_distance, yaw, pos_yaw
    while scanning:

        measured_distance.append(random.randint(100,200))
        yaw.append(pos_yaw)
        time.sleep(0.014)
        pos_yaw += 1


def big_math():
    current_angle, biggest_angle, current_length, biggest_length, starting_length, starting_angle = 0, 0, 0, 0, measured_distance[1], yaw[1]
    for i in range(0, len(measured_distance)-1):
        if measured_distance[i] <= 130:
            current_angle, current_length, starting_length, starting_angle = 0, 0, measured_distance[i+1], yaw[i+1]
        else:
            angle = math.radians(abs(abs(starting_angle) - abs(yaw[i+1])))
            current_angle = ((starting_angle + yaw[i+1]) / 2)
            current_length = round(math.sqrt(((starting_length**2) + (measured_distance[i+1]**2)) - (2 * starting_length * measured_distance[i+1] * math.cos(angle))))
        if current_length > biggest_length:
            biggest_length = current_length
            biggest_angle = current_angle
        print(current_length, current_angle, yaw[i+1], starting_angle, starting_length, measured_distance[i+1], angle)
    if biggest_length > 35:
        if biggest_angle > 0:
            print("clockwise", abs(starting_yaw - biggest_angle))
        else:
            print("anticlockwise", abs(starting_yaw - biggest_angle))
    else:
        print("go back")

    print(starting_angle,starting_yaw, biggest_angle, biggest_length)
    print(measured_distance)
    print(yaw)


spin()