import board, busio
from analogio import AnalogIn
from kmk.modules.analogin import AnalogInput, AnalogInputs
from kmk.modules.analogin.keys import AnalogKey

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC

analog = AnalogInputs(
  [
    AnalogInput(AnalogIn(board.GP5)), 
    AnalogInput(AnalogIn(board.GP7)),
    AnalogInput(AnalogIn(board.GP14)),
    AnalogInput(AnalogIn(board.GP27))
  ],
  [
    [AnalogKey(KC.X), AnalogKey(KC.Y)]
  ]
)

keyboard = KMKKeyboard()

keyboard.modules.append(analog)

_key_cfg = [
  board.GP4, board.GP1, board.GP3, board.GP2,
  board.GP26, board.GP6, board.GP13, board.GP9,
  board.GP14, board.GP11, board.GP12, board.GP10,
  board.GP29, board.GP0, board.GP8, board.GP28
]

class GamePad(KMKKeyboard):
  def __init__(self):
    self.matrix = KeysScanner(
      pins =_key_cfg,
    )

keyboard = GamePad()

keyboard.keymap = [
  [
    KC.X, KC.Y, KC.A, KC.B,
    KC.LSHIFT, KC.ENTER, KC.LCTRL, KC.ESC,
    KC.UP, KC.DOWN, KC.LEFT, KC.RIGHT,
    KC.L, KC.R, KC.MB_LMB, KC.MB_RMB
  ]
]

if __name__ == '__main__':
    keyboard.go()