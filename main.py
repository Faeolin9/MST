
from .Sensors import SensorFactory
import keyboard


if __name__ == "__main__":
    

    # create the sensor objects
    factory = SensorFactory()
    
    temp_sensor = factory.get_temperaterature_sensor()

    power_sensor = factory.get_temperaterature_sensor()


    while not keyboard.is_pressed('q'):
        # read new data from the sensors
        pass

        # publish data to the broker
    
    
