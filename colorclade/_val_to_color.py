import colorsys
import random
import typing


def val_to_color(
    val: typing.Any,
    salt: typing.Optional[int] = None,
    saturation: float = 1.0,
    brightness: float = 0.5,
) -> typing.Tuple[int, int, int]:
    # Convert the hash to a value between 0 and 1
    rand = random.Random()
    rand.seed(str(val) + str(salt))
    hue = rand.random()

    # Convert the HSV color to an RGB color
    rgb_color = colorsys.hsv_to_rgb(hue, saturation, brightness)

    # Convert RGB values into 0-255 range (suitable for use in digital color)
    rgb_color_255 = tuple(int(c * 255) for c in rgb_color)

    return rgb_color_255
