#!/usr/bin/python
# -*- coding:utf-8 -*-
import config
import time
import ADS1256
import numpy

import RPi.GPIO as GPIO
import sys
from time import perf_counter
from datetime import datetime
from scipy.io.wavfile import write
import ss11 as audplot

def compute(buf):
    read = (buf[0]<<16) & 0xff0000
    read |= (buf[1]<<8) & 0xff00
    read |= (buf[2]) & 0xff
    if (read & 0x800000):
        read &= 0xF000000
    return read


def record_audio(file_name):
    ADC = ADS1256.ADS1256()
    ADC.ADS1256_init()
    samplerate = 3000
    
    raw_results = []
    results = []

    ADC.ADS1256_SetChannal(3)

    start = time.time()
    while (time.time() - start) < 5:
        ADC.ADS1256_WaitDRDY()
        config.digital_write(ADC.cs_pin, GPIO.LOW)#cs  0
        config.spi_writebyte([ADS1256.CMD['CMD_RDATA']])
        buf = config.spi_readbytes(3)
        config.digital_write(ADC.cs_pin, GPIO.HIGH)
        raw_results.append(buf)

    processed_results = [compute(buf) for buf in raw_results]
    data1=numpy.array(processed_results)

    write(file_name, 4050, data1.astype('int16'))
    print(f"Total Time taken to read {len(processed_results)} sample: " + str(time.time()-start))

while True:
    exe_datetime = datetime.now().strftime('%Y%m%d%H%M%S')
    file_name = f'recorded_audio/sound_{exe_datetime}.wav'
    record_audio(file_name)
    audplot.plot_audio(file_name)