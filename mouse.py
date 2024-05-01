# from turtle import ht
# import cv2  # pip install opencv-contrib-python
# import numpy as np
# import mediapipe as mp  # pip install mediapipe
# import pyautogui    # pip install PyautoGUI
# import matplotlib.pyplot as plt
# from IPython.display import Image

# cap = cv2.VideoCapture(0)   # capture video '0' one cam
# hand_detector = mp.solutions.hands.Hands()  # detect hand
# drawing_utils = mp.solutions.drawing_utils
# screen_width, screen_height = pyautogui.size()
# index_y = 0

# '''Smoothen the movement of mouse to stop at the exact position of,
#    our hand movement without any shake in the movement of the mouse'''
# smoothening = 9
# plocx, plocy = 0, 0
# clocx, clocy = 0, 0

# while True:
#     _, frame = cap.read()   # read data from cap
#     '''Flip the frame or screen since the camera shows the mirror image,
#        of our hand and moves in opposite direction so we need to flip the screen'''
#     frame = cv2.flip(frame, 1)
#     # shape gives frame height and width using shape
#     frame_height, frame_width, _ = frame.shape
#     # detect on rgb frame color
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     output = hand_detector.process(rgb_frame)
#     hands = output.multi_hand_landmarks  # hand landmark

#     if hands:
#         for hand in hands:
#             drawing_utils.draw_landmarks(
#                 frame, hand)   # see landmarks on frame
#             # we use our index finger tip move the mouse
#             landmarks = hand.landmark

#             for id, landmark in enumerate(landmarks):   # add counter
#                 # show the landmarks on kernel in x and y axis
#                 # x and y axis is multiplies by the height and width to get the x and y axis on the frames
#                 x = int(landmark.x*frame_width)
#                 y = int(landmark.y*frame_height)
#                 # print(x,y)
#                 # Index finger tip point number is 8
#                 # and draw a boundary to the point a circle

#             landmarks = hand.landmark

#             for id, landmark in enumerate(landmarks):   # add counter
#                 # show the landmarks on kernel in x and y axis
#                 # x and y axis is multiplies by the height and width to get the x and y axis on the frames
#                 x = int(landmark.x*frame_width)
#                 y = int(landmark.y*frame_height)
#                 # print(x,y)
#                 # Index finger tip point number is 8
#                 # and draw a boundary to the point a circle
#                 if id == 8:
#                     cv2.circle(img=frame, center=(x, y),
#                                radius=15, color=(0, 255, 255))
#                     # pyautogui.moveTo(x,y)
#                     index_x = (screen_width/frame_width)*x
#                     index_y = (screen_height/frame_height)*y
#                     # co-ordinates need to be changed
#                     # smoothining varies with the change in the smoothening factor
#                     clocx = plocx + (index_x - plocx) / smoothening
#                     clocy = plocy + (index_y - plocy) / smoothening
#                     pyautogui.moveTo(clocx, clocy)
#                     plocx, plocy = clocx, clocy

#                 # thumb tip point number is 4

#                 if id == 4:
#                     cv2.circle(img=frame, center=(x, y),
#                                radius=15, color=(0, 255, 255))
#                     thumb_x = (screen_width/frame_width)*x
#                     thumb_y = (screen_height/frame_height)*y
#                     print('distance : ', abs(index_y - thumb_y))
#                     if abs(index_y - thumb_y) < 70:
#                         print('click')
#                         pyautogui.click()
#                         pyautogui.sleep(1)
#     cv2.imshow('Virtual Mouse', frame)  # show image
#     cv2.waitKey(1)  # waits for key infinitely
# from turtle import ht
# import cv2
# import numpy as np
# import mediapipe as mp
# import pyautogui
# import matplotlib.pyplot as plt
# from IPython.display import Image

# cap = cv2.VideoCapture(0)
# hand_detector = mp.solutions.hands.Hands()
# drawing_utils = mp.solutions.drawing_utils
# screen_width, screen_height = pyautogui.size()
# index_y = 0

# smoothening = 9
# plocx, plocy = 0, 0
# clocx, clocy = 0, 0

# while True:
#     _, frame = cap.read()
#     frame = cv2.flip(frame, 1)
#     frame_height, frame_width, _ = frame.shape
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     output = hand_detector.process(rgb_frame)
#     hands = output.multi_hand_landmarks

#     if hands:
#         for hand in hands:
#             landmarks = hand.landmark
#             index_x, index_y = 0, 0
#             thumb_x, thumb_y = 0, 0
#             middle_x, middle_y = 0, 0
#             ring_x, ring_y = 0, 0
#             pinky_x, pinky_y = 0, 0

#             for id, landmark in enumerate(landmarks):
#                 x = int(landmark.x * frame_width)
#                 y = int(landmark.y * frame_height)

#                 if id == 8:  # Index finger tip
#                     index_x = (screen_width/frame_width)*x
#                     index_y = (screen_height/frame_height)*y

#                 if id == 4:  # Thumb tip
#                     thumb_x = (screen_width/frame_width)*x
#                     thumb_y = (screen_height/frame_height)*y

#                 if id == 12:  # Middle finger tip
#                     middle_x = (screen_width/frame_width)*x
#                     middle_y = (screen_height/frame_height)*y

#                 if id == 16:  # Ring finger tip
#                     ring_x = (screen_width/frame_width)*x
#                     ring_y = (screen_height/frame_height)*y

#                 if id == 20:  # Pinky finger tip
#                     pinky_x = (screen_width/frame_width)*x
#                     pinky_y = (screen_height/frame_height)*y

#             # Mouse Movement (Index + Thumb)
#             if index_x != 0 and index_y != 0 and thumb_x != 0 and thumb_y != 0:
#                 cv2.circle(img=frame, center=(int(index_x), int(
#                     index_y)), radius=15, color=(0, 255, 255))
#                 cv2.circle(img=frame, center=(int(thumb_x), int(
#                     thumb_y)), radius=15, color=(0, 255, 255))
#                 pyautogui.moveTo((index_x + thumb_x) / 2,
#                                  (index_y + thumb_y) / 2)

