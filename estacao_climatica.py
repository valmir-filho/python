import dht
import machine
import network
import time
from conexao_internet import conexao
import urequests

d = dht.DHT11(machine.Pin(4))
r = machine.Pin(2, machine.Pin.OUT)
r.value(0)
contadorIf = contadorElse = 0

while True:
    d.measure()
    temperatura = (d.temperature())
    umidade = (d.humidity())
    print("Aluno: Valmir Moro Conque Filho")
    print("Turma: EAD ADS 2022 - Verão")
    print("Disciplina: IOT - Professor: Edson Kageyama")
    print()
    print("Estação Climática PUCPR")
    print()
    print("A temperatura atual é: {}°C.".format(d.temperature()))
    print("A umidade relativa do ar atual é: {}%.".format(d.humidity()))
    print()
    if d.temperature() > 31 or d.humidity() > 70:
        contadorIf += 1
        r.value(1)
        print("Relé ligado.")
        print()
        print("Número de impressões no console: {}.".format(contadorIf))
        contadorElse = 0
    else:
        contadorElse += 1    
        print("Condições para acionamento do relé: temperatura > 31 °C e umidade relativa do ar > 70%.")
        print()
        print("Relé desligado.")
        print()
        print("Número de impressões no console: {}.".format(contadorElse))
        print()
        contadorIf = 0

print("Conectando com a rede WIFI...")
station = conexao("Martiaco Industria", "$Up3rNOVA")
if not station.isconnected():
    print("Erro de conexão com a rede WIFI! Tente novamente.")
    print()
else:
    print("Conexão com a rede WIFI realizada com sucesso!")
    print()
    print("Acessando a plataforma ThingSpeak...")
    response = urequests.get("https://api.thingspeak.com/update?api_key=VASQJ2UP4CJB19R9&field1={}&field2={}".format(temperatura, umidade))
    print("Acesso a plataforma ThingSpeak realizada com sucesso!")
    print("Enviando os dados...")
    print(response.text)
    station.disconnect()
    time.sleep(2)
