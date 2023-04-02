
import matplotlib.pyplot as plt
import numpy as np

print()
print(10*'*', 'APP DE SIMULACIÓN FINANCIERA PARA ALCANZAR LA META DE ADQUIRIR CASA', 10*'*' )
print()

INGRESOS=float(input('Ingreso mensual?'))
#INGRESOS=25000
PERIODO=12

gasto_fijo=float(input('Gasto fijo mensual?'))
#gasto_variable=6000
gasto_variable= float(input('Gasto variable mensual?'))
EGRESOS=gasto_fijo+gasto_variable

#ALGORITMO INGRESOS, EGRESOS Y AHORROS
activo=False
if INGRESOS>EGRESOS:
    activo=True


if activo:
    ganancia_anual=INGRESOS*PERIODO
    gasto_anual=EGRESOS*PERIODO
    ahorro=ganancia_anual-gasto_anual
    print()
    print(f'El ahorro anual es de {ahorro}')
    print(25*'-')




#DATOS
COSTO_TERRENO={
    'CDMX':28000,
    'MTY':21000,
    'GDL':20000
}

COSTO_CONST={
    'Residencial':(7000+11000)/2,
    'Economico':(5500+7500)/2

}


#VARIABLES DE DECISIÓN
dimension_casa=int(input('Dimension de la casa en m^2?'))
ciudad=input('En que ciudad, CDMX, MTY O GDL?')
modelo=input('Sería Residencial o Economico?')
a=int(input('En cuantos años adquirirla?'))


ct=COSTO_TERRENO[ciudad]*dimension_casa
cc=COSTO_CONST[modelo]*dimension_casa
COSTO_TOTAL=ct+cc
print()
print(f'El costo total de la casa deseada sería de:{COSTO_TOTAL}')
print(25*'-')
print()
print('La gráfica siguiente muestra si se alcanza la meta en el tiempo estimado en base al presupuesto.')
print(25*'-')

#cetes

T=10
simu_cete=[ahorro]
tasa=11.1/100

for i in range(T):
    y=ahorro+simu_cete[i]*(1+tasa)
    simu_cete.append(y)


tiempo=np.arange(T+1)
simu=ahorro*tiempo


plt.figure(figsize=(10,6))
plt.title('ESTRATEGIA PARA META', size=18)
plt.plot(tiempo,simu, label='ingreso fijo')
plt.xlabel('Tiempo (años)', size=14,)
plt.ylabel('Cantidad (miles de pesos)', size=14,)
plt.grid(True)
plt.plot(a,COSTO_TOTAL,'ro', label='costo casa')
plt.plot(tiempo,simu_cete, label='estrategia cete')
plt.legend()
plt.show()