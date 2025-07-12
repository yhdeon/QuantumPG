from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit.quantum_info import Statevector

# in this code, we are using 4 qubits, 4 classical bits
# 4 qubits -> 2 user qubits (target) and 2 ancilla qubits (attacker)
def qubitsInitialization(n_qubits):
    qc = QuantumCircuit(n_qubits, n_qubits)
    # Put user qubits in superposition
    for i in range(n_qubits // 2):
        qc.h(i)  # Apply Hadamard gate to user qubits
    return qc

# simulating oracle
# for the simulation, we mark the solution as |10>
def groverOracle(qc):
    qc.x(1)
    qc.cz(0, 1)  # Apply CZ gate to mark the state |11⟩ as the solution
    qc.x(1)  # Flip qubit 1 back to |0⟩
    return qc

# diffusion operator (H-X-CZ-X-H)
def groverDiffusion(qc, n_qubits):
    # Apply Hadamard gates to all qubits
    qc.h(range(n_qubits // 2))
    # Apply X gates to all qubits
    qc.x(range(n_qubits // 2))
    # Apply CZ gate between the first two qubits
    qc.cz(0, 1)
    # Apply X gates again
    qc.x(range(n_qubits // 2))
    # Apply Hadamard gates again
    qc.h(range(n_qubits // 2))
    return qc

# simulate attacker entangling user qubits with ancilla qubits
def ancillaEntanglement(qc, n_qubits):
    # Entangle user qubits with ancilla qubits
    for i in range(n_qubits // 2):
        qc.cx(i, i + (n_qubits // 2))  # Copy user qubit to ancilla qubit
    return qc

def measureQubits(qc, n_qubits):
    # Measure all qubits
    qc.measure(range(n_qubits), range(n_qubits))
    return qc

final_circuit = (qubitsInitialization(4)
    .compose(groverOracle(QuantumCircuit(4, 4)))
    .compose(groverDiffusion(QuantumCircuit(4, 4), 4))
    .compose(ancillaEntanglement(QuantumCircuit(4, 4), 4))
    .compose(measureQubits(QuantumCircuit(4, 4), 4))
)
print(final_circuit.draw())

simulator = AerSimulator()
job = simulator.run(
    final_circuit,
    shots=1000  # Simulate 1000 runs to get a distribution of results
)
result = job.result()
counts = result.get_counts()
print("No. of counts: ", counts)