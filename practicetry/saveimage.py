import cv2
import os

# Ask for the user's name
name = input("Enter your name: ").strip()

# Create filename
filename = f"{name}.jpg"

# Load Haar cascade for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Open webcam
cap = cv2.VideoCapture(0)
print("Opening camera. Press 's' to save image or 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to open camera.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Capture Face', frame)

    key = cv2.waitKey(1)

    # Press 's' to save the image
    if key == ord('s'):
        if len(faces) > 0:
            cv2.imwrite(filename, frame)
            print(f"Image saved as {filename}")
        else:
            print("No face detected, image not saved.")
        break

    # Press 'q' to quit without saving
    if key == ord('q'):
        print("Quitting without saving.")
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
