#!/usr/bin/python
# -*- coding:utf-8 -*-
import config
import time
import ADS1256

import RPi.GPIO as GPIO
import sys
from time import perf_counter


ADC = ADS1256.ADS1256()

ADC.ADS1256_init()




raw_results = []
results = []


ADC.ADS1256_SetChannal(3)

start = time.time()
while (time.time() - start) < 1:
        ADC.ADS1256_WaitDRDY()
        config.digital_write(ADC.cs_pin, GPIO.LOW)#cs  0
        config.spi_writebyte([ADS1256.CMD['CMD_RDATA']])
        buf = config.spi_readbytes(3)
        config.digital_write(ADC.cs_pin, GPIO.HIGH)
        
        raw_results.append(buf)
        


print(len(raw_results))
print(f"Total Time taken to read {len(raw_results)} sample: " + str(time.time()-start))

def compute(buf):
    read = (buf[0]<<16) & 0xff0000
    read |= (buf[1]<<8) & 0xff00
    read |= (buf[2]) & 0xff
    if (read & 0x800000):
        read &= 0xF000000
    return read


       