#             # Left Click (Middle + Ring)
#             if middle_x != 0 and middle_y != 0 and ring_x != 0 and ring_y != 0:
#                 cv2.circle(img=frame, center=(int(middle_x), int(
#                     middle_y)), radius=15, color=(0, 255, 0))
#                 cv2.circle(img=frame, center=(int(ring_x), int(
#                     ring_y)), radius=15, color=(255, 0, 0))
#                 if abs(middle_y - ring_y) < 70:
#                     pyautogui.click()
#                     pyautogui.sleep(1)

#             # Right Click (Index + Pinky)
#             if index_x != 0 and index_y != 0 and pinky_x != 0 and pinky_y != 0:
#                 cv2.circle(img=frame, center=(int(index_x), int(
#                     index_y)), radius=15, color=(0, 255, 255))
#                 cv2.circle(img=frame, center=(int(pinky_x), int(
#                     pinky_y)), radius=15, color=(255, 255, 0))
#                 if abs(index_y - pinky_y) < 70:
#                     pyautogui.rightClick()
#                     pyautogui.sleep(1)

#             # Drag (Thumb + Pinky)
#             if thumb_x != 0 and thumb_y != 0 and pinky_x != 0 and pinky_y != 0:
#                 if abs(thumb_y - pinky_y) < 70:
#                     pyautogui.dragTo(pinky_x, pinky_y)
#                     pyautogui.sleep(1)

#             # Scroll (Index + Middle)
#             if index_x != 0 and index_y != 0 and middle_x != 0 and middle_y != 0:
#                 if abs(index_y - middle_y) < 70:
#                     pyautogui.scroll(10)  # Scroll up
#                     pyautogui.sleep(0.5)
#                 elif abs(middle_y - index_y) < 70:
#                     pyautogui.scroll(-10)  # Scroll down
#                     pyautogui.sleep(0.5)

#     cv2.imshow('Virtual Mouse', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
# import cv2
# import numpy as np
# import mediapipe as mp
# import pyautogui

# cap = cv2.VideoCapture(0)
# hand_detector = mp.solutions.hands.Hands()
# drawing_utils = mp.solutions.drawing_utils
# screen_width, screen_height = pyautogui.size()

# while True:
#     _, frame = cap.read()
#     frame = cv2.flip(frame, 1)
#     frame_height, frame_width, _ = frame.shape
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     output = hand_detector.process(rgb_frame)
#     hands = output.multi_hand_landmarks

#     if hands:
#         for hand in hands:
#             landmarks = hand.landmark
#             index_x, index_y = 0, 0
#             thumb_x, thumb_y = 0, 0
#             middle_x, middle_y = 0, 0
#             ring_x, ring_y = 0, 0
#             pinky_x, pinky_y = 0, 0

#             for id, landmark in enumerate(landmarks):
#                 x = int(landmark.x * frame_width)
#                 y = int(landmark.y * frame_height)

#                 if id == 8:  # Index finger tip
#                     index_x = (screen_width / frame_width) * x
#                     index_y = (screen_height / frame_height) * y

#                 if id == 4:  # Thumb tip
#                     thumb_x = (screen_width / frame_width) * x
#                     thumb_y = (screen_height / frame_height) * y

#                 if id == 12:  # Middle finger tip
#                     middle_x = (screen_width / frame_width) * x
#                     middle_y = (screen_height / frame_height) * y

#                 if id == 16:  # Ring finger tip
#                     ring_x = (screen_width / frame_width) * x
#                     ring_y = (screen_height / frame_height) * y

#                 if id == 20:  # Pinky finger tip
#                     pinky_x = (screen_width / frame_width) * x
#                     pinky_y = (screen_height / frame_height) * y

#             # Drag (Thumb + Pinky)
#             if thumb_x != 0 and thumb_y != 0 and pinky_x != 0 and pinky_y != 0:
#                 if abs(thumb_y - pinky_y) < 70:
#                     pyautogui.dragTo(pinky_x, pinky_y, button='left')
#                     pyautogui.sleep(1)

#     cv2.imshow('Virtual Mouse', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
# import cv2
# import numpy as np
# import mediapipe as mp
# import pyautogui

# cap = cv2.VideoCapture(0)
# hand_detector = mp.solutions.hands.Hands()
# screen_width, screen_height = pyautogui.size()

# while True:
#     _, frame = cap.read()
#     frame = cv2.flip(frame, 1)
#     frame_height, frame_width, _ = frame.shape
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     output = hand_detector.process(rgb_frame)
#     hands = output.multi_hand_landmarks

#     if hands:
#         for hand in hands:
#             landmarks = hand.landmark
#             index_x, index_y = 0, 0
#             thumb_x, thumb_y = 0, 0
#             pinky_x, pinky_y = 0, 0

#             for id, landmark in enumerate(landmarks):
#                 x = int(landmark.x * frame_width)
#                 y = int(landmark.y * frame_height)

#                 if id == 8:  # Index finger tip
#                     index_x = (screen_width / frame_width) * x
#                     index_y = (screen_height / frame_height) * y

#                 if id == 4:  # Thumb tip
#                     thumb_x = (screen_width / frame_width) * x
#                     thumb_y = (screen_height / frame_height) * y

#                 if id == 20:  # Pinky finger tip
#                     pinky_x = (screen_width / frame_width) * x
#                     pinky_y = (screen_height / frame_height) * y

#             # Drag (Thumb + Pinky)
#             if thumb_x != 0 and thumb_y != 0 and pinky_x != 0 and pinky_y != 0:
#                 if abs(thumb_y - pinky_y) < 70:
#                     pyautogui.dragTo(pinky_x, pinky_y, button='left')
#                     pyautogui.sleep(0.1)  # Reduced sleep time

#     cv2.imshow('Virtual Mouse', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
# import cv2
# import numpy as np
# import mediapipe as mp
# import pyautogui

# cap = cv2.VideoCapture(0)
# hand_detector = mp.solutions.hands.Hands()
# screen_width, screen_height = pyautogui.size()

# while True:
#     _, frame = cap.read()
#     frame = cv2.flip(frame, 1)
#     frame_height, frame_width, _ = frame.shape
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     output = hand_detector.process(rgb_frame)
#     hands = output.multi_hand_landmarks

