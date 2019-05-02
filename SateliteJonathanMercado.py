#g=Es la constante gravitacional de la tierra
#Mt=Es la masa de la tierra, Rt=Radio de la tierra, T= Periodo


g=6.67e-11
Mt=5.97e24
Rt=6371e3
pi=3.1416

print(" Inciso 1")
T=float(input("Ingrese el periodo en segundos T para un día(24 hrs): "))
h=(((g*Mt*T**2)/(4*pi**2))**(1/3))-Rt

print("La altura para el periodo en 24 hrs es: ",h*(1e-5))
print("Inciso 2")

d=86400
min90=90*60
min45=45*60


h1=(((g*Mt*d**2)/(4*pi**2))**(1/3))-Rt
h2=(((g*Mt*min90**2)/(4*pi**2))**(1/3))-Rt
h3=(((g*Mt*min45**2)/(4*pi**2))**(1/3))-Rt

print("La altura para un dia es :",h1*(1e-5))
print("La altura para 90 minuto es :",h2*(1e-5))
print("La altura para 45  minuto es :",h3*(1e-5))


print(" Inciso 3")
Ts=23.93*3600

H1=(((g*Mt*Ts**2)/(4*pi**2))**(1/3))-Rt

print("La altura para un periodo de un dia sideral (23.93):",H1*(1e-5))
print("La diferencia en la altura para ambos periodos es: ",(h-H1)*(1e-5))

