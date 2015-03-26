class Juego:
    """docstring for Juego"""
    def __init__(self, simboloJugador, conexion, numeroJugador):
        self.conexion = conexion
        self.tablero = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
        self.jugadorLocal = simboloJugador
        self.turnoActual = 0
        self.iniciarJuego(numeroJugador)
        
    def jugarTurno(self):
        turno_activo = True
        while (turno_activo):
            print "Ingrese columna (1-3): "
            col = int(raw_input()) - 1
            print "Ingrese fila (1-3): "
            fila = int(raw_input()) - 1
            if self.tablero[fila][col] != ' ':
                print 'Esa casilla ya fue tomada'
            elif fila>2 or col>2:
                print 'Casilla no existe'
            else:
                self.tablero[fila][col] = self.jugadorLocal
                self.conexion.write(self.jugadorLocal+str(fila)+str(col))
                turno_activo = False
                pass
            pass
        self.render()
        return self.jugadorLocal
        pass

    def esperarTurno(self):
        turnoRival = False
        movimientoRival = ''
        while turnoRival == False:
            while movimientoRival=='':
                movimientoRival = self.conexion.read(9999)
                if len(movimientoRival) > 0:
                    turnoRival = True
                    break
                pass
            fila = int(movimientoRival[1])
            col = int(movimientoRival[2])
            self.tablero[fila][col] = movimientoRival[0]
            pass
        self.render()
        return movimientoRival[0]
        pass

    def render(self):
        print '\n Turno '+str(self.turnoActual)+' \n'
        print self.tablero[0]
        print self.tablero[1]
        print self.tablero[2]
        pass

    def revisarVictoria(self, jugador):
        for i in xrange(0,3):
            #Revisar la si gana horizontalmente
            if all(j == jugador for j in(self.tablero[i][0], self.tablero[i][1], self.tablero[i][2])):
                return True
                pass
            #revisar si gana verticalmente
            elif all(j == jugador for j in(self.tablero[0][i], self.tablero[1][i], self.tablero[2][i])):
                return True
                pass
            elif all(j == jugador for j in(self.tablero[0][0], self.tablero[1][1], self.tablero[2][2])):
                return True
                pass
            elif all(j == jugador for j in(self.tablero[0][2], self.tablero[1][1], self.tablero[2][0])):
                return True
                pass
            else:
                return False
            pass

        pass

    def iniciarJuego(self, numero):
        self.tablero = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
        finJuego = False
        if numero == 1:
            self.turnoActual = 0
        else:
            self.turnoActual = 1
        self.render()

        while (finJuego != True):
            self.turnoActual += 1
            #Jugador 1
            if self.turnoActual % 2 != 0:
                self.jugarTurno()
                if self.revisarVictoria(self.jugadorLocal) == True:
                    print '\neres el ganador'
                    finJuego = True
                    break
            else:
                jugadorRival = self.esperarTurno()
                if self.revisarVictoria(jugadorRival) == True:
                    print '\nGana el oponente'
                    finJuego = True
                    break
            if self.turnoActual>=9:
                print 'El juego es un empate'
                finJuego = True
                break
                
                
            pass
        pass