""" Import Required Libraries """

import cv2                    #cv2: OpenCV – वेबकॅम चालवण्यासाठी आणि इमेजेस प्रोसेस करण्यासाठी
import face_recognition                  #चेहरा ओळखण्यासाठी
import os                  #फोल्डर्स आणि फाईल्सशी काम करण्यासाठी
import pandas as pd                  #Attendance डेटा Excel मध्ये सेव्ह करण्यासाठी.
from datetime import datetime                   #तारीख आणि वेळ मिळवण्यासाठी


"""Function to Add a New User"""
def add_new_user():
    print("\n=== Add New User ===")                  #यूजरचे नाव विचारून, वेबकॅम सुरू केला जातो
    name = input("Enter the name of the Student: ")
    
    # Create image directory if it doesn't exist
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'image')
    if not os.path.exists(path):
        os.makedirs(path)
     
    # Start webcam for capturing
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam")
        return
    
    print("Press SPACE to capture image or ESC to cancel")          #SPACE दाबल्यावर फोटो सेव्ह केला जातो image/ फोल्डरमध्ये <name>.jpg नावाने
    
    while True:
        ret, frame = cap.read()   
        if not ret:
            print("Failed to grab frame")
            break
            
        cv2.imshow('Capture Image', frame)
        
        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # ESC key
            print("Cancelled")
            break
        elif key == 32:                            #ESC दाबल्यास प्रक्रिया रद्द होते
            # Save the image
            image_path = os.path.join(path, f"{name}.jpg")
            cv2.imwrite(image_path, frame)
            print(f"Image saved as {image_path}")
            break
    
    cap.release()
    cv2.destroyAllWindows()


"""Main Menu for User Interaction"""
def show_menu():
    while True:
        print("\n=== Face Recognition System ===")
        print("1. Start Attendance System")                       #Attendance सुरू करणे
        print("2. Add New User")                       #नवीन चेहरा (User) अ‍ॅड करणे
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            return "start"
        elif choice == '2':
            add_new_user()
        elif choice == '3':
            return "exit"
        else:
            print("Invalid choice. Please try again.")


"""Load Saved Face Images (Known Faces)"""
def load_known_faces():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'image')       #image/ फोल्डरमधून सर्व चेहरे (images) घेतले जातात
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created image directory at: {path}")
        print("Please add face images to this directory before running the program again.")
        return [], []

    images = []
    classNames = []
    myList = os.listdir(path)

    for cl in myList:
        if cl.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(path, cl)
            try:
                img = cv2.imread(img_path)
                if img is None:
                    print(f"Warning: Could not read image {cl}")
                    continue
                    
                rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)        # प्रत्येक फोटोमधून चेहरा extract करून encoding बनवली जाते (machine ला ओळखता येईल असा डिजिटल फॉर्म).
                face_encodings = face_recognition.face_encodings(rgb_img)
                if len(face_encodings) > 0:
                    images.append(face_encodings[0])
                    classNames.append(os.path.splitext(cl)[0])         #नाव classNames मध्ये सेव्ह केलं जातं.
                else:
                    print(f"Warning: No face detected in image {cl}")
            except Exception as e:
                print(f"Error processing image {cl}: {str(e)}")
    
    return images, classNames


"""Mark Attendance in Excel File"""
def mark_attendance(name):
    try:
        date = datetime.now().strftime('%Y-%m-%d')
        time = datetime.now().strftime('%H:%M:%S')         #Excel फाईलमध्ये नाव, वेळ, तारीख सेव्ह केलं जातं
         
        # get the directory where the script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        attendance_file = os.path.join(script_dir, 'attendance.xlsx')       #attendance.xlsx नावाची फाईल बनते किंवा अपडेट होते
        
        # Load or create dataframe
        if os.path.exists(attendance_file):
            df = pd.read_excel(attendance_file)
        else:
            df = pd.DataFrame(columns=['Name', 'Date', 'Time'])

        # Check if already marked
        if not ((df['Name'] == name) & (df['Date'] == date)).any():
            new_row = pd.DataFrame([{'Name': name, 'Date': date, 'Time': time}])
            df = pd.concat([df, new_row], ignore_index=True)
            df.to_excel(attendance_file, index=False)
            print(f"Attendance marked for {name} at {time}")
        else:
            print(f"Attendance already marked for {name} today")
    except Exception as e:
        print(f"Error marking attendance: {str(e)}")


""" Main Program Loop"""
if __name__ == "__main__":
    # Load known faces at startup
    print("Loading known faces...")
    images, classNames = load_known_faces()
    
    if len(images) == 0:
        print("No face images found. Please add some faces first using option 2.")
    
    while True:
        choice = show_menu()   #यूजरला मेनू दाखवलं जातं
        
        if choice == "exit":
            print("Thank you for using the Face Recognition System!")
            break
        elif choice == "start":          #जर "Start Attendance System" निवडलं, तर वेबकॅम सुरू होतो
            if len(images) == 0:
                print("No faces registered. Please add faces first using option 2.")
                continue
                
            # Start webcam
            cap = cv2.VideoCapture(0)

            # Check if webcam opened successfully
            if not cap.isOpened():
                print("Error: Could not open webcam")
                print("Please check it:")
                print("1. Your webcam is properly connected")
                print("2. No other application is using the webcam")
                print("3. You have given camera permissions to Python")
                continue

            print("Webcam started successfully!")
            print("Press 'q' to quit")

            while True:
                success, img = cap.read()      #चेहरा सापडल्यास images मध्ये असलेल्या known faces शी तुलना केली जाते
                
                if not success:
                    print("Error: Could not read frame from webcam")
                    print("Trying to reconnect...")
                    cap.release()
                    cap = cv2.VideoCapture(0)
                    if not cap.isOpened():
                        print("Failed to reconnect to webcam")
                        break
                    continue

                try:
                    imgS = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
                    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)      #चेहरा मॅच झाला, तर स्क्रीनवर नाव दाखवते आणि attendance mark होते

                    """Face Recognition Logic"""
                    facesCurFrame = face_recognition.face_locations(imgS)
                    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

                    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                        matches = face_recognition.compare_faces(images, encodeFace)
                        faceDis = face_recognition.face_distance(images, encodeFace)
                        matchIndex = faceDis.argmin()

                        if matches[matchIndex]:       #webcam ची फ्रेम resize करून, चेहेरे detect आणि encode केले जातात.
                            name = classNames[matchIndex].upper()
                            y1, x2, y2, x1 = faceLoc
                            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                            cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 2)
                            cv2.putText(img, name, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

                            mark_attendance(name)

                    cv2.imshow('Webcam', img)   
                except Exception as e:
                    print(f"Error processing frame: {str(e)}")    #जर चेहरा मॅच झाला, तर rectangle आणि नाम दाखवलं जातं
                    continue

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            # Clean up
            cap.release()
            cv2.destroyAllWindows()


