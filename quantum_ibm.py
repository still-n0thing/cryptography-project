from qiskit import IBMQ
from qiskit.utils import QuantumInstance
from qiskit.algorithms import Shor

IBMQ.enable_account('API Token here') 
provider = IBMQ.get_provider(hub='ibm-q')

backend = provider.get_backend('ibmq_qasm_simulator') 

print('\n Shors Algorithm')
print('--------------------')
print('\nExecuting...\n')
N = 39
factors = Shor(QuantumInstance(backend, shots=100, skip_qobj_validation=False)) 

result_dict = factors.factor(N, a=2) 
result = result_dict.factors

print(f"Factors of {N}: {result}.")
