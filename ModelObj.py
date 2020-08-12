"""

Universidad del Valle de Guatemala
Graficas por computadora
Obj
Jorge Suchite Carnet 15293
07/07/2020
SR3 . Obj Model


"""
class ModelObJ(object):
    def __init__(self, filename):
        with open(filename, 'r') as file:
            self.lines = file.read().splitlines()

        self.vertices = []
        self.normals = []
        self.texcoords = []
        self.faces = []

        self.modobj()

    def modobj(self):
        for line in self.lines:
            if line:
                prefix, value = line.split(' ', 1)

                if prefix == 'v': # vertices
                    self.vertices.append(list(map(float,value.split(' '))))
                    # normales
                elif prefix == 'vn':
                    self.normals.append(list(map(float,value.split(' '))))
                    #coordens
                elif prefix == 'vt':
                    self.texcoords.append(list(map(float,value.split(' '))))
                    #caras
                elif prefix == 'f':
                    self.faces.append([list(map(int, vert.split('/'))) for vert in value.split(' ')])

