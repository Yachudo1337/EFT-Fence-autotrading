import cv2
import numpy as np
import pyautogui
import time

click_delay = 1  # Задержка между кликами в секундах
THRESHOLD = 0.85  # проверка на схожесть изображения, чем выше тем точнее поиск

respirator_img = cv2.imread("images/template/respirator.jpg") 
lomik_png = cv2.imread("images/template/lomik.png")
#raybench = cv2.imread("images/template/raybench.png")
zhiletdikogo = cv2.imread("images/template/zhiletdikogo.png")
#batteryD = cv2.imread("images/template/batteryD.png")
 
def search(): #поиск предметов в магазине
    screenshot = pyautogui.screenshot()
    frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    height, width = frame.shape[:2]
    left_area = frame[0:height, 0:width // 2]

    templates = [
        ("респиратор", respirator_img),
        ("ломик", lomik_png),
       #("raybench", raybench),
        ("жилетдикого", zhiletdikogo),
        #("батарейка", batteryD),
    ]

    for name, template in templates:
        result = cv2.matchTemplate(
            left_area, template, cv2.TM_CCOEFF_NORMED
        )
        _, score, _, location = cv2.minMaxLoc(result)

        if score >= THRESHOLD:
            print(f"Найден {name}: оценка={score:.2f}, позиция={location}")
            buy(location)
            return True

    return False

def magaz():
    pyautogui.click(939, 1059) # Снизу кнопка "Магазин"
    time.sleep(click_delay)
    pyautogui.click(293, 112) # Cкупщик
    time.sleep(2)
    pyautogui.click(320, 252) # Обновить ассортимент
    time.sleep(click_delay)

def listing(): #листание
    pyautogui.click(637, 266) # Позиция чтобы листать вниз
    time.sleep(click_delay)
    for step in range(1, 91):
        pyautogui.scroll(-5)
        time.sleep(0.02)

        if step % 10 == 0:
            search()

def buy(location):
    x, y = location
    pyautogui.click(x + 7, y + 15)
    pyautogui.press("8")
    pyautogui.press("space")

def restartscrolling():
    for _ in range(10):
            pyautogui.click(642, 270)
            time.sleep(0.1)
    time.sleep(3)
    pyautogui.click(957, 567) # Если вылазит ошибка 
    time.sleep(click_delay)
    pyautogui.click(320, 252) # Обновить ассортимент
    time.sleep(click_delay)



magaz()
while True:
    listing()
    restartscrolling()
