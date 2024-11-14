import matplotlib.pyplot as plt

R = 100 * 10**3 #200*kΩ
C = 100 * 10**(-6) #100 µF
v = [0] #startverdi
t = [0]
N = 1000
T = 60
h = T/N

t_maalte = [i*5 for i in range(13)] #tok målinger hvert 5. sekund i ett minutt
v_maalte = [0, 2.3, 4.9, 6, 6.7, 7.1, 7.4, 7.6, 7.7, 7.77, 7.82, 7.85, 7.88]

def f(x):        #x' = f(x)
    return (8 - x)/(R*C)

for i in range(N):
    v.append(v[i] + h*(f(v[i]) + f(v[i] + h*f(v[i])))/2) #bruker heuns metode 𝑥𝑘+1 = 𝑥𝑘 +ℎ(𝑓(𝑥𝑘) + 𝑓(𝑥𝑘 + ℎ𝑓(𝑥𝑘)))/2
    t.append((i+1)*h) #lagrer variabler for tiden

#plotter figurene, numerisk utregnet i blå, og målte verdier i rød.
plt.figure()
plt.plot(t, v, color = "blue", label = "Numerisk")
plt.plot(t_maalte, v_maalte, color = "red", label = "Målte verdier")
plt.margins(x = 0)
plt.grid()
plt.legend()
plt.show()