#     if hands:
#         for hand in hands:
#             landmarks = hand.landmark
#             index_x, index_y = 0, 0
#             thumb_x, thumb_y = 0, 0
#             pinky_x, pinky_y = 0, 0

#             for id, landmark in enumerate(landmarks):
#                 x = int(landmark.x * frame_width)
#                 y = int(landmark.y * frame_height)

#                 if id == 8:  # Index finger tip
#                     index_x = (screen_width / frame_width) * x
#                     index_y = (screen_height / frame_height) * y

#                 if id == 4:  # Thumb tip
#                     thumb_x = (screen_width / frame_width) * x
#                     thumb_y = (screen_height / frame_height) * y

#                 if id == 20:  # Pinky finger tip
#                     pinky_x = (screen_width / frame_width) * x
#                     pinky_y = (screen_height / frame_height) * y

#                 # Draw circles at finger tip positions
#                 cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

#             # Drag (Thumb + Pinky)
#             if thumb_x != 0 and thumb_y != 0 and pinky_x != 0 and pinky_y != 0:
#                 if abs(thumb_y - pinky_y) < 70:
#                     pyautogui.dragTo(pinky_x, pinky_y, button='left')
#                     cv2.putText(frame, 'Dragging Mouse', (50, 50),
#                                 cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

#     cv2.imshow('Virtual Mouse', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
# import cv2
# import numpy as np
# import mediapipe as mp
# import pyautogui


# cap = cv2.VideoCapture(0)
# hand_detector = mp.solutions.hands.Hands()
# screen_width, screen_height = pyautogui.size()

# # Function to perform left click


# def left_click():
#     pyautogui.click()

# # Function to perform right click


# def right_click():
#     pyautogui.rightClick()

# # Function to perform scrolling


# def scroll(direction):
#     if direction == 'up':
#         pyautogui.scroll(10)  # Scroll up
#     elif direction == 'down':
#         pyautogui.scroll(-10)  # Scroll down

# # Function to perform zoom in


# def zoom_in():
#     pyautogui.keyDown('command')
#     pyautogui.press('+')
#     pyautogui.keyUp('command')

# # Function to perform zoom out


# def zoom_out():
#     pyautogui.keyDown('command')
#     pyautogui.press('-')
#     pyautogui.keyUp('command')

# # Function to perform three-finger swipe for screen change in Mac


# def three_finger_swipe(direction):
#     if direction == 'left':
#         pyautogui.hotkey('ctrl', 'left')
#     elif direction == 'right':
#         pyautogui.hotkey('ctrl', 'right')


# while True:
#     _, frame = cap.read()
#     frame = cv2.flip(frame, 1)
#     frame_height, frame_width, _ = frame.shape
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     output = hand_detector.process(rgb_frame)
#     hands = output.multi_hand_landmarks

#     if hands:
#         for hand in hands:
#             landmarks = hand.landmark
#             index_x, index_y = 0, 0
#             thumb_x, thumb_y = 0, 0
#             pinky_x, pinky_y = 0, 0

#             for id, landmark in enumerate(landmarks):
#                 x = int(landmark.x * frame_width)
#                 y = int(landmark.y * frame_height)

#                 if id == 8:  # Index finger tip
#                     index_x = (screen_width / frame_width) * x
#                     index_y = (screen_height / frame_height) * y

#                 if id == 4:  # Thumb tip
#                     thumb_x = (screen_width / frame_width) * x
#                     thumb_y = (screen_height / frame_height) * y

#                 if id == 20:  # Pinky finger tip
#                     pinky_x = (screen_width / frame_width) * x
#                     pinky_y = (screen_height / frame_height) * y

#                 # Draw circles at finger tip positions
#                 cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

#             # Drag and drop (Thumb + Pinky)
#             if thumb_x != 0 and thumb_y != 0 and pinky_x != 0 and pinky_y != 0:
#                 if abs(thumb_y - pinky_y) < 70:
#                     pyautogui.dragTo(pinky_x, pinky_y, button='left')

#             # Perform actions based on finger positions
#             if index_x != 0 and index_y != 0:
#                 # Left-click (Index + Thumb)
#                 if thumb_x != 0 and thumb_y != 0:
#                     if abs(index_y - thumb_y) < 70:
#                         left_click()

#                 # Right-click (Index + Pinky)
#                 if pinky_x != 0 and pinky_y != 0:
#                     if abs(index_y - pinky_y) < 70:
#                         right_click()

#                 # Scroll (Index + Middle)
#                 if abs(index_y - thumb_y) < 70:
#                     if thumb_y > index_y:
#                         scroll('up')
#                     else:
#                         scroll('down')

#                 # Zoom in (Index + Pinky)
#                 if abs(index_y - pinky_y) < 70:
#                     if pinky_y < index_y:
#                         zoom_in()

#                 # Zoom out (Index + Ring)
#                 if abs(index_y - pinky_y) < 70:
#                     if pinky_y > index_y:
#                         zoom_out()

#                 # Three-finger swipe for screen change in Mac
#                 if thumb_x != 0 and pinky_x != 0:
#                     if abs(thumb_y - pinky_y) < 70:
#                         if thumb_x < pinky_x:
#                             three_finger_swipe('right')
#                         else:
#                             three_finger_swipe('left')

#     cv2.imshow('Virtual Mouse', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
# import cv2
# import numpy as np
# import mediapipe as mp
# import pyautogui

# cap = cv2.VideoCapture(0)
# hand_detector = mp.solutions.hands.Hands()
# screen_width, screen_height = pyautogui.size()

# # Function to perform left click


# def left_click():
#     print("Left Click")
#     pyautogui.click()

# # Function to perform right click


# def right_click():
#     print("Right Click")
#     pyautogui.rightClick()

# # Function to perform scrolling


# def scroll(direction):
#     print("Scroll:", direction)
#     if direction == 'up':
#         pyautogui.scroll(10)  # Scroll up
#     elif direction == 'down':
#         pyautogui.scroll(-10)  # Scroll down

# # Function to perform zoom in


