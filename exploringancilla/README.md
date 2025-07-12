## Exploring Ancilla possible use case by attacker

Due to that nature of quantum, in order to know what the qubits value is, we need to measure it. But once we measured it, the state will collapse and that is the end of the quantum process. This poses an issue for an attacker as they are unable to 'Inspect' it being a MITM - unable to look at what the qubit is without measuring it. 

Since measuring it will result in the ending of quantum process - which will likely notify the target (some way or the another), if the attacker's intent is to eavesdrop what the target's qubit is, they can make use of ancilla to entangle with target's qubit via the use of CNOT gate qc.cx() - though the attacker have to find ways to entangle their ancilla to the target's qubit (either through compromising Quantum Cloud Provider etc.)

The attacker will then be able to know the target's qubit value after the target measured it
