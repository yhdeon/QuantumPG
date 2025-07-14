from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# 2 input qubits, 2 classical bits
qc = QuantumCircuit(2, 2)

# target original circuit logic starts here:
# target original circuit is applying superposition and entanglement, resembling a small
# part of an algorithm like quantum error correction, comms, or simplied shor
qc.h(0)
qc.cx(0,1) # entangling q0, q1
qc.x(0) # flipping q0 to |1> (simulating transformation)
qc.cz(0, 1)
qc.h(1) # applying Hadamard to q1

# performing measurement
qc.measure([0, 1], [0, 1])

print(qc.draw())
