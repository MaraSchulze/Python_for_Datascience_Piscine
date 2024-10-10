import numpy as np
import matplotlib.pyplot as plt


def display_image(image: np.ndarray, greyscale=False) -> None:
    """
    Displays the zoom with plt.
    """
    if greyscale is False:
        plt.imshow(image)
    else:
        plt.imshow(image, cmap='gray')
    plt.show()


def ft_invert(array) -> np.ndarray:
    """
    Inverts the image.
    """
    inversed_image = [[[255 - r, 255 - g, 255 - b]
                      for r, g, b in row] for row in array]
    display_image(inversed_image)
    return inversed_image


def ft_red(array) -> np.ndarray:
    """
    Returns the red channel.
    """
    red_image = [[[r, 0, 0] for r, g, b in row] for row in array]
    display_image(red_image)
    return red_image


def ft_green(array) -> np.ndarray:
    """
    Returns the green channel.
    """
    green_image = [[[0, g, 0] for r, g, b in row] for row in array]
    display_image(green_image)
    return green_image


def ft_blue(array) -> np.ndarray:
    """
    Returns the blue channel.
    """
    blue_image = [[[0, 0, b] for r, g, b in row] for row in array]
    display_image(blue_image)
    return blue_image


def ft_grey(array) -> np.ndarray:
    """
    Returns greyscale.
    """
    grey_image = [[[r / 3.3444816053511705 + g / 1.7035775127768313 + b /
                    8.771929824561404] for r, g, b in row] for row in array]
    display_image(grey_image, greyscale=True)
    return grey_image
