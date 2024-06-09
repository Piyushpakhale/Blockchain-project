import tkinter as tk
from tkinter import messagebox
import cv2
import os
from datetime import datetime
import time

def cam():
    # Make sure the "saved_snaps" folder exists
    if not os.path.exists("saved_snaps"):
        os.makedirs("saved_snaps")

    # Open the webcam (usually 0 or 1 for built-in webcams)
    cap = cv2.VideoCapture(0)
   # cv2.eval('tk::PlaceWindow . centre')   

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


user = "user"
pas = "1234"


def login():
    user_id = entry_user_id.get()
    password = entry_password.get()
    remember_me = remember_me_var.get()
    terms_accepted = terms_var.get()

    if terms_accepted:
        # You can implement your login logic here
        if user_id == str(user) and password == str(pas):
            if remember_me:
                print("User checked 'Remember Me'")
            else:
                print("User did not check 'Remember Me'")
            cam()
            # root.destroy()
        else:
            print("Invalid credentials")
    else:
        print("Please accept the terms and conditions")


def forgot_password():
    # Implement the forgot password logic here
    print("Forgot Password clicked")


def sign_up():
    # Implement the sign-up logic here
    messagebox.showinfo(title="sorry!!!", message="Maximun users reached :( ")

def destroy_win():

    root.destroy

# Create the main window
root = tk.Tk()
root.title("BCCTV Login")
root.iconbitmap('CCTV.ico')

# Set background color to dark grey
root.configure(bg='#5D5D5D')

# User ID
label_user_id = tk.Label(root, text="User ID:", bg='#5D5D5D', fg='white', font=("Arial", 16))
label_user_id.grid(row=0, column=0, padx=10, pady=10, sticky='e')
entry_user_id = tk.Entry(root, font=("Arial", 16))
entry_user_id.grid(row=0, column=1, padx=10, pady=10)

# Password
label_password = tk.Label(root, text="Password:", bg='#5D5D5D', fg='white', font=("Arial", 16))
label_password.grid(row=1, column=0, padx=10, pady=10, sticky='e')
entry_password = tk.Entry(root, show="*", font=("Arial", 16))  # Password is hidden
entry_password.grid(row=1, column=1, padx=10, pady=10)

# Forgot Password Hyperlink
# forgot_password_label = tk.Label(root, text="Forgot Password?", fg="blue", cursor="hand2", font=("Arial", 14))
# forgot_password_label.grid(row=2, column=0, columnspan=2, pady=5)
# forgot_password_label.bind("<Button-1>", lambda event: forgot_password())

# Remember Me Checkbox
remember_me_var = tk.BooleanVar()
check_remember_me = tk.Checkbutton(root, text="remember me                      ", variable=remember_me_var, bg='#5D5D5D', fg='white',
                                   font=("Arial", 14))
check_remember_me.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Accept Terms & Conditions Checkbox
terms_var = tk.BooleanVar()
check_terms = tk.Checkbutton(root, text="Accept Terms & Conditions", variable=terms_var, bg='#5D5D5D', fg='white',
                             font=("Arial", 14))
check_terms.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Log In Button
login_button = tk.Button(root, text="Login", command=login, bg='#390ACA', fg='white', font=(
        "Arial", 16))
login_button.grid(row=5, column=0, padx=10, pady=20)
    
# Sign Up Button
sign_up_button = tk.Button(root, text="Sign Up", command=sign_up, bg='#390ACA', fg='white', font=("Arial", 16))
sign_up_button.grid(row=5, column=1, padx=10, pady=20)


# #close button
# close_button = tk.Button(root, text="closeeeee", command=destroy_win, bg='dark gray', fg='white', font=("Arial", 16))
# close_button.grid(row=6, column=1, columnspan=2, padx=10, pady=20)



# Center the window on the screen
root.geometry('400x420')
root.eval('tk::PlaceWindow . centre')

# Start the main loop
root.mainloop()