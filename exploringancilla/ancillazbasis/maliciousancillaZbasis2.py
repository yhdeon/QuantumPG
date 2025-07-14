# malicious ancilla z-basis used on environment 2

# creating a simple environment for playtesting and observing concepts
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt

# qc = QuantumCircuit(2, 2)
# Initially its 2 qubits, 2 classical bits

# Attacker attaches ancilla so now its 4 qubits, 2 target, 2 ancilla
qc = QuantumCircuit(4, 4)

# target input qubits here:
qc.x(0) # setting q0 to be |1>
# q1 is |0> for this example

# attacker attach their ancilla to 2 target qubits
qc.cx(0,2)
qc.cx(1,3)

# target original circuit logic starts here:
qc.h(0)
qc.h(1)
qc.cx(0,1)
qc.x(0)

# measure will also change because total no. of qubits is now 4
#qc.measure([0, 1], [0, 1])
qc.measure([0, 1, 2, 3], [0, 1, 2, 3])

# Standard way to simulate the circuit and display results + circuit
simulator = AerSimulator()
# simulate a single run (shots=1) to get one random bit
job = simulator.run(qc, shots=1000)
result = job.result()
counts = result.get_counts()
print(qc.draw())
print("No. of counts: ", counts)

# Display graph result
plot_histogram(counts)
plt.show()

