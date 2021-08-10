def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    r, g, b = rgb

    boundaries = range(0, 256)
    if r not in boundaries or g not in boundaries or b not in boundaries:
        raise ValueError

    return f'#{r:02X}{g:02X}{b:02X}'
