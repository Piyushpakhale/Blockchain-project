import cv2
import os
from datetime import datetime
import time
import ipfshttpclient
import numpy as np

# Connect to the local IPFS daemon
api = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')

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

    # Get the current date and time as a string
    current_datetime = datetime.now().strftime("Recording... %Y-%m-%d   %H:%M:%S")

    # Display the date and time in the corner of the window
    cv2.putText(frame, current_datetime, (10, 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)

    # Create a blue frame
    frame_height, frame_width, _ = frame.shape
    blue_frame = np.zeros((frame_height, frame_width, 3), np.uint8)
    blue_frame[:] = (255, 0, 0)  # Set the frame color to blue (BGR format)

    # Display the captured frame in the center of the blue frame
    blue_frame[(blue_frame.shape[0] - frame_height) // 2:(blue_frame.shape[0] - frame_height) // 2 + frame_height,
               (blue_frame.shape[1] - frame_width) // 2:(blue_frame.shape[1] - frame_width) // 2 + frame_width] = frame

    # Display the blue frame with the camera icon
    cv2.imshow("Webcam Capture", blue_frame)

    # Get the current date and time as a string
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Check if it's time to capture a snapshot
    if int(time.time()) - last_capture_time >= capture_interval:
        # Save the frame as an image with the system date and time as the name in the "saved_snaps" folder
        image_filename = f"saved_snaps/{current_datetime}.jpg"
        cv2.imwrite(image_filename, frame)
        print(f"Image saved as '{image_filename}'")

        # Upload the image to IPFS and get the IPFS hash
        with open(image_filename, "rb") as image_file:
            ipfs_hash = api.add(image_file)
            print(f"Image uploaded to IPFS with hash: {ipfs_hash['Hash']}")

        # Construct a URL using a public IPFS gateway
        ipfs_url = f"http://localhost:8080/ipfs/{ipfs_hash['Hash']}"
        print(f"IPFS URL: {ipfs_url}")

        last_capture_time = int(time.time())

    # Handle window events without any delay
    key = cv2.waitKey(1)

    # Press 'q' to exit
    if key == ord('q'):
        break

# Release the webcam and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
