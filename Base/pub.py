import random
import time

from paho.mqtt import client as mqtt_client


broker = 'localhost'
port = 1883
topic = "EMA/mqtt"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Conectado ao Broker!")
        else:
            print("Conexão falhou, códico: %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"Mensagem {msg_count}"
        result = client.publish(topic, msg)
        result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Enviando mensagem `{msg}` para o tópico `{topic}`.")
        else:
            print(f"O envio da mensagem para o tópico {topic} falhou.")
        msg_count += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()
