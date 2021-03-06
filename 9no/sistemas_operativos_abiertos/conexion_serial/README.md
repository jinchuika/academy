# Conectando dos equipos usando serial
Se conectaron dos equipos enviando información en python.

### 1. Instalar pySerial
Sirve para conectarse a un puerto serial.

```
sudo apt-get install python-pip
pip install pyserial
```

### 2. Instalar socat
Socat sirve para emular dos puertos seriales conectados entre sí. Este paso puede evitarse en caso de contar con los puertos reales conectados entre sí.

```
sudo apt-get install socat
socat -d -d PTY PTY
```

El último comando generará una salida tipo

```
2015/03/26 08:27:43 socat[5039] N PTY is /dev/pts/4
2015/03/26 08:27:43 socat[5039] N PTY is /dev/pts/8
2015/03/26 08:27:43 socat[5039] N starting data transfer loop with FDs [3,3] and [5,5]
```

El texto `/dev/pts/#` es el nombre del puerto; donde `#` identifica a cada uno.

### 3. Ejecutar el programa
El programa es un juego "Totito". Se debe correr en dos terminales distintas. El comando para ejecutarlo es

```
python main.py X '/dev/pts/4' 1

```
Donde la `X` representa el símbolo que va a jugar (puede ser `X` o `0`), la cadena el puerto completo y el `1` el número de jugador.

Por ejemplo:
En la primer terminal se escribe

```
python main.py X '/dev/pts/4' 1

```
y en la segunda terminal se escribe

```
python main.py 0 '/dev/pts/8' 2

```

El juego debería conectarse entre sí con normalidad.