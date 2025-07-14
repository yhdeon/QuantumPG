# creating a simple environment for playtesting and observing concepts
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(2, 2)

qc.h(0)
qc.h(1)
qc.cx(0,1)
qc.x(0)

qc.measure([0, 1], [0, 1])

# # Standard way to simulate the circuit and display results + circuit
# simulator = AerSimulator()
# # simulate a single run (shots=1) to get one random bit
# job = simulator.run(qc, shots=1000)
# result = job.result()
# counts = result.get_counts()
print(qc.draw())
# print("No. of counts: ", counts)