# creating a simple environment for playtesting and observing concepts
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit.quantum_info import Statevector

# initially its 2 qubits, 2 classical bits
qc = QuantumCircuit(2, 2)

qc.h(0)
qc.h(1)

qc.cx(0,1)
qc.x(0)

qc.measure([0, 1], [0, 1])

print(qc.draw())
