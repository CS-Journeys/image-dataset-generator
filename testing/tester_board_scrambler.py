"""
# This unit tester requires OpenCV (cv2) and scikit-image (skimage).
# OpenCV and scikit-image are libraries that helps us work with images.
"""
import cv2
import skimage.transform

from src.board_scrambler import *

# Scale at which to display images
# Set value to whatever you like
DISPLAY_SCALE = 0.5

# Load the starting position image of a chessboard
board_start_image = cv2.imread('../res/sample-board-starting-position.png', 0)

# Display the starting position image to the screen
# Press any key to continue
cv2.imshow('starting position', skimage.transform.rescale(board_start_image, DISPLAY_SCALE, anti_aliasing=True))
cv2.waitKey(0)
cv2.destroyAllWindows()

# Run the function
scrambled_image = scramble_board(board_start_image)

# Display the results
# Press any key to continue
cv2.imshow('scrambled', skimage.transform.rescale(scrambled_image, DISPLAY_SCALE, anti_aliasing=True))
cv2.waitKey(0)
cv2.destroyAllWindows()
