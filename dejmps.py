from netqasm.sdk.classical_communication.message import StructuredMessage
from netqasm.sdk.external import get_qubit_state
import math
import numpy as np


def dejmps_protocol_alice(q1, q2, alice, socket):
    """
    Implements Alice's side of the DEJMPS distillation protocol.
    This function should perform the gates and measurements for DEJMPS using
    qubits q1 and q2, then send the measurement outcome to Bob and determine
    if the distillation was successful.
    
    :param q1: Alice's qubit from the first entangled pair
    :param q2: Alice's qubit from the second entangled pair
    :param alice: Alice's NetQASMConnection
    :param socket: Alice's classical communication socket to Bob
    :return: True/False indicating if protocol was successful
    """
               
    
    outcome1 = dejmps_gates_and_measurement_alice(q1, q2)
    alice.flush()

    # Write below the code to send measurement result to Bob,
    outcome1 = int(outcome1)
    socket.send_structured(StructuredMessage("The results are:", (outcome1)))

    # receive measurement result from Bob and check if protocol was successful
    bob_out1 = socket.recv_structured().payload

    successful = False
    if outcome1 == bob_out1:
        successful = True

    return successful

def dejmps_gates_and_measurement_alice(q1, q2):
    """
    Performs the gates and measurements for Alice's side of the DEJMPS protocol
    :param q1: Alice's qubit from the first entangled pair
    :param q2: Alice's qubit from the second entangled pair
    :return: Integer 0/1 indicating Alice's measurement outcome

    """
    q1.rot_X(n=1,d=1,angle=None)
    q2.rot_X(n=1,d=1,angle=None)
    
    q1.cnot(q2)
    m1 = q2.measure()

    return m1
    


def dejmps_protocol_bob(q1, q2, bob, socket):
    """
    Implements Bob's side of the DEJMPS distillation protocol.
    This function should perform the gates and measurements for DEJMPS using
    qubits q1 and q2, then send the measurement outcome to Alice and determine
    if the distillation was successful.
    
    :param q1: Bob's qubit from the first entangled pair
    :param q2: Bob's qubit from the second entangled pair
    :param bob: Bob's NetQASMConnection
    :param socket: Alice's classical communication socket to Bob
    :return: True/False indicating if protocol was successful
    """
        
    outcome1 = dejmps_gates_and_measurement_bob(q1, q2)
    bob.flush()

    # Write below the code to send measurement result to Alice,
    outcome1 = int(outcome1)
    socket.send_structured(StructuredMessage("The results are:", (outcome1)))

    alice_out1= socket.recv_structured().payload

    successful = False
    if outcome1 == alice_out1:
        successful = True

    return successful
    

   
def dejmps_gates_and_measurement_bob(q1, q2):
    """
    Performs the gates and measurements for Bob's side of the DEJMPS protocol
    :param q1: Bob's qubit from the first entangled pair
    :param q2: Bob's qubit from the second entangled pair
    :return: Integer 0/1 indicating Bob's measurement outcome
    """

    q1.rot_X(n=7,d=1,angle=None)
    q2.rot_X(n=7,d=1,angle=None)

    q1.cnot(q2)
    m2 = q2.measure()
      
    return m2

def get_fidelity_phi00(matrix):
    phi00 = np.array([1, 0, 0, 1])
    fidelity = (1/2) * phi00.dot(matrix).dot(phi00.transpose())
    return fidelity
