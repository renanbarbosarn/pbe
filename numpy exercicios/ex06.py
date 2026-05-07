import numpy as np

imagem = np.random.randint(0, 256, size=(8, 8))

print("Imagem capturada (8x8):")
print(imagem)

centro = imagem[2:6, 2:6]

print("\nRegião central (4x4):")
print(centro)

media_centro = np.mean(centro)

print(f"\nMédia de intensidade da região central: {media_centro:.2f}")

if media_centro > 120:
    print("Engrenagem centralizada e detectada")
else:
    print("Área vazia ou peça desalinhada")
