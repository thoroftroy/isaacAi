import time
import random
from multiprocessing import Process
import keyboard
from pynput.keyboard import Key, Controller
#let the keyboard work
keyboard = Controller()
#wait for a few seconds before starting the program
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
#shoot in a randomized direction
def shoot():
    time.sleep(0.001)
    chooseShot = random.randint(1,4)
    if(chooseShot == 1):
        print('Shooting up')
        keyboard.press(Key.up)
        time.sleep(random.uniform(0,1))
        keyboard.release(Key.up)
        shoot()
    elif(chooseShot == 2):
        print('Shooting right')
        keyboard.press(Key.right)
        time.sleep(random.uniform(0,1))
        keyboard.release(Key.right)
        shoot()
    elif(chooseShot == 3):
        print('Shooting down')
        keyboard.press(Key.down)
        time.sleep(random.uniform(0,1))
        keyboard.release(Key.down)
        shoot()
    elif(chooseShot == 4):
        print('Shooting left')
        keyboard.press(Key.left)
        time.sleep(random.uniform(0,1))
        keyboard.release(Key.left)
        shoot()
    else:
        shoot()
#move in a randomized direction
def move():
    time.sleep(0.01)
    chooseDir = random.randint(1,8)
    if(chooseDir == 1):
        print('Moving up')
        keyboard.press('w')
        time.sleep(random.uniform(0,1))
        keyboard.release('w')
        move()
    elif(chooseDir == 2):
        print('Moving up right')
        keyboard.press('w')
        keyboard.press('d')
        time.sleep(random.uniform(0,1))
        keyboard.release('w')
        keyboard.release('d')
        move()
    elif(chooseDir == 3):
        print('Moving right')
        keyboard.press('d')
        time.sleep(random.uniform(0,1))
        keyboard.release('d')
        move()
    elif(chooseDir == 4):
        print('Moving down right')
        keyboard.press('s')
        keyboard.press('d')
        time.sleep(random.uniform(0,1))
        keyboard.release('s')
        keyboard.release('d')
        move()
    elif(chooseDir == 5):
        print('Moving down')
        keyboard.press('s')
        time.sleep(random.uniform(0,1))
        keyboard.release('s')
        move()
    elif(chooseDir == 6):
        print('Moving left')
        keyboard.press('a')
        time.sleep(random.uniform(0,1))
        keyboard.release('a')
        move()
    elif(chooseDir == 7):
        print('Moving down left')
        keyboard.press('a')
        keyboard.press('s')
        time.sleep(random.uniform(0,1))
        keyboard.release('a')
        keyboard.release('s')
        move()
    elif(chooseDir == 8):
        print('Moving up left')
        keyboard.press('a')
        keyboard.press('w')
        time.sleep(random.uniform(0,1))
        keyboard.release('a')
        keyboard.release('w')
        move()
    else:
        move()
#score what isaac does
def score():
    points = 0
    print('Start')
    #if isaac gets hit -1 points
    points -= 1
    #if isaac hits an enemy add one point
    points += 1

#run both shoot and move at the same time
if __name__ =='__main__':
    p1 = Process(target=shoot)
    p1.start()
    p2 = Process(target=move)
    p2.start()
    p3 = Process(target=score)
    p3.start()
