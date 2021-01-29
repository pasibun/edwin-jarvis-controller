from Domain.control_board_types import ControlBoardTypes
from Service.mqtt_service import MqttService
from Service.touch_keypad import ControlBoard


class EdwinJarvisController(object):
    mqtt = MqttService()
    control_board = ControlBoard()
    current_value = None
    current_topic = None

    def controller(self):
        while True:
            value = self.control_board.get_key_press()
            if self.value_checker(value):
                if value == ControlBoardTypes.RIGHT or value == ControlBoardTypes.LEFT:
                    self.current_topic = self.mqtt.MQTT_TOPIC_BASE
                    self.mqtt.send_msg(self.mqtt.MQTT_TOPIC_BASE, value.name)
                elif value == ControlBoardTypes.UP or value == ControlBoardTypes.DOWN:
                    self.current_topic = self.mqtt.MQTT_TOPIC_FIRST_AXIS
                    self.mqtt.send_msg(self.mqtt.MQTT_TOPIC_FIRST_AXIS, value.name)
            elif self.current_topic is not None and value is None:
                print('button release.')
                self.mqtt.send_msg(self.mqtt.MQTT_TOPIC, ControlBoardTypes.DONE.name)
                self.current_value = None
                self.current_topic = None

    def value_checker(self, value):
        if value is not None and value is not self.current_value:
            print('pressed value: ', value)
            self.current_value = value
            return True
        else:
            return False
