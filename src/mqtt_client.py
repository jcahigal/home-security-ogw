import paho.mqtt.client as mqtt

# Define the MQTT client
client = mqtt.Client()
# Connect to the MQTT broker
# client.connect("mqtt.eclipse.org", 1883, 60)
# TODO up a mosquitto MQTT broker on the local machine

def notify_someone_is_at_home():
    # Publish a message to a topic
    client.publish("at_home", "Someone is at home")

def notify_all_outdoors():
    # Publish a message to a topic
    client.publish("all_outdoors", "Nobody is at home")
