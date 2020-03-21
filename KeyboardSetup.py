import cv2
import numpy as np
import dlib

#Variables of Text and Keyboard settings
text = ""
keyboard_selected = "left"
last_keyboard_selected = "left"
select_keyboard_menu = True
keyboard_selection_frames = 0

#from math import hypot

board = np.zeros((1600, 2400), np.uint8)
board[:] = 255

#import dlib face shape

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Keyboard settings
keyboard = np.zeros((1200, 2400, 3), np.uint8)

#KeySet Dictonary Small Letter
keys_set_1 = {0: "@", 1: "q", 2: "w", 3: "e", 4: "r",5: "t", 6: "y", 7: "u", 8: "i", 9: "o", 10: "p", 11: ".", 
              12: "+", 13: "a", 14: "s", 15: "d", 16: "f", 17: "g", 18: "h", 19: "j", 20: "k", 21:"l", 22: "(", 23: ")",
              24: "*", 25: ",", 26: "z", 27: "x", 28: "c", 29: "v", 30: "b", 31: "n", 32: "m", 33: "_", 34: "?", 35: "-",
              36: "!", 37: "0", 38: "1", 39: "2", 40: "3", 41: "4", 42: "5", 43: "6", 44: "7", 45: "8", 46: "9", 47: "=",
              48: "spk", 49: "src", 50: "CALL", 51: "MAIL", 52:"SE", 53:"ban",
              54: "sve", 55: "tube", 56: "FB", 57: "IEEE", 58:"RU", 59:"<"
              }
#KeySet Dictonary Block Letter
keys_set_2 = {0: "@", 1: "Q", 2: "W", 3: "E", 4: "R",5: "T", 6: "Y", 7: "U", 8: "I", 9: "O", 10: "P", 11: ".", 
              12: "+", 13: "A", 14: "S", 15: "D", 16: "F", 17: "G", 18: "H", 19: "J", 20: "K", 21:"L", 22: "(", 23: ")",
              24: "*", 25: ",", 26: "Z", 27: "X", 28: "C", 29: "V", 30: "B", 31: "N", 32: "M", 33: "_", 34: "?", 35: "-",
              36: "!", 37: "0", 38: "1", 39: "2", 40: "3", 41: "4", 42: "5", 43: "6", 44: "7", 45: "8", 46: "9", 47: "=",
              48: "spk", 49: "src", 50: "CALL", 51: "MAIL", 52:"SE", 53:"ban",
              54: "sve", 55: "tube", 56: "FB", 57: "IEEE", 58:"RU", 59:"<"}

