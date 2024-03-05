import subprocess
try:
    import cirq
except ImportError:
    subprocess.check_call(["pip3", "install", "cirq"])
    import cirq
else:
    print("Cirq is already installed")

circuit = cirq.Circuit()

