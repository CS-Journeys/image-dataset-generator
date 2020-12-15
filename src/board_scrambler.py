"""
# For this module, we'll be needing a super helpful Python library called "NumPy".
# NumPy makes working with multi-dimensional arrays/matrices much easier.
# NumPy arrays can store all kinds of data, including the pixel values of images
# (after all, an image is just a 2D array of pixels).
#
# see https://numpy.org/devdocs/user/quickstart.html to learn more about NumPy
"""

import numpy as np


def scramble_board(board_image):
    """
    Description:
        Function scrambles the pieces on a chessboard.
    Parameters:
        'board_image':
        N*N numpy array that represents a black & white image,
        each element in the 'board_image' array contains an integer (0-255 inclusive).
    Return:
        N*N integer numpy array (integer value between 0-255)
    Pre-condition:
        The input image ('board_image') is a square image of a chessboard.
        The chess pieces are in their starting positions.
    Process:
        NOTE: a chessboard is an 8x8 grid
        1. Crop a copy of the input image to an empty white tile and store the resulting image in a numpy array
        2. Crop a copy of the input image to an empty black tile and store the resulting image in a numpy array
        3. Select a random number of the 32 chess pieces (all of them, 2 kings and a few pawns, 1 knight, etc.)
        4. Copy the images of the selected pieces to the chessboard image at random locations
            WARNING: the chessboard tiles must retain the checkered pattern
                     Ex: the image of the black rook at H8 cannot be moved to H5 because H8's tile color is black but
                         H5's tile color is white. Copying the H8 black rook image to H5 will ruin the checkered pattern
        5. Set the remaining locations to empty tiles (use the numpy images from steps 1 and 2)
            WARNING: again, the checkered pattern must be conserved
        6. Return the scrambled chessboard image
    Example:
        See res/sample-board-scrambled.png
    """

    # TODO: scramble the chessboard
    return board_image
