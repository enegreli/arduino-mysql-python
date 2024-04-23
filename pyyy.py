import serial 
import mysql. connector
from pynput import keyboard

# Conecta ao banco de dados MySQL
db = mysql. connector.connect(
    host="localhost", # Normalmente, o XAMPP usa 'localhost'
    user="root", # Usuário padrão do XAMPP
    passwd="'", # Senha padrão do XAMPP é vazia
    database="ClimaWeb" # Nome do banco de dados
)

# Prepara um cursor para executar operações no banco de dados
cursor = db. cursor ()

# Conecta à porta serial onde o Arduino está conectado
arduino = serial.Serial('COM3', 9600, timeout=1) # Substitua 'COM3' pela sua porta

def on_press(key): # Função chamada sempre que uma tecla é pressionada
    try:
        if key == keyboard.Key.esc:
            return False # Se a tecla Esc for pressionada, encerra o listener
    except AttributeError:
        pass

# Cria um listener para monitorar as teclas pressionadas
listener = keyboard. Listener(on_press=on_press)
listener .start()

try:
    while True:
        # Lê a umidade e temperatura do serial
        umidade = float(arduino.readline().decode('utf-8').rstrip())
        temperatura.float(arduino.realine().decode('utf-8').rstrip())
        
        # Query SQL para inserção dos dados
        query = "INSERT INTO DadosClimaticos (temperatura, umidade) VALUES (%s, %s)"
        values = (temperatura, umidade)
        
        # Executa a query
        cursor. execute(query, values)
        
        # Faz o commit da transação
        db.commit()
        # Imprime os dados inseridos
        print(f"Dados inseridos: temperatura = {temperatura}, umidade = {umidade}")
finally:
# Encerra o listener e fecha a conexão com o banco de dados e serial listener.stop() cursor. close()
    db. close()
    arduino.close()