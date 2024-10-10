from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Loads an image and prints out the shape.
    """

    # Open image
    try:
        image = Image.open(path)
    except Exception as e:
        print("Error: Could not open image:", e)
        exit()

    # Convert to array
    arr = np.array(image)

    # Print out shape
    print("The shape of image is: ", arr.shape)

    return arr
