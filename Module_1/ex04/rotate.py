import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def transpose(arr):
    """
    Transposes the array
    """
    for j in range(len(arr)):
        for i in range(j + 1, len(arr[0])):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    return arr


def display_image(image: np.ndarray) -> None:
    """
    Displays the zoom with plt.
    """
    plt.imshow(image, cmap="gray")
    plt.show()


def main():
    """
    Loads 'animal.jpg', cuts it, prints information, transposes it,
    and displays it.
    """

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
    print("The shape of the image is: " + str(arr.shape))
    print(arr)

    # Transpose
    arr = transpose(arr)

    print("New shape after transpose: " + str(arr.shape))
    print(arr)

    # Display transpose
    display_image(arr)


if __name__ == "__main__":
    main()
