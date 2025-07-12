# creating a simple environment for playtesting and observing concepts
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit.quantum_info import Statevector

##########################################
# TEMPLATE FOR ENVIRONMENT 1             #
# ENVIRONMENT 1  Does abit of processing #
# (superposition, entanglement)          #
# and then measures                      #
##########################################

# Create a simple 3-qubit circuit
qc = QuantumCircuit(3, 3)

# Step 1: Apply H to qubit 0 and 1 (superposition)
qc.h(0)
qc.h(1)

# Step 2: Apply CNOT gates for some entanglement
qc.cx(0, 2)  # entangle q0 with q2
qc.cx(1, 2)  # further entangle q1 with q2

# Step 3: Measure all qubits
qc.measure([0, 1, 2], [0, 1, 2])

# Standard way to simulate the circuit and display results + circuit
simulator = AerSimulator()
# simulate a single run (shots=1) to get one random bit
job = simulator.run(qc, shots=1000)
result = job.result()
counts = result.get_counts()
print(qc.draw())
print("No. of counts: ", counts)

