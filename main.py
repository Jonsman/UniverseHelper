import cv2
from mss import mss
import numpy as np
import keyboard

class Main():
    def __init__(self):
        self.sct = mss()

        # Set the capture device
        self.capture_device = self.sct.monitors[0]

        # Load the healthbar template
        self.healthbar_template = cv2.imread('.\pictures\health_bar.png', cv2.IMREAD_COLOR)

        # Load the buff template
        self.buff_template = cv2.imread('.\pictures\\buff_haste.png', cv2.IMREAD_COLOR)

    def main(self):
        while(True):

            self.healthbar = self.detectHealthbar(self.healthbar_template)
            self.healPlayer(self.healthbar[0])

            if self.healthbar[0] > 0.98:
                self.buffs = self.detectBuffs(self.buff_template)
                self.buffPlayer(self.buffs)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break

    def detectHealthbar(self, template):
        # Capture screenshot
        screenshot = self.sct.grab(self.capture_device)
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGBA2RGB)

        # Convert screenshot to grayscale
        #screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

        # Perform template matching
        res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)

        # Find the location of the best match
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # Draw a rectangle around the matched area
        #top_left = max_loc
        #bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])
        #cv2.rectangle(screenshot, top_left, bottom_right, (0, 255, 0), 2)

        # Display the image
        #cv2.imshow('Screen Capture', screenshot)

        # Return the max value of the template matching
        return max_val, max_loc

    def detectBuffs(self, template):
        # Capture screenshot
        dimenson = {'top': self.healthbar[1][1] + 30, 'left': (self.healthbar[1][0] - 50), 'width': 230, 'height': 55}
        screenshot = self.sct.grab(dimenson)
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGBA2RGB)

        # Convert screenshot to grayscale
        #screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

        # Perform template matching
        res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)

        # Find the location of the best match
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # Draw a rectangle around the matched area
        #top_left = max_loc
        #bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])
        #cv2.rectangle(screenshot, top_left, bottom_right, (0, 255, 0), 2)

        # Display the image
        #cv2.imshow('Screen Capture', screenshot)

        # Return the max value of the template matching
        return max_val

    def healPlayer(self, confidence):
        if 0.73 < confidence < 0.96:
            keyboard.press_and_release('2')
            #print('Healing! ' + str(confidence))
        else:
            pass

    def buffPlayer(self, confidence):
        if confidence < 0.9:
            keyboard.press_and_release('c')
            #print('Buffing! ' + str(confidence))
        else:
            pass


program = Main()
program.main()