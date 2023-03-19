import cv2
import numpy as np

# ASCII character set used for creating the ASCII image
ascii_chars = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

# Create a function to convert the video frame to an ASCII image
def convert_frame_to_ascii(frame):
    # Resize the frame to a smaller size
    frame = cv2.resize(frame, (80, 60))
    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Create an empty ASCII image
    ascii_image = np.empty((60, 80), dtype=np.dtype('U1'))
    # Loop through each pixel of the grayscale image
    for i in range(60):
        for j in range(80):
            # Convert the pixel value to an ASCII character based on its intensity
            ascii_image[i, j] = ascii_chars[int(gray_frame[i, j] / 25.5)]
    return ascii_image

# Create a video capture object
capture = cv2.VideoCapture(0)

# Create a window to display the ASCII video
cv2.namedWindow("ASCII Webcam", cv2.WINDOW_NORMAL)

# Set the font used to display the ASCII characters
font = cv2.FONT_HERSHEY_SIMPLEX

# Loop through each frame of the video
while True:
    # Read a frame from the video capture object
    ret, frame = capture.read()
    # If the frame was read successfully, convert it to an ASCII image and display it
    if ret:
        ascii_image = convert_frame_to_ascii(frame)
        # Display the ASCII image in the window
        # cv2.imshow("ASCII Webcam", cv2.putText(np.zeros((600, 800, 3), np.uint8), "\n".join(["".join(row) for row in ascii_image]), (20, 40), font, 0.6, (255, 255, 255), 2))
        # Display the ASCII image in the window
        ascii_display = np.zeros((600, 800, 3), np.uint8)
        for i in range(60):
            for j in range(80):
                cv2.putText(ascii_display, ascii_image[i, j], (j * 10, i * 10 + 15), font, 0.4, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.imshow("ASCII Webcam", ascii_display)

    # If the frame couldn't be read, break out of the loop
    else:
        break
    # Wait for a key press and check if the 'q' key was pressed to quit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and destroy the window
capture.release()
cv2.destroyAllWindows()