# def zoom_in():
#     print("Zoom In")
#     pyautogui.keyDown('command')
#     pyautogui.press('+')
#     pyautogui.keyUp('command')

# # Function to perform zoom out


# def zoom_out():
#     print("Zoom Out")
#     pyautogui.keyDown('command')
#     pyautogui.press('-')
#     pyautogui.keyUp('command')

# # Function to perform three-finger swipe for screen change in Mac


# def three_finger_swipe(direction):
#     print("Three Finger Swipe:", direction)
#     if direction == 'left':
#         pyautogui.hotkey('ctrl', 'left')
#     elif direction == 'right':
#         pyautogui.hotkey('ctrl', 'right')

# # Function to move the cursor


# def move_cursor(x, y):
#     screen_x = int(x * screen_width)
#     screen_y = int(y * screen_height)
#     pyautogui.moveTo(screen_x, screen_y)

# # Function to map hand coordinates to screen coordinates


# def map_to_screen(x, y):
#     return x, y


# while True:
#     _, frame = cap.read()
#     frame = cv2.flip(frame, 1)
#     frame_height, frame_width, _ = frame.shape
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     output = hand_detector.process(rgb_frame)
#     hands = output.multi_hand_landmarks

#     if hands:
#         for hand in hands:
#             landmarks = hand.landmark
#             index_x, index_y = 0, 0
#             thumb_x, thumb_y = 0, 0
#             pinky_x, pinky_y = 0, 0

#             for id, landmark in enumerate(landmarks):
#                 x = landmark.x
#                 y = landmark.y

#                 if id == 8:  # Index finger tip
#                     index_x, index_y = map_to_screen(x, y)

#                 if id == 4:  # Thumb tip
#                     thumb_x, thumb_y = map_to_screen(x, y)

#                 if id == 20:  # Pinky finger tip
#                     pinky_x, pinky_y = map_to_screen(x, y)

#                 # Draw circles at finger tip positions
#                 cv2.circle(frame, (int(x * frame_width),
#                            int(y * frame_height)), 5, (0, 255, 0), -1)

#             # Perform actions based on finger positions
#             if index_x != 0 and index_y != 0:
#                 # Move the cursor
#                 move_cursor(index_x, index_y)

#                 # Left-click (Index + Thumb)
#                 if thumb_x != 0 and thumb_y != 0:
#                     if abs(index_y - thumb_y) < 70:
#                         left_click()

#                 # Right-click (Index + Pinky)
#                 if pinky_x != 0 and pinky_y != 0:
#                     if abs(index_y - pinky_y) < 70:
#                         right_click()

#                 # Scroll (Index + Middle)
#                 if abs(index_y - thumb_y) < 70:
#                     if thumb_y > index_y:
#                         scroll('up')
#                     else:
#                         scroll('down')

#                 # Zoom in (Index + Pinky)
#                 if abs(index_y - pinky_y) < 70:
#                     if pinky_y < index_y:
#                         zoom_in()

#                 # Zoom out (Index + Ring)
#                 if abs(index_y - pinky_y) < 70:
#                     if pinky_y > index_y:
#                         zoom_out()

#                 # Three-finger swipe for screen change in Mac
#                 if thumb_x != 0 and pinky_x != 0:
#                     if abs(thumb_y - pinky_y) < 70:
#                         if thumb_x < pinky_x:
#                             three_finger_swipe('right')
#                         else:
#                             three_finger_swipe('left')

#     cv2.imshow('Virtual Mouse', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
# import cv2
# import numpy as np
# import mediapipe as mp
# import pyautogui

# cap = cv2.VideoCapture(0)
# hand_detector = mp.solutions.hands.Hands()
# screen_width, screen_height = pyautogui.size()

# # Smoothness factor for cursor movement
# SMOOTHNESS_FACTOR = 0.5
# # Number of frames to use for the moving average filter
# MOVING_AVERAGE_WINDOW = 5

# # Function to perform left click


# def left_click():
#     print("Left Click")
#     pyautogui.click()

# # Function to perform right click


# def right_click():
#     print("Right Click")
#     pyautogui.rightClick()

# # Function to perform scrolling


# def scroll(direction):
#     print("Scroll:", direction)
#     if direction == 'up':
#         pyautogui.scroll(10)  # Scroll up
#     elif direction == 'down':
#         pyautogui.scroll(-10)  # Scroll down

# # Function to perform zoom in


# def zoom_in():
#     print("Zoom In")
#     pyautogui.keyDown('command')
#     pyautogui.press('+')
#     pyautogui.keyUp('command')

# # Function to perform zoom out


# def zoom_out():
#     print("Zoom Out")
#     pyautogui.keyDown('command')
#     pyautogui.press('-')
#     pyautogui.keyUp('command')

# # Function to perform three-finger swipe for screen change in Mac


# def three_finger_swipe(direction):
#     print("Three Finger Swipe:", direction)
#     if direction == 'left':
#         pyautogui.hotkey('ctrl', 'left')
#     elif direction == 'right':
#         pyautogui.hotkey('ctrl', 'right')

# # Function to move the cursor smoothly


# def move_cursor_smoothly(x, y, smoothness):
#     current_x, current_y = pyautogui.position()
#     target_x = int(x * screen_width)
#     target_y = int(y * screen_height)
#     new_x = current_x + smoothness * (target_x - current_x)
#     new_y = current_y + smoothness * (target_y - current_y)
#     pyautogui.moveTo(new_x, new_y)

# # Function to calculate moving average of hand positions


# def moving_average(data, window):
#     return np.convolve(data, np.ones(window)/window, mode='valid')

# # Function to map hand coordinates to screen coordinates


# def map_to_screen(x, y):
#     return x, y


# # Initialize variables for smoothing
# smooth_index_x, smooth_index_y = 0, 0
# smoothed_index_x, smoothed_index_y = [], []

# while True:
#     _, frame = cap.read()
#     frame = cv2.flip(frame, 1)
#     frame_height, frame_width, _ = frame.shape
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     output = hand_detector.process(rgb_frame)
#     hands = output.multi_hand_landmarks

#     if hands:
#         for hand in hands:
#             landmarks = hand.landmark
#             index_x, index_y = 0, 0
#             thumb_x, thumb_y = 0, 0
#             pinky_x, pinky_y = 0, 0

