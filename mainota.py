# More details can be found in TechToTinker.blogspot.com 
# George Bantique | tech.to.tinker@gmail.com
import machine
import utime
from machine import UART, Pin, Timer
from utime import sleep_ms, sleep
from picodfplayer import DFPlayer
from mfrc522 import MFRC522
from array import *
from ir_rx.nec import NEC_16
from ir_rx.print_error import print_error
from micropython import const
from WifiConfig import SSID, PASSWORD

print(f"{SSID}, {PASSWORD}")

################################################################
# turn off all button leds
################################################################
def BtnLedOff():
    for i in range(4):
        BtnArr[i].value(0)

################################################################
# turn one LED on
################################################################
def BtnLedOne(idx):
    BtnLedOff()
    j = (idx-1) % 4
    BtnArr[j].value(1)


####################################################################
# End of Subroutine Section
####################################################################


######################################################################
# Keys and Key Led
######################################################################
BTN1     = 10
BTN2     = 11
BTN3     = 12
BTN4     = 13
BTNLED1  = 6
BTNLED2  = 7
BTNLED3  = 14
BTNLED4  = 15
Btn1 = Pin(BTN1, Pin.IN, Pin.PULL_UP)
Btn2 = Pin(BTN2, Pin.IN, Pin.PULL_UP)
Btn3 = Pin(BTN3, Pin.IN, Pin.PULL_UP)
Btn4 = Pin(BTN4, Pin.IN, Pin.PULL_UP)
BtnLed1  = Pin(BTNLED1, Pin.OUT)
BtnLed2  = Pin(BTNLED2, Pin.OUT)
BtnLed3  = Pin(BTNLED3, Pin.OUT)
BtnLed4  = Pin(BTNLED4, Pin.OUT)
BtnArr   = [BtnLed1, BtnLed2, BtnLed3, BtnLed4]
BtnState = [0,1,1,1,1]

# init key LED to OFF
BtnLedOff()
  

nn = 0
while True:
    nn = (nn + 1) % 2
    BtnArr[3].value(nn)
    utime.sleep_ms(500)

  

