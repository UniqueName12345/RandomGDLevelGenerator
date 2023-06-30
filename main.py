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

def search_current_processes_for_info_of_name(process_name):
    for proc in psutil.process_iter():
        try:
            if proc.name() == process_name:
                return proc
        except psutil.NoSuchProcess:
            pass

if __name__ == '__main__':
    # search the currently running desktop apps for the PID of "GeometryDash.exe"
    pid = search_current_processes_for_info_of_name("GeometryDash.exe").pid
    duration = int(input("Enter the duration in milliseconds: "))

    move_mouse(pid, duration)
