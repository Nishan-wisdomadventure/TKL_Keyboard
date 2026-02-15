import board
import busio
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers

# I2C bus (shared for both displays)
i2c = busio.I2C(board.GP26, board.GP27, frequency=400_000)

# SSD1306 (0x3C, assume 128x64)
display_bus1 = displayio.I2CDisplay(i2c, device_address=0x3C)
oled1 = adafruit_displayio_ssd1306.SSD1306(display_bus1, width=128, height=64)

# SSD1309 (0x3D, assume 128x64) 
display_bus2 = displayio.I2CDisplay(i2c, device_address=0x3D)
oled2 = adafruit_displayio_ssd1306.SSD1306(display_bus2, width=128, height=64)

# Show "Your Name" on both OLEDs
splash1 = displayio.Group(max_size=10)
text1 = label.Label(terminalio.FONT, text="Your Name", color=0xFFFFFF, x=20, y=35)
splash1.append(text1)
oled1.show(splash1)

splash2 = displayio.Group(max_size=10)
text2 = label.Label(terminalio.FONT, text="Your Name", color=0xFFFFFF, x=20, y=35)
splash2.append(text2)
oled2.show(splash2)

# CORRECTED MATRIX: 17 cols (GP0-16) x 6 rows (GP17-22)
keyboard = KMKKeyboard()

# 17 COLUMN PINS: GP0 through GP16
keyboard.col_pins = (
    board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5,
    board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11,
    board.GP12, board.GP13, board.GP14, board.GP15, board.GP16
)

# 6 ROW PINS: GP17-22
keyboard.row_pins = (board.GP17, board.GP18, board.GP19, board.GP20, board.GP21, board.GP22)
keyboard.diode_orientation = DiodeOrientation.COL2ROW  # Test both directions

# 102-key keymap (17x6) - basic layout, customize as needed
keyboard.keymap = [
    # Row 1 (17 keys): Esc + numbers row + F-keys + extras
    [KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.PRNT, KC.PSCR, KC.PAUS, KC.BSPC],
    
    # Row 2: Tab + QWERTY row
    [KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLS, KC.N1, KC.N2, KC.N3],
    
    # Row 3: Caps + ASDF row
    [KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.N0, KC.N4, KC.N5, KC.N6, KC.N7],
    
    # Row 4: Shift + ZXCV row
    [KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT, KC.N8, KC.N9, KC.MINS, KC.EQUALS, KC.ENT],
    
    # Row 5: Ctrl/Alt/Space + modifiers
    [KC.LCTL, KC.LGUI, KC.LALT, KC.SPC, KC.SPC, KC.SPC, KC.SPC, KC.RALT, KC.RGUI, KC.RCTL, KC.LEFT, KC.DOWN, KC.UP, KC.RGHT, KC.NO, KC.NO, KC.NO],
    
    # Row 6: Arrows + numpad/media
    [KC.NO, KC.HOME, KC.PGDN, KC.PGUP, KC.END, KC.INS, KC.DEL, KC.VOLU, KC.VOLD, KC.MUTE, KC.MPLY, KC.MPRV, KC.MNXT, KC.NO, KC.NO, KC.NO, KC.NO]
]

keyboard.modules = [Layers]

if __name__ == '__main__':
    keyboard.go()
