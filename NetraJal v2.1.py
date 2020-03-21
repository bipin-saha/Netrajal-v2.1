#Module Importing
import cv2
import webbrowser
import playsound
import DataSection
from KeyboardSetup import *
from ComputerVisionFunctions import *
from SoftwareFunctionality import *

#video capture from Notebook Webcam
cap = cv2.VideoCapture(0)
#MobileCapture.py
 
while True:
    _, frame = cap.read()
    #MobileCapture.py
    rows, cols, _ = frame.shape
    keyboard[:] = (255, 255, 255)
    frames += 1
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
    # Draw a white space for loading bar
    frame[rows - 50: rows, 0: cols] = (255, 255, 255)
 
    if select_keyboard_menu is True:
        draw_menu()
 
    # Keyboard selected
    if keyboard_selected == "left":
        keys_set = keys_set_1
    else:
        keys_set = keys_set_2
    active_letter = keys_set[letter_index]
 
    # Face detection
    faces = detector(gray)
    for face in faces:
        landmarks = predictor(gray, face)
 
        left_eye, right_eye = eyes_contour_points(landmarks)
 
        # Detect blinking
        left_eye_ratio = get_blinking_ratio([36, 37, 38, 39, 40, 41], landmarks)
        right_eye_ratio = get_blinking_ratio([42, 43, 44, 45, 46, 47], landmarks)
        blinking_ratio = (left_eye_ratio + right_eye_ratio) / 2
 
        # Eyes color
        cv2.polylines(frame, [left_eye], True, (0, 0, 255), 2)
        cv2.polylines(frame, [right_eye], True, (0, 0, 255), 2)
 
 
        if select_keyboard_menu is True:
            # Detecting gaze to select Left or Right keybaord
            gaze_ratio_left_eye = get_gaze_ratio([36, 37, 38, 39, 40, 41], landmarks,frame,gray)
            gaze_ratio_right_eye = get_gaze_ratio([42, 43, 44, 45, 46, 47], landmarks,frame,gray)
            gaze_ratio = (gaze_ratio_right_eye + gaze_ratio_left_eye) / 2
 
            if gaze_ratio <= 0.9:
                keyboard_selected = "right"
                keyboard_selection_frames += 1
                # If Kept gaze on one side more than 15 frames, move to keyboard
                if keyboard_selection_frames == 15:
                    select_keyboard_menu = False
                    #RightMenuSoundStatus===>>> OFF
                    frames = 0
                    keyboard_selection_frames = 0
                if keyboard_selected != last_keyboard_selected:
                    last_keyboard_selected = keyboard_selected
                    keyboard_selection_frames = 0
            else:
                keyboard_selected = "left"
                keyboard_selection_frames += 1
                # If Kept gaze on one side more than 15 frames, move to keyboard
                if keyboard_selection_frames == 15:
                    select_keyboard_menu = False
                    #LeftMenuSoundStatus===>>> OFF
                    # Set frames count to 0 when keyboard selected
                    frames = 0
                if keyboard_selected != last_keyboard_selected:
                    last_keyboard_selected = keyboard_selected
                    keyboard_selection_frames = 0
 
        else:
            # Detect the blinking to select the key that is lighting up
            if blinking_ratio > 5:
                # cv2.putText(frame, "BLINKING", (50, 150), font, 4, (255, 0, 0), thickness=3)
                blinking_frames += 1
                frames -= 1
 
                # Show green eyes when closed
                cv2.polylines(frame, [left_eye], True, (0, 255, 0), 2)
                cv2.polylines(frame, [right_eye], True, (0, 255, 0), 2)
 
                # Typing letter
                if blinking_frames == frames_to_blink:
                    if active_letter != "<" and active_letter != "_":
                        text += active_letter
                    if active_letter == "_":
                        text += " "
                    if active_letter == "ban":
                        if "ban" in text:
                            text = text.replace("ban",'')
                        BanglaConverter(text)
                        """ ::::: TEXT OUTPUT IN BANGAL ISSUE ::::: """     
                        
                    if active_letter == "src":
                        if "src" in text:
                            text = text.replace("src",'')
                        webbrowser.open(Url+text,new=new)
                    if active_letter == "MAIL":
                        if "MAIL" in text:
                            text = text.replace("MAIL",'')
                        send_email(subject, text)
                    if active_letter == "SE":
                        if "SE" in text:
                            text = text.replace("SE",'')
                        webbrowser.open(stock_url,new=new)
                    if active_letter == "tube":
                        if "tube" in text:
                            text = text.replace("tube",'')
                        webbrowser.open(youtube_url,new=new)
                    if active_letter == "FB":
                        if "FB" in text:
                            text = text.replace("FB",'')
                        webbrowser.open(facebook_url,new=new)
                    if active_letter == "IEEE":
                        if "IEEE" in text:
                            text = text.replace("IEEE",'')
                        webbrowser.open(ieee_url,new=new)
                    if active_letter == "RU":
                        if "RU" in text:
                            text = text.replace("RU",'')
                        webbrowser.open(ru_url,new=new)
                    if active_letter == "sve":
                        if "sve" in text:
                            text = text.replace("sve",'')
                        GazeOutputText(text)
                    if active_letter == "CALL":
                        if "CALL" in text:
                            text = text.replace("CALL",'')
                        playsound.playsound('Siren.wav', True)
                        
                    if active_letter == "spk":
                        speak = "spk"
                        if speak in text:
                            text = text.replace(speak,'')
                            SpeakLanguage(text)
                    select_keyboard_menu = True
                    # time.sleep(1)
 
            else:
                blinking_frames = 0
 
 
    # Display letters on the keyboard
    if select_keyboard_menu is False:
        if frames == frames_active_letter:
            letter_index += 1
            frames = 0
        if letter_index == 60:
            letter_index = 0
        for i in range(60):
            if i == letter_index:
                light = True
            else:
                light = False
            draw_letters(i, keys_set[i], light)
 
    # Show the text we're writing on the board
    cv2.putText(board, text, (80, 100), font, 9, 0, 3)
 
    # Blinking loading bar
    percentage_blinking = blinking_frames / frames_to_blink
    loading_x = int(cols * percentage_blinking)
    cv2.rectangle(frame, (0, rows - 50), (loading_x, rows), (255, 51, 51), -1)
 
    flipVertical = cv2.flip(frame, 1)
    cv2.imshow("NetraJal : Live View", cv2.resize(flipVertical,(320,240)))
    cv2.imshow("NetraJal : Virtual keyboard", cv2.resize(keyboard,(1000,400)))
    cv2.imshow("NetraJal : Text Board", cv2.resize(board,(600,200)))
 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

# Release handle to the webcam
#video_capture.release()
cv2.destroyAllWindows()
cap.release()