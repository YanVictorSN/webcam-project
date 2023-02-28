import cv2
import numpy as np
import matplotlib.pyplot as plt

# Access the primary WebCam
video = cv2.VideoCapture(0)
while True:
    # Read the WebCam
    connected, frame = video.read()
    # Show the WebCam on the screen
    cv2.imshow("WebCam", frame)
    # Define the "q" key to exit the WebCam
    if cv2.waitKey(1) == ord("q"):
        break
    # Define the "p" key to take a picture.
    elif cv2.waitKey(1) == ord("p"):
        # Save the captured image from the WebCam
        cv2.imwrite("image.jpg", frame)
        break

# Release the WebCam
video.release()

# Read the saved image.
img = cv2.imread("image.jpg")

# Convert the image to grayscale.
imgGray = np.array(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))

# Save the grayscale image.
cv2.imwrite("imageCinza.jpg", imgGray)

# Set the figure size.
plt.figure(figsize=(4, 4))

# Set the title.
plt.title(f"Grayscale Image")

# Show the image on the screen.
plt.imshow(imgGray)
plt.show()

print(cv2.__version__)
