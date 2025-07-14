# creating a simple environment for playtesting and observing concepts
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit.quantum_info import Statevector

import matplotlib.pyplot as plt

#################################################
# ENVIRONMENT 1 Target Does abit of processing  #
# (superposition, entanglement)                 #
# and then measures                             #
#################################################
# OPTION 1 Z-Basis Attack
# Goal: Attacker stealing target qubit input state
# Attacker attach aniclla and infer parity

# Advantage:
# No interference to target original circuit logic
# Attacker will get original qubit input of target

# Limitations:
# - Attacker will need access to the circuit and modify to add ancilla qubits
# - This attack works only if malicious ancilla is attached before the target qubit is put into superposition
#################################################


# Originally created as simple 2-qubit circuit
# Attacker attaches ancilla to each of the 2 qubits -> so now 4 qubits (2 target, 2 ancilla)
# q0, q1, a2, a3,
qc = QuantumCircuit(4, 4)

# qubits are |0> by default
# in this example, we simulate user inputing q0 |1>, q1 |0>
qc.x(0) # setting q0 to be |1> 
# setting q1 to be |0>

# Attacker attaches ancilla to each of the 3 qubits
qc.cx(0, 2) # ancilla (qc[2]) copies target qubit (qc[0])
qc.cx(1, 3) # ancilla (qc[3]) copies target qubit (qc[1])

##############################################
# Target original circuit starts here onwards:
# Apply H to qubit 0 and 1 (superposition)
qc.h(0)
qc.h(1)
# Apply CNOT gates for some entanglement
qc.cx(0, 1)  # entangle q0 with q1
# qc.cx(1, 2)  # further entangle q1 with q2

# Measure all qubits
qc.measure([0, 1, 2, 3], [0, 1, 2, 3])
# output will be bitstring = [q3][q2][q1][q0]
# ancilla is q2, q3

# Standard way to simulate the circuit and display results + circuit
simulator = AerSimulator()
# simulate a single run (shots=1) to get one random bit
job = simulator.run(qc, shots=1000)
result = job.result()
counts = result.get_counts()
print(qc.draw())
print("No. of counts: ", counts)

# The output will be something like:
# No. of counts:  {'0101': 257, '0100': 240, '0110': 242, '0111': 261}
# bitstring = [q3][q2][q1][q0] -> q2 & q3 are ancilla

######################################################
######## q2 ## q3 ## Attacker inference          #####
# 0101 # 1  ## 0  ## Stating that q0 = 1, q1 = 0 #####
# 0100 # 1  ## 0  ## Stating that q0 = 1, q1 = 0 #####
# 0110 # 1  ## 0  ## Stating that q0 = 1, q1 = 0 #####
# 0111 # 1  ## 0  ## Stating that q0 = 1, q1 = 0 #####
######################################################
# Based on the inference, attacker will know that the target qubit q0 is |1> and q1 is |0>
# For the other qubits, they are different from the original target circuit logic (not really relevant for attacker)

# Display graph result
plot_histogram(counts)
plt.show()