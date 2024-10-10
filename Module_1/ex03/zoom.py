from load_image import ft_load
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def display_image(image: np.ndarray) -> None:
    """
    Displays the zoom with plt.
    """
    plt.imshow(image, cmap="gray")
    plt.show()


def main():
    """
    Loads 'animal.jpg', prints information and displays it after zooming.
    """
    # Prints shape and pixels
    print(ft_load("animal.jpeg"))

    # Open image
    try:
        image = Image.open("animal.jpeg")
    except Exception as e:
        print("Error: Could not open image:", e)
        exit()

    # Convert to array and greyscale
    arr = np.array(image.convert("L"))

    # Slice (zoom) and print out the new pixel content
    arr = arr[100:500, 450:850]
    print("New shape after slicing: " + str(arr.shape))
    print(arr)

    display_image(arr)


if __name__ == "__main__":
    main()
