import os
import cv2
import time
import uuid

IMAGE_PATH = "CollectedImages"

labels = ['Hello', 'Yes', 'No', 'Thanks', 'IloveYou', 'Please']
number_of_images = 5 #defining how many images you want to collect for a particular variable

for label in labels:
    img_path = os.path.join(IMAGE_PATH, label)
    os.makedirs(img_path, exist_ok=True)

    # Open camera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print(f"Error: Could not open camera for label {label}")
        continue

    print(f"Collecting images for {label}")
    time.sleep(5)

    for imgnum in range(number_of_images):
        ret, frame = cap.read()
        if not ret:
            print(f"Error: Failed to capture image for {label} image number {imgnum}")
            continue

        imagename = os.path.join(img_path, f"{label}.{str(uuid.uuid1())}.jpg")
        cv2.imwrite(imagename, frame)
        cv2.imshow('frame', frame)
        time.sleep(10)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
