import getpass

import paho.mqtt.client as mqtt


class MqttService(object):
    client = mqtt.Client("edwin-jarvis-controller")
    MQTT_HOST = "10.0.0.109"
    MQTT_USERNAME = ""
    MQTT_PASSWORD = ""
    MQTT_TOPIC = "edwin/jarvis/set"
    MQTT_TOPIC_BASE = "edwin/jarvis/control/base/set"
    MQTT_TOPIC_FIRST_AXIS = "edwin/jarvis/control/first/axis/set"

    def __init__(self):
        print("init mqtt service")
        self.make_connection()

    def make_connection(self):
        self.enter_credentials()
        print("Making connection with mqtt service.")
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.username_pw_set(username=self.MQTT_USERNAME, password=self.MQTT_PASSWORD)
        self.client.connected_flag = False
        self.client.connect(self.MQTT_HOST, port=1883, keepalive=60, bind_address="")
        self.client.loop_start()  # loop_forever

    def enter_credentials(self):
        try:
            print("Enter username for the MQTT connection:")
            self.MQTT_USERNAME = input()
            print("Enter password for the MQTT connection:")
            self.MQTT_PASSWORD = getpass.getpass()
            print("Press y to confirm.")
            result = input()
            if not result.isdigit() and result.lower() != "y":
                print("Lets try that again..")
                self.enter_credentials()
        except ValueError:
            print("Wrong fucking input retard.")

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            self.client.connected_flag = True
            print("connected ok")
        else:
            print("Bad connection Returned code= ", rc)

    def on_message(self, client, userdata, message):
        print("TODO")

    def send_msg(self, topic, payload):
        self.client.publish(topic, payload)
