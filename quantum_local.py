import math
import numpy as np
from qiskit import Aer
from qiskit.utils import QuantumInstance
from qiskit.algorithms import Shor

N  = 39
backend = Aer.get_backend('aer_simulator')
quantum_instance = QuantumInstance(backend, shots=1024)
shor = Shor(quantum_instance=quantum_instance)
print('\n Shors Algorithm')
print('--------------------')
print('\nExecuting...\n')
result = shor.factor(N)

print(f"Factors of {N}: {result.factors[0]}.")