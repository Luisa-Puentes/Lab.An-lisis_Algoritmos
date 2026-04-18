import time
import random
import matplotlib.pyplot as plt
import seaborn as sns

# --- ALGORITMOS DE SUBARREGLO MÁXIMO ---

def fuerza_bruta_max_subarray(A):
    max_suma = float('-inf')
    for i in range(len(A)):
        suma_actual = 0
        for j in range(i, len(A)):
            suma_actual += A[j]
            if suma_actual > max_suma:
                max_suma = suma_actual
    return max_suma

def max_crossing_subarray(A, low, mid, high):
    left_sum = float('-inf')
    suma = 0
    for i in range(mid, low - 1, -1):
        suma += A[i]
        if suma > left_sum:
            left_sum = suma
    right_sum = float('-inf')
    suma = 0
    for j in range(mid + 1, high + 1):
        suma += A[j]
        if suma > right_sum:
            right_sum = suma
    return left_sum + right_sum

def divide_y_venceras_max_subarray(A, low, high):
    if high == low:
        return A[low]
    mid = (low + high) // 2
    left_max = divide_y_venceras_max_subarray(A, low, mid)
    right_max = divide_y_venceras_max_subarray(A, mid + 1, high)
    cross_max = max_crossing_subarray(A, low, mid, high)
    return max(left_max, right_max, cross_max)

# --- FUNCIÓN PARA MEDIR TIEMPOS ---

def medir_tiempos():
    tallas = [10, 50, 100, 200, 500, 1000]
    tiempos_fb = []
    tiempos_dv = []

    for n in tallas:
        # Generar arreglo aleatorio con signos alternos como pide el taller
        arreglo = [random.randint(-100, 100) for _ in range(n)]
        
        # Medir Fuerza Bruta
        inicio = time.time()
        fuerza_bruta_max_subarray(arreglo)
        tiempos_fb.append(time.time() - inicio)
        
        # Medir Divide y Vencerás
        inicio = time.time()
        divide_y_venceras_max_subarray(arreglo, 0, len(arreglo) - 1)
        tiempos_dv.append(time.time() - inicio)

    # Graficar resultados
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=tallas, y=tiempos_fb, label='Fuerza Bruta O(n²)', color='purple', marker='o')
    sns.lineplot(x=tallas, y=tiempos_dv, label='Divide y Vencerás O(n log n)', color='hotpink', marker='o')
    plt.title('Comparación de Tiempos: Subarreglo Máximo')
    plt.xlabel('Tamaño del arreglo (n)')
    plt.ylabel('Tiempo (segundos)')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    medir_tiempos()