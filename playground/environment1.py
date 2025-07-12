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

# Create a simple 2-qubit circuit
qc = QuantumCircuit(2, 2)

qc.h(0)
qc.h(1)

qc.cx(0, 1)  # entangle q0 with q2
# qc.cx(1, 2)  # further entangle q1 with q2

qc.measure([0, 1], [0, 1])

# Standard way to simulate the circuit and display results + circuit
simulator = AerSimulator()
# simulate a single run (shots=1) to get one random bit
job = simulator.run(qc, shots=1000)
result = job.result()
counts = result.get_counts()
print(qc.draw())
print("No. of counts: ", counts)