#             for id, landmark in enumerate(landmarks):
#                 x = landmark.x
#                 y = landmark.y

#                 if id == 8:  # Index finger tip
#                     index_x, index_y = map_to_screen(x, y)

#                 if id == 4:  # Thumb tip
#                     thumb_x, thumb_y = map_to_screen(x, y)

#                 if id == 20:  # Pinky finger tip
#                     pinky_x, pinky_y = map_to_screen(x, y)

#             # Smooth the index finger position
#             if index_x != 0 and index_y != 0:
#                 smoothed_index_x.append(index_x)
#                 smoothed_index_y.append(index_y)
#                 if len(smoothed_index_x) > MOVING_AVERAGE_WINDOW:
#                     smoothed_index_x.pop(0)
#                     smoothed_index_y.pop(0)
#                 smooth_index_x = moving_average(
#                     smoothed_index_x, MOVING_AVERAGE_WINDOW)[0]
#                 smooth_index_y = moving_average(
#                     smoothed_index_y, MOVING_AVERAGE_WINDOW)[0]

#             # Perform actions based on finger positions
#             if smooth_index_x != 0 and smooth_index_y != 0:
#                 # Move the cursor smoothly
#                 move_cursor_smoothly(smooth_index_x, smooth_index_y, 0.2)

#                 # Left-click (Index + Thumb)
#                 if thumb_x != 0 and thumb_y != 0:
#                     if abs(index_y - thumb_y) < 70:
#                         left_click()

#                 # Right-click (Index + Pinky)
#                 if pinky_x != 0 and pinky_y != 0:
#                     if abs(index_y - pinky_y) < 70:
#                         right_click()

#                 # Scroll (Index + Middle)
#                 if abs(index_y - thumb_y) < 70:
#                     if thumb_y > index_y:
#                         scroll('up')
#                     else:
#                         scroll('down')

#                 # Zoom in (Index + Pinky)
#                 if abs(index_y - pinky_y) < 70:
#                     if pinky_y < index_y:
#                         zoom_in()

#                 # Zoom out (Index + Ring)
#                 if abs(index_y - pinky_y) < 70:
#                     if pinky_y > index_y:
#                         zoom_out()

#                 # Three-finger swipe for screen change in Mac
#                 if thumb_x != 0 and pinky_x != 0:
#                     if abs(thumb_y - pinky_y) < 70:
#                         if thumb_x < pinky_x:
#                             three_finger_swipe('right')
#                         else:
#                             three_finger_swipe('left')

#     cv2.imshow('Virtual Mouse', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


# CURSOR WORKING GOOD
# import cv2
# import numpy as np
# import mediapipe as mp
# import pyautogui

# cap = cv2.VideoCapture(0)
# hand_detector = mp.solutions.hands.Hands()
# screen_width, screen_height = pyautogui.size()

# # Smoothness factor for cursor movement
# SMOOTHNESS_FACTOR = 0.5
# # Number of frames to use for the moving average filter
# MOVING_AVERAGE_WINDOW = 5

# # Function to move the cursor smoothly


# def move_cursor_smoothly(x, y, smoothness):
#     current_x, current_y = pyautogui.position()
#     target_x = int(x * screen_width)
#     target_y = int(y * screen_height)
#     new_x = current_x + smoothness * (target_x - current_x)
#     new_y = current_y + smoothness * (target_y - current_y)
#     pyautogui.moveTo(new_x, new_y)

# # Function to calculate moving average of hand positions


# def moving_average(data, window):
#     return np.convolve(data, np.ones(window)/window, mode='valid')

# # Function to map hand coordinates to screen coordinates


# def map_to_screen(x, y):
#     return x, y


# # Initialize variables for smoothing
# smooth_index_x, smooth_index_y = 0, 0
# smooth_middle_x, smooth_middle_y = 0, 0
# smoothed_index_x, smoothed_index_y = [], []
# smoothed_middle_x, smoothed_middle_y = [], []

# while True:
#     _, frame = cap.read()
#     frame = cv2.flip(frame, 1)
#     frame_height, frame_width, _ = frame.shape
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     output = hand_detector.process(rgb_frame)
#     hands = output.multi_hand_landmarks

#     if hands:
#         for hand in hands:
#             landmarks = hand.landmark
#             index_x, index_y = 0, 0
#             middle_x, middle_y = 0, 0
#             for id, landmark in enumerate(landmarks):
#                 x = landmark.x
#                 y = landmark.y

#                 if id == 8:  # Index finger tip
#                     index_x, index_y = map_to_screen(x, y)

#                 if id == 12:  # Middle finger tip
#                     middle_x, middle_y = map_to_screen(x, y)

#             # Smooth the index finger position
#             if index_x != 0 and index_y != 0:
#                 smoothed_index_x.append(index_x)
#                 smoothed_index_y.append(index_y)
#                 if len(smoothed_index_x) > MOVING_AVERAGE_WINDOW:
#                     smoothed_index_x.pop(0)
#                     smoothed_index_y.pop(0)
#                 smooth_index_x = moving_average(
#                     smoothed_index_x, MOVING_AVERAGE_WINDOW)[0]
#                 smooth_index_y = moving_average(
#                     smoothed_index_y, MOVING_AVERAGE_WINDOW)[0]

#             # Smooth the middle finger position
#             if middle_x != 0 and middle_y != 0:
#                 smoothed_middle_x.append(middle_x)
#                 smoothed_middle_y.append(middle_y)
#                 if len(smoothed_middle_x) > MOVING_AVERAGE_WINDOW:
#                     smoothed_middle_x.pop(0)
#                     smoothed_middle_y.pop(0)
#                 smooth_middle_x = moving_average(
#                     smoothed_middle_x, MOVING_AVERAGE_WINDOW)[0]
#                 smooth_middle_y = moving_average(
#                     smoothed_middle_y, MOVING_AVERAGE_WINDOW)[0]

#             # Perform actions based on finger positions
#             if smooth_index_x != 0 and smooth_index_y != 0 and smooth_middle_x != 0 and smooth_middle_y != 0:
#                 # Move the cursor smoothly using the index finger position
#                 move_cursor_smoothly(
#                     smooth_index_x, smooth_index_y, SMOOTHNESS_FACTOR)

