
import cv2

# Initialize video capture (0 = webcam, or use 'video.mp4' for file)
cap = cv2.VideoCapture(0)

# Read the first frame
ret, frame1 = cap.read()
gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
gray1 = cv2.GaussianBlur(gray1, (21, 21), 0)

while True:
    ret, frame2 = cap.read()
    if not ret:
        break

    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.GaussianBlur(gray2, (21, 21), 0)

    # Compute absolute difference
    diff = cv2.absdiff(gray1, gray2)

    # Apply thresholding
    _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

    # Dilate to fill in holes, making contours clearer
    dilated = cv2.dilate(thresh, None, iterations=2)

    # Find contours from thresholded image
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 500:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame2, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display result
    cv2.imshow("Motion Detection", frame2)

    # Update reference frame
    gray1 = gray2

    # Break with 'q' key
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
