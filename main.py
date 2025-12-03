import paho.mqtt.client as mqtt
import paho.mqtt.enums as en
from SensorFactory import SensorFactory
import keyboard
import time
import json


if __name__ == "__main__":
    

    # create the sensor objects
    factory = SensorFactory()
    
    temp_sensor = factory.get_temperaterature_sensor()

    power_sensor = factory.get_temperaterature_sensor()

    
    client = mqtt.Client(en.CallbackAPIVersion.VERSION2)
    client.connect("broker.hivemq.com", 1883, 60)
    client.loop_start()

    while not keyboard.is_pressed('q'):
        
        temp_data = temp_sensor.get_data()
        if not len(temp_data) == 0:

            client.publish('MST/Solution/Temperature', json.dumps({'data': temp_data}))
        power_data = power_sensor.get_data()
        if not len(power_data) == 0:
            
            client.publish('MST/Solution/Power', json.dumps({'data': power_data}))
        time.sleep(.1)
    
    client.loop_stop()
    client.disconnect()

       
            
