from Domain.control_board_types_enum import ControlBoardTypes
from Service.mqtt_service import MqttService
from Service.touch_keypad import ControlBoard


class EdwinJarvisController(object):
    mqtt = MqttService()
    control_board = ControlBoard()

    def controller(self):
        value = self.control_board.keypad_input()
        print(value)
        while True:
            if value == ControlBoardTypes.RIGHT or value == ControlBoardTypes.LEFT:
                self.mqtt.send_msg(self.mqtt.MQTT_TOPIC_BASE, value.name)
            elif value == ControlBoardTypes.UP or value == ControlBoardTypes.DOWN:
                self.mqtt.send_msg(self.mqtt.MQTT_TOPIC_FIRST_AXIS, value.name)
            else:
                self.mqtt.send_msg(self.mqtt.MQTT_TOPIC, value.name)


if __name__ == "__main__":
    print("Init Edwin jarvis controller")
    edwin = EdwinJarvisController()
    edwin.controller()
