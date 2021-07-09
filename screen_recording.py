import numpy as np
import cv2
# for windows, mac users
from PIL import ImageGrab



audio_data = b''
channel = -1
samplewidth = -1
framerate = -1

def scrn_rec():

    # four character code object for video writer
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    # video writer object
    out = cv2.VideoWriter("output.mp4", fourcc, 10.0, (1920,1080))

    while True:
        # capture computer screen
        img = ImageGrab.grab()
        # convert image to numpy array
        img_np = np.array(img)
        # convert color space from BGR to RGB
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        # show image on OpenCV frame
        cv2.imshow("Screen", frame)
        # write frame to video writer
        out.write(frame)

        if cv2.waitKey(1) == 27:
            break

    out.release()
    cv2.destroyAllWindows()


if __name__=='__main__':
    scrn_rec()
