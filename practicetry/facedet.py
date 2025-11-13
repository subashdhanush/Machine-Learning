import cv2
import pandas as pd
from datetime import datetime

# Load the Haar Cascade face detector
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Create an empty DataFrame to store attendance
attendance = pd.DataFrame(columns=["Name", "Time"])

name = input("Enter your name: ")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        attendance = pd.concat([attendance, pd.DataFrame([[name, now]], columns=["Name", "Time"])])
        print(f"Attendance recorded for {name} at {now}")
        break

    cv2.imshow('Face Attendance', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q') or len(faces) == 0:
    
        break

cap.release()
cv2.destroyAllWindows()

# Save to Excel
attendance.drop_duplicates(subset='Name').to_excel("attendance.xlsx", index=False)
print(attendance)
print("Attendance saved to attendance.xlsx")
