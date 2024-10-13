import cv2
import numpy as np
import pyautogui
import pytesseract
import keyboard
import sys
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

not_found_count = 0
last_not_found_time = 0
last_number1 = None
last_number2 = None
skip_count = 0


def capture_area():
    # region1 = (616, 400, 49, 54)
    # region2 = (717, 398, 50, 50)
    region1 = (628, 309, 30, 43)
    region2 = (723, 310, 30, 44)
    screenshot1 = pyautogui.screenshot(region=region1)
    screenshot2 = pyautogui.screenshot(region=region2)
    return [np.array(screenshot1), np.array(screenshot2)]


def recognize_numbers(images):
    gray1 = cv2.cvtColor(images[0], cv2.COLOR_BGR2GRAY)
    text1 = pytesseract.image_to_string(gray1, config=r'--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789')


    gray2 = cv2.cvtColor(images[1], cv2.COLOR_BGR2GRAY)
    text2 = pytesseract.image_to_string(gray2, config=r'--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789')

    try:
        return [int(text1), int(text2)]
    except:
        return []




def draw_comparison(numbers):
    global not_found_count, last_not_found_time, last_number1, skip_count, last_number2
    first, second = numbers[0], numbers[1]

    if first > second:
        print(f"{first} > {second}")
        pyautogui.press(".")
    elif first < second:
        print(f"{first} < {second}")
        pyautogui.press(",")
    elif first == second:
        print(f"{first} == {second}")
        pyautogui.press("/")


def wait_for_new_question():
    global last_number1, last_number2
    count = 0
    while True:
        images = capture_area()
        numbers = recognize_numbers(images)
        if len(numbers) > 0:
            if numbers[0] != last_number1 or numbers[1] != last_number2:
                count = 0
                last_number1, last_number2 = numbers[0], numbers[1]
                return numbers
            if count >= 3:
                count = 0
                return numbers
            else:
                count += 1


def main():
    keyboard.add_hotkey('=', lambda: sys.exit("进程已结束"))

    try:
        while True:
            numbers = wait_for_new_question()
            draw_comparison(numbers)
    except SystemExit as e:
        print(e)


if __name__ == "__main__":
    main()