#     cv2.imshow('Virtual Mouse', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
# import cv2
# import numpy as np
# import mediapipe as mp
# import pyautogui

# cap = cv2.VideoCapture(0)
# hand_detector = mp.solutions.hands.Hands()
# screen_width, screen_height = pyautogui.size()

# # Smoothness factor for cursor movement
# SMOOTHNESS_FACTOR = 0.5
# # Number of frames to use for the moving average filter
# MOVING_AVERAGE_WINDOW = 5

# # Function to move the cursor smoothly


# def move_cursor_smoothly(x, y, smoothness):
#     current_x, current_y = pyautogui.position()
#     target_x = int(x * screen_width)
#     target_y = int(y * screen_height)
#     new_x = current_x + smoothness * (target_x - current_x)
#     new_y = current_y + smoothness * (target_y - current_y)
#     pyautogui.moveTo(new_x, new_y)

# # Function to calculate moving average of hand positions


# def moving_average(data, window):
#     return np.convolve(data, np.ones(window)/window, mode='valid')

# # Function to map hand coordinates to screen coordinates


# def map_to_screen(x, y):
#     return x, y


# # Initialize variables for smoothing
# smooth_index_x, smooth_index_y = 0, 0
# smooth_thumb_x, smooth_thumb_y = 0, 0
# smoothed_index_x, smoothed_index_y = [], []
# smoothed_thumb_x, smoothed_thumb_y = [], []

# # Initialize variables for double-click gesture
# joined_frames = 0
# JOINED_FRAMES_THRESHOLD = 10  # Adjust as needed

# while True:
#     _, frame = cap.read()
#     frame = cv2.flip(frame, 1)
#     frame_height, frame_width, _ = frame.shape
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     output = hand_detector.process(rgb_frame)
#     hands = output.multi_hand_landmarks

#     if hands:
#         for hand in hands:
#             landmarks = hand.landmark
#             index_x, index_y = 0, 0
#             thumb_x, thumb_y = 0, 0
#             for id, landmark in enumerate(landmarks):
#                 x = landmark.x
#                 y = landmark.y

#                 if id == 8:  # Index finger tip
#                     index_x, index_y = map_to_screen(x, y)

#                 if id == 4:  # Thumb tip
#                     thumb_x, thumb_y = map_to_screen(x, y)

#             # Smooth the index finger position
#             if index_x != 0 and index_y != 0:
#                 smoothed_index_x.append(index_x)
#                 smoothed_index_y.append(index_y)
#                 if len(smoothed_index_x) > MOVING_AVERAGE_WINDOW:
#                     smoothed_index_x.pop(0)
#                     smoothed_index_y.pop(0)
#                 smooth_index_x = moving_average(
#                     smoothed_index_x, MOVING_AVERAGE_WINDOW)[0]
#                 smooth_index_y = moving_average(
#                     smoothed_index_y, MOVING_AVERAGE_WINDOW)[0]

#             # Smooth the thumb finger position
#             if thumb_x != 0 and thumb_y != 0:
#                 smoothed_thumb_x.append(thumb_x)
#                 smoothed_thumb_y.append(thumb_y)
#                 if len(smoothed_thumb_x) > MOVING_AVERAGE_WINDOW:
#                     smoothed_thumb_x.pop(0)
#                     smoothed_thumb_y.pop(0)
#                 smooth_thumb_x = moving_average(
#                     smoothed_thumb_x, MOVING_AVERAGE_WINDOW)[0]
#                 smooth_thumb_y = moving_average(
#                     smoothed_thumb_y, MOVING_AVERAGE_WINDOW)[0]

#             # Perform actions based on finger positions
#             if smooth_index_x != 0 and smooth_index_y != 0 and smooth_thumb_x != 0 and smooth_thumb_y != 0:
#                 # Move the cursor smoothly using the index finger position
#                 move_cursor_smoothly(
#                     smooth_index_x, smooth_index_y, SMOOTHNESS_FACTOR)

#             # Calculate distance between thumb and index finger
#             thumb_index_distance = np.sqrt(
#                 (smooth_thumb_x - smooth_index_x)**2 + (smooth_thumb_y - smooth_index_y)**2)

#             # If thumb and index finger are close, increment joined_frames
#             if thumb_index_distance < 50:  # Adjust threshold as needed
#                 joined_frames += 1
#                 # If joined_frames exceeds the threshold, trigger a double-click
#                 if joined_frames >= JOINED_FRAMES_THRESHOLD:
#                     pyautogui.doubleClick()
#             else:
#                 joined_frames = 0  # Reset joined_frames if fingers are not joined

#     cv2.imshow('Virtual Mouse', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
# import cv2
# import numpy as np
# import mediapipe as mp
# import pyautogui

# cap = cv2.VideoCapture(0)
# hand_detector = mp.solutions.hands.Hands()
# screen_width, screen_height = pyautogui.size()

# # Smoothness factor for cursor movement
# SMOOTHNESS_FACTOR = 0.5
# # Number of frames to use for the moving average filter
# MOVING_AVERAGE_WINDOW = 5

# # Function to move the cursor smoothly


# def move_cursor_smoothly(x, y, smoothness):
#     current_x, current_y = pyautogui.position()
#     target_x = int(x * screen_width)
#     target_y = int(y * screen_height)
#     new_x = current_x + smoothness * (target_x - current_x)
#     new_y = current_y + smoothness * (target_y - current_y)
#     pyautogui.moveTo(new_x, new_y)

# # Function to calculate moving average of hand positions


# def moving_average(data, window):
#     return np.convolve(data, np.ones(window)/window, mode='valid')

# # Function to map hand coordinates to screen coordinates


# def map_to_screen(x, y):
#     return x, y


# # Initialize variables for smoothing
# smooth_index_x, smooth_index_y = 0, 0
# smooth_middle_x, smooth_middle_y = 0, 0
# smoothed_index_x, smoothed_index_y = [], []
# smoothed_middle_x, smoothed_middle_y = [], []

