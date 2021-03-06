import getpass

import paho.mqtt.client as mqtt

from Service.display_service import DisplayService


class MqttService(object):
    dp = DisplayService()
    client = mqtt.Client("edwin-jarvis-controller")
    MQTT_HOST = "10.0.0.109"
    MQTT_USERNAME = ""
    MQTT_PASSWORD = ""
    MQTT_TOPIC = "edwin/jarvis/set"
    MQTT_TOPIC_ROBOTARM_MOVEMENT = "edwin/jarvis/robotarm/movement/set"
    MQTT_TOPIC_ROBOTARM_METHODE = "edwin/jarvis/robotarm/movement/methode/set"
    MQTT_TOPIC_HEXAPOD_MOVEMENT = "edwin/jarvis/hexapod/movement/set"
    MQTT_TOPIC_HEXAPOD_METHODE = "edwin/jarvis/hexapod/movement/method/set"

    def __init__(self):
        print("init mqtt service")
        self.make_connection()

    def make_connection(self):
        self.enter_credentials()
        self.dp.show_msg("Making connection with mqtt service.")
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.username_pw_set(username=self.MQTT_USERNAME, password=self.MQTT_PASSWORD)
        self.client.connected_flag = False
        self.client.connect(self.MQTT_HOST, port=1883, keepalive=60, bind_address="")
        self.client.loop_start()  # loop_forever

    def enter_credentials(self):
        try:
            self.dp.show_msg("Enter username for the MQTT connection:")
            self.MQTT_USERNAME = input()
            self.dp.show_msg("Enter password for the MQTT connection:")
            self.MQTT_PASSWORD = getpass.getpass()
            self.dp.show_msg("Press y to confirm.")
            result = input()
            if not result.isdigit() and result.lower() != "y":
                self.dp.show_msg("Lets try that again..")
                self.enter_credentials()
        except ValueError:
            self.dp.show_msg("Wrong fucking input retard.")

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            self.client.connected_flag = True
            self.dp.show_msg("connected ok")
        else:
            self.dp.show_msg("Bad connection Returned code= ", rc)

    def on_message(self, client, userdata, message):
        print("TODO")

    def send_msg(self, topic, payload):
        self.client.publish(topic, payload)
