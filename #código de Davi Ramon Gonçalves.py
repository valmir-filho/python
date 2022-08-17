#código de Davi Ramon Gonçalves

import dht
import machine
import time
from conexaoInternet import conexao
import urequests

# atribui a leitura dos sensores a variaveis
temperatura = dht.DHT11(machine.Pin(4)) 
rele = machine.Pin(2,machine.Pin.OUT)

# o programa inicioa com o rele desligado
rele.value(0)


# inicia o monitoramento da temperatura e da umidade relativa do ar
while True:
    
    # variável que chama a função de leitura do DHT11
    temperatura.measure()
    
    # atribui os valores lidos a variáveis dentro laço
    temp = (temperatura.temperature())
    umid = (temperatura.humidity())
    
    #mostra na tela a temperatura e umidade relativa do ar em intervalos de 5 segundos
    print ("temperatura: {}º, Umidade: {}%".format (temp, umid))
    time.sleep(2)
    
    # se a temperatura atingir >31º ou a umidade ultrapasr 70% acende o led
    if temp > 31 or umid > 70:
        rele.value(1)
        
    # caso nenhuma das condições seja atingida, o led continua desligado
    else:
        rele.value(0)
        
        
    #conecta ao wifi 
    station = conecta("Martiaco Industria", "$Up3rNOVA")
    if not station.isconnected():
        print("Não conectado!...")
    else:
        #acessa o site do ThingSpeak e envia os dados lidos pelo sensor. 
        print("Acessando o ThingSpeak...")
        response = urequests.get("https://api.thingspeak.com/update?api_key=VASQJ2UP4CJB19R9&field1={}&field2={}".format(temp,umid))
        print("Dados enviados com sucesso!")
        print(response.text)
        station.disconnect()
        time.sleep(2)
