import numpy as np

drone_a = np.array([float(input("Informe a coordenada x do Drone A: ")), 
                    float(input("Informe a coordenada y do Drone A: ")), 
                    float(input("Informe a coordenada z do Drone A: "))])

drone_b = np.array([float(input("Informe a coordenada x do Drone B: ")), 
                    float(input("Informe a coordenada y do Drone B: ")), 
                    float(input("Informe a coordenada z do Drone B: "))])

distancia = np.linalg.norm(drone_b - drone_a)

print(f"Distância entre os drones: {distancia:.2f} metros")

if distancia < 2.5:
    print("ALERTA DE COLISÃO")
