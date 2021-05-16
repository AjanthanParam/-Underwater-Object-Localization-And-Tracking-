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

# Reading one sample 
start = time.time()
ADC.ADS1256_GetChannalValue(3)
print("Time taken to read on sample: " + str(time.time() - start))


results = []
start = time.time()

duration = 1

while (time.time() - start) < duration:
    results.append(ADC.ADS1256_GetChannalValue(3))
  
print(f"Total Time taken to read {len(results)} sample: " + str(time.time()-start))
print(f"Total samples read in {duration} second: " + str(len(results)))








