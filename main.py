import time
import pyautogui
import keyboard

# TODO: Add element's coords calculation based on game size
GAME_SIZE= (2890, 90, 4348, 1110)

# Check if there is a start button on the coordinates and press it
START_BTN_COORDS = (3470, 850)
START_BTN_COLOR = (247, 149, 24)
exists_start_btn = pyautogui.pixelMatchesColor(*START_BTN_COORDS, START_BTN_COLOR)
if not exists_start_btn:
    raise Exception('Start button was not found')
pyautogui.moveTo(*START_BTN_COORDS)
pyautogui.click()


while keyboard.is_pressed('q') == False:
    # Debug. Get coords of mouse pointer and color of pixel
    if keyboard.is_pressed('2'):
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, pyautogui.pixel(x, y))

    # TODO: Fix detection
    # When food is near player, space to get it
    # (78, 226, 0) (68, 170, 0)  (71, 205, 0) (84, 238, 84)  (196, 182, 196)
    if pyautogui.pixel(3377, 760) in { (84, 238, 84), (0, 194, 0), (68, 170, 0), (78, 226, 0), (67, 210, 144), (127, 195, 127), (0, 135, 0) }:
        print('FOOD', pyautogui.pixel(3377, 760))
        pyautogui.press('space')

    # Owl to give food
    if pyautogui.pixelMatchesColor(3377, 760, (249, 92, 25)):
        print('sova')
        pyautogui.press('space')

    # TODO: Better detect
    # Red barrier
    if pyautogui.pixelMatchesColor(3470, 567, (255, 0, 0)):
        print('red barrier')
        pyautogui.keyDown('down')
        time.sleep(1.2)
        pyautogui.keyUp('down')

    # TODO: Better detect
    # Red barrier
    if pyautogui.pixelMatchesColor(3550, 675, (235, 247, 255)):
        print('white barrier')
        pyautogui.keyDown('down')
        time.sleep(1)
        pyautogui.keyUp('down')

    # Yellow barrier
    if pyautogui.pixelMatchesColor(3453, 781, (255, 218, 93)):
        print('yellow barrier')
        pyautogui.press('up')

    # Brown barrier
    if pyautogui.pixelMatchesColor(3450, 775, (153, 153, 153)):
        print('BROWN barrier')
        pyautogui.press('up')

    