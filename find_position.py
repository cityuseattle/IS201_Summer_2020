import pyautogui

print('press control + C to terminate')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x) + ' Y: ' + str(y)
        print(positionStr, end= '\r')
except KeyboardInterrupt:
    print('\nDone')
