import cv2
import os
from datetime import datetime
import time

# Make sure the "saved_snaps" folder exists
if not os.path.exists("saved_snaps"):
    os.makedirs("saved_snaps")

# Open the webcam (usually 0 or 1 for built-in webcams)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Set the time interval for capturing snapshots in seconds (e.g., 5 seconds)
capture_interval = 5
last_capture_time = 0

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Check if the frame was captured successfully
    if not ret:
        print("Error: Could not read frame.")
        break

    # Display the frame in a window
    cv2.imshow("Webcam Capture", frame)

    # Get the current date and time as a string
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Check if it's time to capture a snapshot
    if int(time.time()) - last_capture_time >= capture_interval:
        # Save the frame as an image with the system date and time as the name in the "saved_snaps" folder
        image_filename = f"saved_snaps/{current_datetime}.jpg"
        cv2.imwrite(image_filename, frame)
        print(f"Image saved as '{image_filename}'")

        last_capture_time = int(time.time())

    # Handle window events without any delay
    key = cv2.waitKey(1)

    # Press 'q' to exit
    if key == ord('q'):
        break

# Release the webcam and close the OpenCV window
cap.release()
cv2.destroyAllWindows()