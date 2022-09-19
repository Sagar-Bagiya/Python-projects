from pynput.mouse import Button, Controller
import keyboard
import time
mouse = Controller()
while True:
    x = mouse.position
    time.sleep(1)
    print(x)

# time.sleep(2)
# mouse.position = (1130, 700)
# (1230, 613)
# (1251, 613)
# mouse.position = (1246, 693)
# mouse.click(Button.left, 1)
# mouse.position = (1230, 613)
# mouse.click(Button.left, 1)