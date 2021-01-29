import time

import Adafruit_CharLCD as LCD


def singleton(cls):
    instances = {}

    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return get_instance


@singleton
class DisplayService(object):
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

    def show_msg(self, msg):
        self.lcd.show_cursor(False)
        self.lcd.clear()
        message = msg.split('\n')
        if len(message) > 1:
            if len(message[0]) > 15 or len(message[1]) > 15:
                self.show_long_msg(msg)
            else:
                self.lcd.message(msg)
        else:
            self.lcd.message(msg)

    def show_long_msg(self, message):
        self.lcd.message(message)
        for i in range(self.lcd_columns - len(message)):
            time.sleep(0.5)
            self.lcd.move_right()
        for i in range(self.lcd_columns - len(message)):
            time.sleep(0.5)
            self.lcd.move_left()
