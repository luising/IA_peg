class operador(object):
    """docstring for operador."""

    def __init__(self):
        super(operador, self).__init__()

    def mapa_movimiento(self, tablero):
        ts = []

        # activar modo english (cruz)
        for i in range(5):
            for j in range(2, 5, 3):
                desplazar_columna = [self.tablero[i][j], self.tablero[i][j + 1], self.tablero[i][j + 2]]
                desplazar_fila = [self.tablero[j][i], self.tablero[j + 1][i], self.tablero[j + 2][i]]
                ts.append(desplazar_columna)
                ts.append(desplazar_fila)
        i, j = 0, 2
        for i in range(4):
            desplazar_columna = [self.tablero[i][j], self.tablero[i][j + 1], self.tablero[i][j + 2]]
            desplazar_fila = [self.tablero[j][i], self.tablero[j + 1][i], self.tablero[j + 2][i]]
            ts.append(desplazar_columna)
            ts.append(desplazar_fila)

    def obtener_estados_diponibles():
        pass
