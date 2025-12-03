from Sensor import Sensor



class SensorFactory:

    @staticmethod
    def get_temperaterature_sensor():

        return Sensor('temperature', 20, 80, 42)

    
    @staticmethod
    def get_power_sensor():
        return Sensor('power', 0, 5, 1337)
