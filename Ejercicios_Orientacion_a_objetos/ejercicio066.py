""" Defina dos clases, Paciente y Médico. Un paciente puede tener asignado un médico, pero un médico puede tener muchos pacientes. """

class Medico:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.pacientes = []  

    def asignar_paciente(self, paciente):
        self.pacientes.append(paciente)

class Paciente:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.medico_asignado = None  

    def asignar_medico(self, medico):
        self.medico_asignado = medico
