import sctp
import time

client = sctp.Client()
client.connect('127.0.0.1', 55770, login='user', password='passwd')
time.sleep(1)
client.disconnect()
