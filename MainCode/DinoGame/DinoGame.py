from numpy import asarray
from PIL import ImageOps,ImageGrab,Image
import time
import pyautogui
def hit(key):
    pyautogui.press(key)
    return
def isCollide(data):
    #for cactus
    for i in range(190,238):
        for j in range(395,460):
            if data[i,j] < 100:
                hit("up")
                return
    #for birds
    for i in range(170,210):
        for j in range(270,395):
            if data[i,j] < 100:
                hit("down")
                return
if __name__ == "__main__":
    time.sleep(2)
    print("Hey...Dino game is about to start in 3 seconds")
    hit('up')
    while True:
        img = ImageGrab.grab().convert('L')
        inverted_img = ImageOps.invert(img)
        data = img.load()
        isCollide(data)