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




results = []

start = time.time()

while (time.time() - start) < 1:
    results.append(ADC.ADS1256_GetChannalValue(3))
        
        
print(len(results))
print(results)


print(time.time()-start)
print(results)

       




