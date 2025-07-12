## Exploring using ancilla for z-basis attack

### This information may be wrong, I am just jotting down based on my level of understanding :3

### About Z-Basis
- It a computational basis, consisting of 2 states |1> or |0>
- Usually if the target qubit is |0>, from the output we can usually get '0' with the ancilla

### About Z-Basis Attack
- The goal of this attack is to allow attack to find out what the input qubit state is
- From the attack, attacker can get to learn about amplitude probabilities and see the bias/parity

### Image of Circuit based on maliciousancillaZbasis.py
- Built with IBM Composer
![alt text](maliciousancillaZbasiscircuit.png)


### Advantage of the attack:
- No interference to the target original circuit logic
- Can learn about the initial target input qubit state

### Disadvantage of the attack:
- Attacker firstly need to somehow get access to the circuit first to make modification
- This attack requires the malicious ancilla to be attached to target qubit before they goes into superposition (if there is). This is because if target qubit goes into superposition, ancilla 


### Understanding target qubits when they are in classical basis state and superpositioned state
- When the malicious ancilla attach to the target qubit when they are in classical basis state, the ancilla will receive an exact copy of the classical value. It is entanglement, but a trivial kind whereby it is separatable, no cloning involved thus not violating No-Cloning theorem.
- But if the malicious ancilla attach to the target qubit when they are in superpositioned state, the action will no longer be like copying. This entanglement with superpositioned qubit will result in attacker unable to tell the target qubit and ancilla separately as it is either 0 or 1 randomly, and measuring it will collapse the entangled state, not allowing the attacker to get the original state of the target qubit fully (resulting in failed z-basis attack)

