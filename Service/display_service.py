import time

import Adafruit_CharLCD as LCD

lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 4
lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
lcd.message('Init display')
time.sleep(1)
lcd.clear()
lcd.show_cursor(True)


def show_msg(msg):
    lcd.show_cursor(False)
    lcd.clear()
    if len(msg) > 15:
        show_long_msg(msg)
    else:
        lcd.message(msg)


def show_long_msg(message):
    lcd.message(message)
    for i in range(lcd_columns - len(message)):
        time.sleep(0.5)
        lcd.move_right()
    for i in range(lcd_columns - len(message)):
        time.sleep(0.5)
        lcd.move_left()