# while True:
#     _, frame = cap.read()
#     frame = cv2.flip(frame, 1)
#     frame_height, frame_width, _ = frame.shape
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     output = hand_detector.process(rgb_frame)
#     hands = output.multi_hand_landmarks

#     if hands:
#         for hand in hands:
#             landmarks = hand.landmark
#             index_x, index_y = 0, 0
#             middle_x, middle_y = 0, 0
#             for id, landmark in enumerate(landmarks):
#                 x = landmark.x
#                 y = landmark.y

#                 if id == 8:  # Index finger tip
#                     index_x, index_y = map_to_screen(x, y)

#                 if id == 12:  # Middle finger tip
#                     middle_x, middle_y = map_to_screen(x, y)

#             # Smooth the index finger position
#             if index_x != 0 and index_y != 0:
#                 smoothed_index_x.append(index_x)
#                 smoothed_index_y.append(index_y)
#                 if len(smoothed_index_x) > MOVING_AVERAGE_WINDOW:
#                     smoothed_index_x.pop(0)
#                     smoothed_index_y.pop(0)
#                 smooth_index_x = moving_average(
#                     smoothed_index_x, MOVING_AVERAGE_WINDOW)[0]
#                 smooth_index_y = moving_average(
#                     smoothed_index_y, MOVING_AVERAGE_WINDOW)[0]

#             # Smooth the middle finger position
#             if middle_x != 0 and middle_y != 0:
#                 smoothed_middle_x.append(middle_x)
#                 smoothed_middle_y.append(middle_y)
#                 if len(smoothed_middle_x) > MOVING_AVERAGE_WINDOW:
#                     smoothed_middle_x.pop(0)
#                     smoothed_middle_y.pop(0)
#                 smooth_middle_x = moving_average(
#                     smoothed_middle_x, MOVING_AVERAGE_WINDOW)[0]
#                 smooth_middle_y = moving_average(
#                     smoothed_middle_y, MOVING_AVERAGE_WINDOW)[0]

#             # Perform actions based on finger positions
#             if smooth_index_x != 0 and smooth_index_y != 0 and smooth_middle_x != 0 and smooth_middle_y != 0:
#                 # Move the cursor smoothly using the index finger position
#                 move_cursor_smoothly(
#                     smooth_index_x, smooth_index_y, SMOOTHNESS_FACTOR)

#     cv2.imshow('Virtual Mouse', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
# Three swipe and cursor moving cool
# import cv2
# import numpy as np
# import mediapipe as mp
# import pyautogui
# import time

# cap = cv2.VideoCapture(0)
# hand_detector = mp.solutions.hands.Hands()
# screen_width, screen_height = pyautogui.size()

# # Smoothness factor for cursor movement
# SMOOTHNESS_FACTOR = 0.5
# # Number of frames to use for the moving average filter
# MOVING_AVERAGE_WINDOW = 5
# # Delay in seconds for the swipe action
# SWIPE_DELAY = 1.0  # Adjust as needed

# # Initialize previous finger position
# previous_x = None

# # Function to move the cursor smoothly


# def move_cursor_smoothly(x, y, smoothness):
#     current_x, current_y = pyautogui.position()
#     target_x = int(x * screen_width)
#     target_y = int(y * screen_height)
#     new_x = current_x + smoothness * (target_x - current_x)
#     new_y = current_y + smoothness * (target_y - current_y)
#     pyautogui.moveTo(new_x, new_y)

# # Function to check if fingers moved to the right


# def fingers_moved_right(previous_x, current_x):
#     if previous_x is not None:
#         return current_x > previous_x + 0.05  # Adjust sensitivity by changing the value
#     return False

# # Function to check if fingers moved to the left


# def fingers_moved_left(previous_x, current_x):
#     if previous_x is not None:
#         return current_x < previous_x - 0.05  # Adjust sensitivity by changing the value
#     return False


# # Main loop
# while True:
#     _, frame = cap.read()
#     frame = cv2.flip(frame, 1)
#     frame_height, frame_width, _ = frame.shape
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     output = hand_detector.process(rgb_frame)
#     hands = output.multi_hand_landmarks

#     if hands:
#         for hand in hands:
#             landmarks = [(lm.x, lm.y) for lm in hand.landmark]
#             index_x, index_y = landmarks[8]  # Index finger tip

#             # Perform actions based on finger positions
#             if fingers_moved_right(previous_x, index_x):
#                 # Perform right screen shift action
#                 # Example: Ctrl + Right arrow
#                 pyautogui.hotkey('ctrl', 'right')
#                 time.sleep(SWIPE_DELAY)  # Introduce delay
#             elif fingers_moved_left(previous_x, index_x):
#                 # Perform left screen shift action
#                 pyautogui.hotkey('ctrl', 'left')  # Example: Ctrl + Left arrow
#                 time.sleep(SWIPE_DELAY)  # Introduce delay

#             # Store previous finger positions for the next iteration
#             previous_x = index_x

#             # Move the cursor smoothly using the index finger position
#             move_cursor_smoothly(index_x, index_y, SMOOTHNESS_FACTOR)

#     cv2.imshow('Virtual Mouse', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


# import cv2
# import numpy as np
# import mediapipe as mp
# import pyautogui
# import time

# cap = cv2.VideoCapture(0)
# hand_detector = mp.solutions.hands.Hands()
# screen_width, screen_height = pyautogui.size()

# # Smoothness factor for cursor movement
# SMOOTHNESS_FACTOR = 0.5
# # Number of frames to use for the moving average filter
# MOVING_AVERAGE_WINDOW = 5
# # Delay in seconds for the swipe action
# SWIPE_DELAY = 1.0  # Adjust as needed

# # Initialize previous finger position
# previous_x = None

# # Function to move the cursor smoothly


# def move_cursor_smoothly(x, y, smoothness):
#     current_x, current_y = pyautogui.position()
#     target_x = int(x * screen_width)
#     target_y = int(y * screen_height)
#     new_x = current_x + smoothness * (target_x - current_x)
#     new_y = current_y + smoothness * (target_y - current_y)
#     pyautogui.moveTo(new_x, new_y)

# # Function to check if fingers moved to the right


