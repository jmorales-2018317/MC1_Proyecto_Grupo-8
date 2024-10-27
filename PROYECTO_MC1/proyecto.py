# PROYECTO MC1 - Grupo # 8
# Importar las librerías necesarias para el proyecto

from qiskit_aer import Aer
from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import os

# Declarar e inicializar el simulador

simulator = Aer.get_backend('qasm_simulator')

# Definir todas las combinaciones posibles (4)

possible_combinations = [(0, 0), (0, 1), (1, 0), (1, 1)]

# Ciclo 'for' para realizar las operaciones en las 4 posibles combinaciones

for (a, b) in possible_combinations:
    # Crear una carpeta para almacenar la info de la combinación correspondiente de A y B

    file = f"Reporte_A_{a}_B_{b}"
    if not os.path.exists(file):
        os.makedirs(file)
    
    # Crear un circuito cuántico con 3 qubits y 2 bits clásicos

    qc = QuantumCircuit(3, 2)
    
    # Inicializar los qubits A y B

    if a == 1:
        qc.x(0)  # Utilizar el método ¨X¨ para aplicar la puerta NOT al qubit A y cambiar su estado a 1
    if b == 1:
        qc.x(1)  # Utilizar el método ¨X¨ para aplicar la puerta NOT al qubit B y cambiar su estado a 1
    
    # Visualizar y guardar el circuito cuántico inicial

    qc.draw(output='mpl')
    plt.title(f"Circuito cuántico inicial para A={a}, B={b}")
    plt.savefig(f"{file}/Grupo#8_Circuito_inicial_A_{a}_B_{b}(1).png")
    plt.close()

    # Utilizar el método ¨CX¨ para aplicar la puerta CNOT para calcular la suma (A ⊕ B)

    qc.cx(0, 1)

    # Visualizar y guardar el circuito después de aplicar CNOT
    
    qc.draw(output='mpl')
    plt.title(f"Circuito cuántico después de CNOT para A={a}, B={b}")
    plt.savefig(f"{file}/Grupo#8_Circuito_suma_A_{a}_B_{b}(2).png")
    plt.close()

    # Utilizar el método ¨CCX¨ para aplicar la puerta Toffoli (CCNOT) para calcular el acarreo (A ∙ B)

    qc.ccx(0, 1, 2)

    # Visualizar y guardar el circuito después de aplicar Toffoli (acarreo)
    
    qc.draw(output='mpl')
    plt.title(f"Circuito cuántico después de Toffoli (Acarreo) para A={a}, B={b}")
    plt.savefig(f"{file}/Grupo#8_Circuito_acarreo_A_{a}_B_{b}(3).png")
    plt.close()

    # Medir los resultados

    qc.measure(1, 0)  # Medir el qubit de la suma (S)
    qc.measure(2, 1)  # Medir el qubit del acarreo (C)
    
    # Visualizar y guardar el circuito final con las mediciones

    qc.draw(output='mpl')
    plt.title(f"Circuito final con mediciones para A={a}, B={b}")
    plt.savefig(f"{file}/Grupo#8_Circuito_final_A_{a}_B_{b}(4).png")
    plt.close()

    # Ejecutar el circuito creado en el simulador cuántico que declaramos al inicio

    result = simulator.run(qc).result()
    
    # Utilizar el método get_counts para obtener la distribución de probabilidad de las mediciones

    counts = result.get_counts(qc)
    
    # Mostrar y guardar la distribución de resultados en un histograma

    plot_histogram(counts)
    plt.title(f"Distribución de resultados para A={a}, B={b}")
    plt.savefig(f"{file}/Grupo#8_Histograma_A_{a}_B_{b}(5).png")
    plt.close()

    # Mostrar el resultado más probable

    resultado = max(counts, key=counts.get)  # El método 'max' retorna el resultado mas frecuente
    suma = resultado[0]  # Obtener el primer bit, resultado de la suma (S)
    acarreo = resultado[1]  # Obtener el segundo bit, resultado del acarreo (C)
    
    # Crear un archivo txt para guardar los resultados

    with open(f"{file}/Grupo#8_Resultados_A_{a}_B_{b}(6).txt", 'w') as f:
        f.write(f"A={a}, B={b} Resultado más probable: Suma = {suma}, Acarreo = {acarreo}\n")
        f.write(f"Distribución completa de resultados: {counts}\n")

    # Visualizar y guardar el estado de los qubits de entrada

    x_labels = ['A', 'B']
    y_values = [a, b]

    plt.bar(x_labels, y_values, color=['blue', 'orange'])
    plt.ylim(-0.5, 1.5)
    plt.ylabel('Estado del Qubit')
    plt.title(f"Estado de los Qubits de Entrada para A={a}, B={b}")
    plt.axhline(y=0, color='black', linewidth=0.5, linestyle='--')
    plt.axhline(y=1, color='black', linewidth=0.5, linestyle='--')

    for i, v in enumerate(y_values):
        plt.text(i, v + 0.1, str(v), ha='center', va='bottom')

    # Guardar el gráfico de los estados de los qubits de entrada
    
    plt.savefig(f"{file}/Grupo#8_Estado_Qubits_A_{a}_B_{b}(7).png")
    plt.close()

    # Hacer un archivo txt resumiendo lo que se trabajo en la iteración del circuito

    with open(f"{file}/Grupo#8_Resumen_A_{a}_B_{b}(8).txt", 'w') as f:
        f.write(f"Resumen para A={a}, B={b}:\n")
        f.write(f"- Se inicializan los qubits A y B en los estados {a} y {b}, respectivamente.\n")
        f.write(f"- Se aplica la puerta CNOT para obtener la suma (A xor B).\n")
        f.write(f"- Se aplica la puerta Toffoli (CCNOT) para obtener el acarreo (A . B).\n")
        f.write(f"- Se mide el qubit 1 para la suma y el qubit 2 para el acarreo.\n")
        f.write(f"- El resultado más probable es suma = {suma}, acarreo = {acarreo}.\n")
        f.write(f"- Se genera un histograma que muestra la probabilidad de cada resultado posible.\n")
        f.write(f"- Finalmente, se muestran los estados de entrada de los qubits A y B en un gráfico.\n")