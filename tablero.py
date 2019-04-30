class tablero(object):
    def __init__(self, dimencion, hueco):
        super(tablero, self).__init__()
        self.dimencion = 7
        self.tablero = [[2 for __ in range(dimencion)] for _ in range(dimencion)]
        # activar modo english (cruz)
        for i in range(dimencion):
            for j in range(2, 5):
                self.tablero[i][j] = 1
                self.tablero[j][i] = 1

        hueco = [3, 3]
        self.tablero[hueco[0]][hueco[1]] = 0

    def mostrar_tablero(self):
        # mostrar tablero
        for fila in self.tablero:
            txt = ""
            for columna in fila:
                txt += "  " + str(columna) + "  "
            print(txt)