# def fingers_moved_right(previous_x, current_x):
#     if previous_x is not None:
#         return current_x > previous_x + 0.02  # Adjust sensitivity by changing the value
#     return False

# # Function to check if fingers moved to the left


# def fingers_moved_left(previous_x, current_x):
#     if previous_x is not None:
#         return current_x < previous_x - 0.02  # Adjust sensitivity by changing the value
#     return False

# # Function to detect three fingers


# def detect_three_fingers(landmarks):
#     if len(landmarks) == 3:
#         return True
#     return False


# # Main loop
# while True:
#     _, frame = cap.read()
#     frame = cv2.flip(frame, 1)
#     frame_height, frame_width, _ = frame.shape
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     output = hand_detector.process(rgb_frame)
#     hands = output.multi_hand_landmarks

#     if hands:
#         for hand in hands:
#             landmarks = [(lm.x, lm.y) for lm in hand.landmark]
#             index_x, index_y = landmarks[8]  # Index finger tip

#             # Check if three fingers are detected
#             if detect_three_fingers(landmarks):
#                 # Perform actions based on finger positions
#                 if fingers_moved_right(previous_x, index_x):
#                     # Perform right screen shift action
#                     # Example: Ctrl + Right arrow
#                     pyautogui.hotkey('ctrl', 'right')
#                     time.sleep(SWIPE_DELAY)  # Introduce delay
#                 elif fingers_moved_left(previous_x, index_x):
#                     # Perform left screen shift action
#                     # Example: Ctrl + Left arrow
#                     pyautogui.hotkey('ctrl', 'left')
#                     time.sleep(SWIPE_DELAY)  # Introduce delay

#                 # Store previous finger positions for the next iteration
#                 previous_x = index_x

#             # Move the cursor smoothly using the index finger position
#             move_cursor_smoothly(index_x, index_y, SMOOTHNESS_FACTOR)

#     cv2.imshow('Virtual Mouse', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
# import cv2
# import numpy as np
# import mediapipe as mp
# import pyautogui
# import time

# cap = cv2.VideoCapture(0)
# hand_detector = mp.solutions.hands.Hands()
# screen_width, screen_height = pyautogui.size()

# # Smoothness factor for cursor movement
# SMOOTHNESS_FACTOR = 0.5

# # Initialize previous finger positions
# previous_x = None

# # Function to move the cursor smoothly


# def move_cursor_smoothly(x, y, smoothness):
#     current_x, current_y = pyautogui.position()
#     target_x = int(x * screen_width)
#     target_y = int(y * screen_height)
#     new_x = current_x + smoothness * (target_x - current_x)
#     new_y = current_y + smoothness * (target_y - current_y)
#     pyautogui.moveTo(new_x, new_y)

# # Function to check if fingers moved to the right


# def fingers_moved_right(previous_x, current_x):
#     if previous_x is not None:
#         return current_x > previous_x + 0.02  # Adjust sensitivity by changing the value
#     return False

# # Function to check if fingers moved to the left


# def fingers_moved_left(previous_x, current_x):
#     if previous_x is not None:
#         return current_x < previous_x - 0.02  # Adjust sensitivity by changing the value
#     return False

# # Function to detect a single finger


# def detect_single_finger(landmarks):
#     if len(landmarks) == 1:
#         return True
#     return False

# # Function to detect two fingers


# def detect_two_fingers(landmarks):
#     if len(landmarks) == 2:
#         return True
#     return False


# # Main loop
# while True:
#     _, frame = cap.read()
#     frame = cv2.flip(frame, 1)
#     frame_height, frame_width, _ = frame.shape
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     output = hand_detector.process(rgb_frame)
#     hands = output.multi_hand_landmarks

#     if hands:
#         for hand in hands:
#             landmarks = [(lm.x, lm.y) for lm in hand.landmark]
#             index_x, index_y = landmarks[8]  # Index finger tip

#             # Perform actions based on finger positions
#             if detect_single_finger(landmarks):
#                 # Perform left click action
#                 pyautogui.click(button='left')
#             elif detect_two_fingers(landmarks):
#                 # Perform double click action
#                 pyautogui.doubleClick()

#             # Store previous finger positions for the next iteration
#             previous_x = index_x

#             # Move the cursor smoothly using the index finger position
#             move_cursor_smoothly(index_x, index_y, SMOOTHNESS_FACTOR)

#     cv2.imshow('Virtual Mouse', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
import cv2
import numpy as np
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
screen_width, screen_height = pyautogui.size()

# Smoothness factor for cursor movement
SMOOTHNESS_FACTOR = 0.5

# Initialize previous finger positions
previous_x = None

# Function to move the cursor smoothly


def move_cursor_smoothly(x, y, smoothness):
    current_x, current_y = pyautogui.position()
    target_x = int(x * screen_width)
    target_y = int(y * screen_height)
    new_x = current_x + smoothness * (target_x - current_x)
    new_y = current_y + smoothness * (target_y - current_y)
    pyautogui.moveTo(new_x, new_y)

# Function to detect two fingers


def detect_two_fingers(landmarks):
    return len(landmarks) == 2

# Function to detect three fingers


def detect_three_fingers(landmarks):
    return len(landmarks) == 3


# Main loop
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            landmarks = [(lm.x, lm.y) for lm in hand.landmark]
            thumb_x, thumb_y = landmarks[4]  # Thumb tip
            index_x, index_y = landmarks[8]  # Index finger tip
            middle_x, middle_y = landmarks[12]  # Middle finger tip

            # Perform actions based on finger positions
            if detect_two_fingers(landmarks) and abs(thumb_x - index_x) < 0.05 and abs(thumb_y - index_y) < 0.05:
                # Single click when thumb and index finger are joined
                pyautogui.click()
            elif detect_two_fingers(landmarks) and abs(thumb_x - middle_x) < 0.05 and abs(thumb_y - middle_y) < 0.05:
                # Double click when thumb and middle finger are joined
                pyautogui.doubleClick()

            # Move the cursor smoothly using the index finger position
            move_cursor_smoothly(index_x, index_y, SMOOTHNESS_FACTOR)

    cv2.imshow('Virtual Mouse', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
