from dejmps import dejmps_protocol_alice, get_fidelity_phi00
from netqasm.sdk import EPRSocket
from netqasm.sdk.external import NetQASMConnection, Socket

def main(app_config=None):

    # Create a socket for classical communication
    classical_socket = Socket("alice", "bob")

    # Create a EPR socket for entanglement generation
    epr_socket = EPRSocket("bob")

    # Initialize Alice's NetQASM connection
    alice = NetQASMConnection(
        app_name=app_config.app_name,
        epr_sockets=[epr_socket]
    )

    with alice:

        # Create EPR Pairs
        print("Alice is creating the EPR pairs...")
        q = epr_socket.create(number=2)
        q1, q2 = q[0], q[1]

        # Apply 3->1 method and print success result
        print("Alice is running the dejmps protocol...")
        if dejmps_protocol_alice(q1, q2, alice, classical_socket):
            print("Alice successfully created an EPR Pair with Bob")
            
        else:
            print("Alice failed to create an EPR Pair with Bob")

        
        
        


if __name__ == "__main__":
    main()
