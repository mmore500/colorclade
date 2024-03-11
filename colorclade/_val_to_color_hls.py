import random
import seaborn as sns
import typing


def val_to_color_hls(
    val: typing.Any,
    salt: typing.Optional[int] = None,
) -> typing.Tuple[int, int, int]:
    # Convert the hash to a value between 0 and 1
    rand = random.Random()
    rand.seed(str(val) + str(salt))
    rgb_color = rand.choice(sns.hls_palette(1024))

    # Convert RGB values into 0-255 range (suitable for use in digital color)
    rgb_color_255 = tuple(int(c * 255) for c in rgb_color)

    return rgb_color_255
