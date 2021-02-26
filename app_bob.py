from dejmps import dejmps_protocol_bob, get_fidelity_phi00
from netqasm.sdk import EPRSocket
from netqasm.sdk.external import NetQASMConnection, Socket, get_qubit_state

def main(app_config=None):

    # Create a socket for classical communication
    classical_socket = Socket("bob", "alice")

    # Create a EPR socket for entanglement generation
    epr_socket = EPRSocket("alice")

    # Initialize Bob's NetQASM connection
    bob = NetQASMConnection(
        app_name=app_config.app_name,
        epr_sockets=[epr_socket]
    )

    with bob:
        # Receive EPR Pairs
        q = epr_socket.recv(number=2)
        q1, q2 = q[0], q[1]
        print("Bob received the EPR pairs")

        # Apply 3->1 method and print success result
        print("Bob is running the dejmps protocol...")
        if dejmps_protocol_bob(q1, q2, bob, classical_socket):
            print("Bob successfully created an EPR Pair with Alice")
            qubit_state = get_qubit_state(q1, reduced_dm=False)
           
            fidelity = float(get_fidelity_phi00(qubit_state))
            
        else:
            print("Bob failed to created an EPR Pair with Alice")
            fidelity = None

        return {
            
            "fidelity": fidelity
            }

if __name__ == "__main__":
    main()