def draw_letters(letter_index, text, letter_light):
    # Keys
    if letter_index == 0:
        x = 0
        y = 0
    elif letter_index == 1:
        x = 200
        y = 0
    elif letter_index == 2:
        x = 400
        y = 0
    elif letter_index == 3:
        x = 600
        y = 0
    elif letter_index == 4:
        x = 800
        y = 0
    elif letter_index == 5:
        x = 1000
        y = 0
    elif letter_index == 6:
        x = 1200
        y = 0
    elif letter_index == 7:
        x = 1400
        y = 0
    elif letter_index == 8:
        x = 1600
        y = 0
    elif letter_index == 9:
        x = 1800
        y = 0
    elif letter_index == 10:
        x = 2000
        y = 0
    elif letter_index == 11:
        x = 2200
        y = 0
    elif letter_index == 12:
        x = 0
        y = 200
    elif letter_index == 13:
        x = 200
        y = 200
    elif letter_index == 14:
        x = 400
        y = 200
    elif letter_index == 15:
        x = 600
        y = 200
    elif letter_index == 16:
        x = 800
        y = 200
    elif letter_index == 17:
        x = 1000
        y = 200
    elif letter_index == 18:
        x = 1200
        y = 200
    elif letter_index == 19:
        x = 1400
        y = 200
    elif letter_index == 20:
        x = 1600
        y = 200
    elif letter_index == 21:
        x = 1800
        y = 200
    elif letter_index == 22:
        x = 2000
        y = 200
    elif letter_index == 23:
        x = 2200
        y = 200
    elif letter_index == 24:
        x = 0
        y = 400
    elif letter_index == 25:
        x = 200
        y = 400
    elif letter_index == 26:
        x = 400
        y = 400
    elif letter_index == 27:
        x = 600
        y = 400
    elif letter_index == 28:
        x = 800
        y = 400
    elif letter_index == 29:
        x = 1000
        y = 400
    elif letter_index == 30:
        x = 1200
        y = 400
    elif letter_index == 31:
        x = 1400
        y = 400
    elif letter_index == 32:
        x = 1600
        y = 400
    elif letter_index == 33:
        x = 1800
        y = 400
    elif letter_index == 34:
        x = 2000
        y = 400
    elif letter_index == 35:
        x = 2200
        y = 400
    elif letter_index == 36:
        x = 0
        y = 600
    elif letter_index == 37:
        x = 200
        y = 600
    elif letter_index == 38:
        x = 400
        y = 600
    elif letter_index == 39:
        x = 600
        y = 600
    elif letter_index == 40:
        x = 800
        y = 600
    elif letter_index == 41:
        x = 1000
        y = 600
    elif letter_index == 42:
        x = 1200
        y = 600
    elif letter_index == 43:
        x = 1400
        y = 600
    elif letter_index == 44:
        x = 1600
        y = 600
    elif letter_index == 45:
        x = 1800
        y = 600
    elif letter_index == 46:
        x = 2000
        y = 600
    elif letter_index == 47:
        x = 2200
        y = 600
    elif letter_index == 48:
        x = 0
        y = 800
    elif letter_index == 49:
        x = 400
        y = 800
    elif letter_index == 50:
        x = 800
        y = 800
    elif letter_index == 51:
        x = 1200
        y = 800
    elif letter_index == 52:
        x = 1600
        y = 800
    elif letter_index == 53:
        x = 2000
        y = 800
    elif letter_index == 54:
        x = 0
        y = 1000
    elif letter_index == 55:
        x = 400
        y = 1000
    elif letter_index == 56:
        x = 800
        y = 1000
    elif letter_index == 57:
        x = 1200
        y = 1000
    elif letter_index == 58:
        x = 1600
        y = 1000
    elif letter_index == 59:
        x = 2000
        y = 1000
 
    width = 200
    height = 200
    th = 3 # thickness
    # Text settings
    font_letter = cv2.FONT_HERSHEY_PLAIN
    font_scale = 10
    font_th = 5
    text_size = cv2.getTextSize(text, font_letter, font_scale, font_th)[0]
    width_text, height_text = text_size[0], text_size[1]
    text_x = int((width - width_text) / 2) + x
    text_y = int((height + height_text) / 2) + y
 
    if letter_light is True:
        cv2.rectangle(keyboard, (x + th, y + th), (x + width - th, y + height - th), (0, 255, 0), -1)
        cv2.putText(keyboard, text, (text_x, text_y), font_letter, font_scale, (51, 51, 51), font_th)
    else:
        cv2.rectangle(keyboard, (x + th, y + th), (x + width - th, y + height - th), (51, 51, 51), -1)
        cv2.putText(keyboard, text, (text_x, text_y), font_letter, font_scale, (0, 255, 0), font_th)
        
def draw_menu():
    rows, cols, _ = keyboard.shape
    th_lines = 4 # thickness lines
    font = cv2.FONT_HERSHEY_PLAIN
    cv2.line(keyboard, (int(cols/2) - int(th_lines/2), 0),(int(cols/2) - int(th_lines/2), rows),
             (51, 51, 51), th_lines)
    cv2.putText(keyboard, "LEFT", (200, 600), font, 20, (0, 0, 0), 20)
    cv2.putText(keyboard, "RIGHT", (200 + int(cols/2), 600), font, 20, (0, 0, 0), 20)