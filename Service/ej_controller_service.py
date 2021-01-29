import time

from Domain.application_types import ApplicationTypes
from Domain.control_board_types import ControlBoardTypes
from Domain.hexapod_movement_types import HexapodMovementTypes
from Service.display_service import DisplayService
from Service.mqtt_service import MqttService
from Service.touch_keypad_service import TouchKeypadService


class EJControllerService(object):
    dp = DisplayService()
    mqtt = MqttService()
    control_board = TouchKeypadService()
    current_value = None
    current_topic = None
    application = None
    movement_topic = None
    method_topic = None

    def __init__(self):
        print("Init Controller")
        self.choose_application()
        time.sleep(2)
        self.dp.show_msg("Ready to move.")
        self.controller()

    def choose_application(self):
        self.dp.show_msg("Press + for Hexapod\nPress - for Robotarm")
        while True:
            value = self.control_board.get_key_press()
            if value == ControlBoardTypes.HEXAPOD or value == ControlBoardTypes.ROBOTARM:
                self.dp.show_msg("Thank you\nPreparing communication.")
                if value == ControlBoardTypes.HEXAPOD:
                    self.application = ApplicationTypes.HEXAPOD
                    self.movement_topic = self.mqtt.MQTT_TOPIC_HEXAPOD_MOVEMENT
                    self.method_topic = self.mqtt.MQTT_TOPIC_HEXAPOD_METHODE
                    self.mqtt.send_msg(self.method_topic, HexapodMovementTypes.TRIPOD_GAIT)
                else:
                    self.application = ApplicationTypes.ROBOTARM
                    self.movement_topic = self.mqtt.MQTT_TOPIC_ROBOTARM_MOVEMENT
                    self.method_topic = self.mqtt.MQTT_TOPIC_ROBOTARM_METHODE
                break
            else:
                self.dp.show_msg("Please choose again.")

    def controller(self):
        while True:
            value = self.control_board.get_key_press()
            if self.value_checker(value):
                if self.application == ApplicationTypes.HEXAPOD:
                    self.mqtt.send_msg(self.movement_topic, value.name)
                elif self.application == ApplicationTypes.ROBOTARM:
                    if value == ControlBoardTypes.RIGHT or value == ControlBoardTypes.LEFT:
                        self.mqtt.send_msg(self.current_topic, value.name)
                    elif value == ControlBoardTypes.UP or value == ControlBoardTypes.DOWN:
                        self.mqtt.send_msg(self.method_topic, value.name)
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
