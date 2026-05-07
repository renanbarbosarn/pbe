import numpy as np

temperaturas = [round(np.random.uniform(20, 80), 2) for _ in range(30)]

ultrapassou_limite = list()

print(f"Temperatura máxima registrada: {np.amax(temperaturas)}°C")
print(f"Temperatura mínima registrada: {np.amin(temperaturas)}°C")
print(f"Temperatura média mensal: {round(np.mean(temperaturas), 2)}°C")

for temp in temperaturas:
    if temp > 75:
        ultrapassou_limite.append(temp)

print(f"\nA temperatura ultrapassou o limite {len(ultrapassou_limite)} vezes, em: ")

for temp in ultrapassou_limite:
    print(f"{temp}°C")
