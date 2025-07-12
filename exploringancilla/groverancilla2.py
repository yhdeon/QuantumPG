from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt

# in this example, the system marks the state |10⟩ as the solution

# ancilla purpose is to become entangled with the user qubits
# attacker will know the user qubits once user measures their own qubits, through the ancilla qubits

qc = QuantumCircuit(4,4)
# 2 user qubits and 2 ancilla qubits, 4 classical bits

qc.h(0)  # Put qubit 0 in superposition
qc.h(1)  # Put qubit 1 in superposition

qc.x(1) # flip qubit 0 to |1⟩ for cz gate 'marking'
qc.cz(0, 1)  # Mark the state |01⟩ as the solution by flipping the phase of ancilla qubit 1
qc.x(1) # flip qubit 0 back to |0⟩

# apply diffusion operator H-X-CZ-X-H
# H-X-CZ-X-H diffusion operator (CZ version)
qc.h(0)
qc.h(1)
qc.x(0)
qc.x(1)
qc.cz(0, 1)
qc.x(0)
qc.x(1)
qc.h(0)
qc.h(1)

# ancilla qubits not needed to be in superposition for this attack example
# they are initialized to |0⟩ state default
# use CNOT gate to entangle user qubits with ancilla qubits
# if user qubit is |0⟩, ancilla qubit will be |0⟩
# if user qubit is |1⟩, ancilla qubit will be |1⟩
# this is not really copying but done via entanglement

# attacker entangles user qubits with their ancilla qubits
# copy qubit0 to ancilla0
qc.cx(0,2)
# copy qubit1 to ancilla1
qc.cx(1,3)
# as we have 4 qubits -> q0 - 0, q1 - 1, ancilla0 - 2, ancilla1 - 3

# perform measurement on user qubits
qc.measure([0, 1, 2, 3], [0, 1, 2, 3])  # Measure the qubits

simulator = AerSimulator()
# simulate a single run (shots=1) to get one random bit
job = simulator.run(qc, shots=1000)
result = job.result()
counts = result.get_counts()

print(qc.draw())
print("No. of counts: ", counts)