# import cv2 to capture videofeed
import cv2
import numpy as np

# attach camera indexed as 0
camera = cv2.VideoCapture(1)

bg = 0

# setting framewidth and frameheight as 640 X 480
camera.set(3 , 640)
camera.set(4 , 480)

# loading the mountain image
img = cv2.imread('mount everest.jpeg')

# resizing the mountain image as 640 X 480
img = img.resize((640,480))

while True:

    # read a frame from the attached camera
    status , frame = camera.read()

    # if we got the frame successfully
    if status:

        # flip it
        frame = cv2.flip(frame , 1)

        # converting the image to RGB for easy processing
        frame_rgb = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
        # creating thresholds
        lower_bound = np.array([100, 100, 100])
        upper_bound = np.array([255, 255, 255])
        # thresholding image
        mask_1 = cv2.inRange(frame_rgb, lower_bound, upper_bound)
        # inverting the mask
        bg = np.flip(bg)
        # bitwise and operation to extract foreground / person
        mask_2 = cv2.bitwise_not(mask_1)
        res_1 = cv2.bitwise_and(img, img, mask = mask_2)
        res_2 = cv2.bitwise_and(bg, bg, mask = mask_1)
        # final image
        final_output = cv2.addWeighted(res_1, 1, res_2, 1, 0)
        # show it
        cv2.imshow('frame' , frame)

        # wait of 1ms before displaying another frame
        code = cv2.waitKey(1)
        if code  ==  32:
            break

# release the camera and close all opened windows
camera.release()
cv2.destroyAllWindows()
