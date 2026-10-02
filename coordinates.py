import time
import pyautogui

print("Наведи курсор на нужное место. Для остановки нажми Ctrl+C.")

try:
    while True:
        x, y = pyautogui.position()
        print(f"\rКоординаты: x={x}, y={y}   ", end="", flush=True)
        time.sleep(0.2)
except KeyboardInterrupt:
    print("\nОстановлено.")