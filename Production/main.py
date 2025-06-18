import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()
media = MediaKeys()
keyboard.extensions.append(media)

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

PINS = [
    board.D11,
    board.D9,
    board.D10,
    board.D8,
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        KC.LCTRL(KC.V),
        KC.LCTRL(KC.C),
        KC.LCTRL(KC.Y),
        KC.LWIN(KC.LSHIFT(KC.S)),
    ]
]

encoder_handler.pins = (
    (board.D1, board.D2, None),
    (board.D3, board.D4, None),
)

encoder_handler.map = [
    ((KC.MEDIA_VOL_UP, KC.MEDIA_VOL_DOWN, None),
    (KC.MEDIA_BRIGHTNESS_UP, KC.MEDIA_BRIGHTNESS_DOWN, None)),
]

if __name__ == '__main__':
    keyboard.go()