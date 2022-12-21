import time
import board
import adafruit_dht

def temperatura_umidade(sala):
    if(sala=='1' or sala=='3'):
        dhtDevice = adafruit_dht.DHT22(board.D4)
    else:
        dhtDevice = adafruit_dht.DHT22(board.D18)
    while True:
        try:
            temperature_c = dhtDevice.temperature
            temperature_f = temperature_c * (9 / 5) + 32
            humidity = dhtDevice.humidity
            print(
                "Temperatura: {:.1f} F / {:.1f} C    Umidade: {}% ".format(
                    temperature_f, temperature_c, humidity
                )
            )
            break

        except RuntimeError as error:
            print(error.args[0])
            time.sleep(2.0)
            continue
        except Exception as error:
            dhtDevice.exit()
            raise error

        time.sleep(2.0)