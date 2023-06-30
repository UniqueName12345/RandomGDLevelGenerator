import pyautogui
import psutil
import random
import time

def move_mouse(pid, duration):
    try:
        process = psutil.Process(pid)
        window = process.window()
        if window is None:
            print("No window found for the specified PID.")
            return

        start_time = time.time()
        end_time = start_time + duration / 1000

        while time.time() < end_time:
            window_rect = window.rect
            x = random.randint(window_rect.left, window_rect.right)
            y = random.randint(window_rect.top, window_rect.bottom)
            pyautogui.moveTo(x, y, duration=0.2)
            pyautogui.click(button='left')

        print("Mouse movement completed.")

    except psutil.NoSuchProcess:
        print("No process found for the specified PID.")

if __name__ == '__main__':
    pid = int(input("Enter the PID: "))
    duration = int(input("Enter the duration in milliseconds: "))

    move_mouse(pid, duration)
