
# Author: ajanthan

import datetime
import time
import ADS1256
import Adafruit_DHT

import model



data = model.DHTData()
ADC = ADS1256.ADS1256()
ADC.ADS1256_init()

data.define_sensor('MAX4466-1', ADC.ADS1256_init(), 3)
data.define_sensor('MAX4466-2', ADC.ADS1256_init(), 4)

# Main loop to take sensor readings every two seconds.
try:
    while True:
        # Get the current time for this batch of sensor readings.
        reading_time = datetime.datetime.now()
        # Go through each sensor and get its current reading.
        for sensor in data.get_sensors():

            ADC_value = ADC.ADS1256_GetChannalValue(3)
            ADC_value2 = ADC.ADS1256_GetChannalValue(4)
            print(ADC_value)


            data.add_reading(time=reading_time, name='ADC Sound Value', value=ADC_value)
            data.add_reading(time=reading_time, name='ADC2 Sound Value', value=ADC_value2)
        # Wait 2 seconds and repeat.
        time.sleep(0.5)
finally:
    # Finally close the connection to the database when done.
    data.close()
