from ds3231 import *
from machine import I2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from time import sleep

I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

# Create an instance of the DS3231 class for interfacing with the DS3231 RTC
ds = DS3231(i2c)

# Set the DS3231 RTC to current system time
ds.set_time()

while True:
    # Get the current time from the DS3231 RTC
    time_data = ds.get_time()

    # Extract the date and time components
    year = time_data[0]
    month = time_data[1]
    day = time_data[2]
    hour = time_data[3]
    minute = time_data[4]
    second = time_data[5]

    # Format date and time components with leading zeros
    date_str = "{:02d}/{:02d}/{:04d}".format(month, day, year)
    time_str = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)

    # Display formatted date and time on the LCD
    lcd.putstr("Date={}\nTime={}".format(date_str, time_str))
    
    sleep(1)
    lcd.clear()