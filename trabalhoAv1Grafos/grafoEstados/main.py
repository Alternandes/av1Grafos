import numpy as np
from collections import Counter

# Dados simplificados para os estados brasileiros
fronteiras = {
    'AC': ['AM', 'RO', 'PA'],
    'AL': ['BA', 'SE', 'PE'],
    'AP': ['PA'],
    'AM': ['AC', 'RO', 'PA', 'RR'],
    'BA': ['SE', 'AL', 'PE', 'PI', 'GO', 'TO','MG', 'ES'],
    'CE': ['PI', 'PB', 'PE', 'BA'],
    'DF': ['GO', 'MG'],
    'ES': ['MG', 'RJ', 'BA'],
    'GO': ['DF', 'MG', 'BA', 'TO', 'MT'],
    'MA': ['PI', 'TO', 'PA'],
    'MG': ['ES', 'RJ', 'SP', 'BA', 'GO', 'DF'],
    'MS': ['MT', 'GO', 'SP'],
    'MT': ['RO', 'PA', 'GO', 'MS', 'DF'],
    'PA': ['AM', 'MA', 'TO', 'MT', 'RO'],
    'PB': ['PE', 'CE', 'RN', 'PA'],
    'PE': ['PB', 'CE', 'BA', 'AL'],
    'PI': ['MA', 'CE', 'BA', 'TO'],
    'PR': ['SP', 'MG', 'RS', 'SC', 'MS'],
    'RJ': ['ES', 'MG', 'SP'],
    'RN': ['PB', 'CE'],
    'RO': ['AC', 'AM', 'PA', 'MT'],
    'RR': ['AM', 'PA'],
    'RS': ['SC', 'PR'],
    'SC': ['PR', 'RS'],
    'SE': ['AL', 'BA'],
    'SP': ['MG', 'RJ', 'PR'],
    'TO': ['MA', 'PI', 'BA', 'GO', 'MT'],
}

# Ordena os estados
estados = sorted(fronteiras.keys())
n = len(estados)

# # Matriz de Adjacência
matriz_adjacencia = np.zeros((n, n), dtype=int)
indice = {estado: i for i, estado in enumerate(estados)}

for estado, vizinhos in fronteiras.items():
    i = indice[estado]
    for vizinho in vizinhos:
        j = indice[vizinho]
        matriz_adjacencia[i][j] = 1
        matriz_adjacencia[j][i] = 1

print("Matriz de Adjacência:")
print(matriz_adjacencia)

# Identificação dos Estados com Graus Máximo e Mínimo
graus = {estado: len(vizinhos) for estado, vizinhos in fronteiras.items()}
max_grau = max(graus.values())
min_grau = min(graus.values())

estados_max_grau = [estado for estado, grau in graus.items() if grau == max_grau]
estados_min_grau = [estado for estado, grau in graus.items() if grau == min_grau]

print("\nEstados com o maior número de vizinhos (grau máximo):")
print(estados_max_grau, "com grau", max_grau)

print("\nEstados com o menor número de vizinhos (grau mínimo):")
print(estados_min_grau, "com grau", min_grau)

# Frequência dos Graus dos Vértices
frequencia_graus = Counter(graus.values())

print("\nFrequência dos graus dos vértices:")
for grau, freq in frequencia_graus.items():
    print(f"Grau {grau}: {freq} estados")
