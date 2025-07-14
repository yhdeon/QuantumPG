# creating a simple environment for playtesting and observing concepts
# using environment 4
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit.quantum_info import Statevector

import matplotlib.pyplot as plt

# initially its 2 qubits, 2 classical bits
# including ancilla, now its 4 qubits, 2 target, 2 ancilla
qc = QuantumCircuit(4, 4)

# simulate target input qubit q0 be |1> and q1 be |0>
qc.x(0)  # q0 is |1>

# attacker attach malicious ancilla to target qubits
qc.cx(0,2)
qc.cx(1,3)

# target original circuit logic starts here:
# target original circuit is applying superposition and entanglement, resembling a small
# part of an algorithm like quantum error correction, comms, or simplied shor
qc.h(0)
qc.cx(0,1) # entangling q0, q1
qc.x(0) # flipping q0 to |1> (simulating transformation)
qc.cz(0, 1)
qc.h(1) # applying Hadamard to q1

## perform measurement
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