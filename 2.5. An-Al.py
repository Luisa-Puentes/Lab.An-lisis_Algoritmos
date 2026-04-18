import time
import random
import matplotlib.pyplot as plt
import seaborn as sns

# --- ALGORITMOS DE ORDENAMIENTO ---

def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        # Insertar A[j] en la secuencia ordenada A[0..j-1]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key

def merge_sort(A):
    if len(A) > 1:
        mid = len(A) // 2
        L = A[:mid]
        R = A[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Mezcla de los subarreglos
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1

        # Verificar si quedaron elementos
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1

# --- FUNCIÓN PARA MEDIR TIEMPOS ---

def medir_tiempos_ordenamiento():
    # Tallas específicas pedidas en la guía para el punto 2.5
    tallas = [10, 50, 100, 500, 1000, 5000]
    tiempos_insertion = []
    tiempos_merge = []

    print("Iniciando pruebas de tiempo... Por favor espera.")

    for n in tallas:
        # Generar arreglo aleatorio para la prueba
        arreglo_base = [random.randint(1, 10000) for _ in range(n)]
        
        # Copia para Insertion Sort
        copia_ins = arreglo_base.copy()
        inicio = time.time()
        insertion_sort(copia_ins)
        tiempos_insertion.append(time.time() - inicio)
        
        # Copia para Merge Sort
        copia_merge = arreglo_base.copy()
        inicio = time.time()
        merge_sort(copia_merge)
        tiempos_merge.append(time.time() - inicio)
        
        print(f"Finalizada talla n={n}")

    # Graficar resultados con tus colores favoritos
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=tallas, y=tiempos_insertion, label='Insertion Sort O(n²)', color='purple', marker='s')
    sns.lineplot(x=tallas, y=tiempos_merge, label='Merge Sort O(n log n)', color='hotpink', marker='o')
    
    plt.title('Comparación de Tiempos: Merge Sort vs Insertion Sort')
    plt.xlabel('Tamaño del arreglo (n)')
    plt.ylabel('Tiempo (segundos)')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    print("Mostrando gráfica...")
    plt.show()

if __name__ == "__main__":
    medir_tiempos_ordenamiento()