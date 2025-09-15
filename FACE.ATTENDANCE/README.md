📸 Face Recognition Attendance System

This Python project uses a webcam to detect and recognize faces and automatically saves attendance in an Excel file.

🚀 Features

Face Detection & Recognition using webcam

Add new student/user face

Attendance saved in Excel file (attendance.xlsx)

Prevents duplicate attendance (only one entry per user per day)

CLI-based Menu System

Error handling (e.g., webcam issues, no face detected, etc.)

🛠️ Tech Stack

Python 3.x

OpenCV (cv2)
 → Webcam access & image processing

face_recognition
 → Face detection & recognition

Pandas
 → Save attendance in Excel

datetime
 → Date & time handling

os
 → File & folder operations

📂 Project Structure
Face_Recognition_Attendance/
│── image/                # Stores all student images
│── attendance.xlsx       # Attendance data (auto-created/updated)
│── main.py               # Main program (run this file)
│── README.md             # Documentation

2️⃣ Install required libraries
pip install opencv-python
pip install face_recognition
pip install pandas

3️⃣ Run the program
python main.py

📖 Usage
Main Menu
=== Face Recognition System ===
1. Start Attendance System
2. Add New User
3. Exit

✅ Add New User

Select Option 2

Webcam will open

Press SPACE → Capture and save photo in image/ folder as <name>.jpg

Press ESC → Cancel the process

✅ Start Attendance System

Select Option 1

Webcam will start

When a face is recognized:

Name is displayed on screen

Attendance is saved in attendance.xlsx

Press 'q' → Exit attendance mode

📊 Attendance Output (Excel File Example)
Name	Date	Time
OMKAR	2025-09-15	10:35:12
RAHUL	2025-09-15	10:40:22
⚠️ Notes

Make sure your webcam is connected and accessible

Give camera permissions to Python

Ensure face images are clear and well-lit for better recognition

Do you also want me to make this README GitHub-styled with badges (Python, OpenCV, Pandas) for a professional look?

You said:
all English explain 
ChatGPT said:

Perfect 👍 Here’s a fully English explained version of your README.md — everything clean, simple, and GitHub-ready:

📸 Face Recognition Attendance System

This Python project uses a webcam to recognize faces and automatically saves attendance in an Excel file. It is simple, effective, and easy to use for classrooms, offices, or events.

🚀 Features

Detects and recognizes faces using a webcam

Allows adding a new user (student/employee) face

Saves attendance into Excel file (attendance.xlsx)

Prevents duplicate attendance (only one entry per person per day)

Easy command-line menu for interaction

Handles errors (e.g., webcam not available, no face detected)

🛠️ Technologies Used

Python 3.x

OpenCV
 → for webcam access & image processing

face_recognition
 → for face detection and recognition

Pandas
 → for saving attendance into Excel

datetime
 → for date and time

os
 → for file and folder handling

📂 Project Structure
Face_Recognition_Attendance/
│── image/                # Stores all user images
│── attendance.xlsx       # Attendance records (auto-created/updated)
│── main.py               # Main program file
│── README.md             # Documentation

2️⃣ Install dependencies
pip install opencv-python
pip install face_recognition
pip install pandas

3️⃣ Run the program
python main.py

📖 Usage Guide
Main Menu Options
=== Face Recognition System ===
1. Start Attendance System
2. Add New User
3. Exit

✅ Add New User

Select Option 2

Webcam will open

Press SPACE → Capture and save photo (image/<name>.jpg)

Press ESC → Cancel

✅ Start Attendance System

Select Option 1

Webcam will open

If a face is recognized:

The name is displayed on screen

Attendance is saved in attendance.xlsx

Press 'q' → Quit attendance system

📊 Example Attendance (Excel File)
Name	Date	Time
OMKAR	2025-09-15	10:35:12
RAHUL	2025-09-15	10:40:22
⚠️ Important Notes

Ensure your webcam is properly connected

Make sure Python has camera permissions

Place clear, well-lit images in the image/ folder for better recognition

Attendance file (attendance.xlsx) will be auto-created and updated

👉 This project is perfect for schools, colleges, offices, and events where attendance tracking is required.
