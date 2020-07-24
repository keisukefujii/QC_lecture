import types
from sympy import Integer
from sympy.physics.quantum.gate import OneQubitGate,TwoQubitGate,Gate
from sympy.physics.quantum.matrixcache import matrix_cache
class ThreeQubitGate(Gate):
    nqubits = Integer(3)
def SafeUGate(target,matrix,name,nqubit=1):
    clGate = {1:OneQubitGate, 2:TwoQubitGate, 3:ThreeQubitGate}
    if(nqubit not in clGate.keys()):
        raise ValueError("Unsupported number of qubits")
    matrix_cache.cache_matrix(name, matrix.as_mutable())
    def get_from_myname(self,format = "sympy"):
        return matrix_cache.get_matrix(self.myString,format)
    gg = clGate[nqubit](target)
    gg.get_target_matrix = types.MethodType(get_from_myname,gg)
    gg.myString = name
    return gg
