from sistema_empleados.empleado import Empleado
from sistema_empleados.empresa import Empresa

# Creamos un objeto de tipo Empresa
empresa1 = Empresa('Wayne Tech')

# Contratamos empleados
empresa1.contratar_empleado('Lucius Fox', 'I+D')
empresa1.contratar_empleado('Bruce Wayne', 'I+D')
empresa1.contratar_empleado('Jonathan Crane', 'Medicina')

# Obtener el total de empleados
print (f'Total de empleados: {Empleado.obtener_total_empleados()}')

# Obtener el total de empleados de un departamento
print (f'El numero de empleados del departamento de I+D es'
       f' {empresa1.obtener_numero_empleados_departamento('I+D')}')

# Mostrar todos los empleados de la empresa
empresa1.obtener_total_empleados()