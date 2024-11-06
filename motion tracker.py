import cv2

# Open the default camera (index 0)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to the grayscale frame
    blurred = cv2.GaussianBlur(gray, (21, 21), 0)

    # Calculate the difference between the current frame and the previous frame
    if 'prev_frame' not in locals():
        prev_frame = blurred
    diff = cv2.absdiff(prev_frame, blurred)

    # Update the previous frame
    prev_frame = blurred

    # Threshold the difference to highlight the motion
    thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)[1]

    # Dilate the thresholded image to fill in holes
    dilated = cv2.dilate(thresh, None, iterations=2)

    # Find contours in the dilated image
    contours, _ = cv2.findContours(
        dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    # Iterate over the contours
    for contour in contours:
        # Calculate the area of the contour
        area = cv2.contourArea(contour)

        # Ignore small contours
        if area < 700:
            continue

        # Draw a rectangle around the contour
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('Motion Tracker', frame)

    # Exit on key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
