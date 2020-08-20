import cirq

circuit = cirq.Circuit()
(q0, q1) = cirq.LineQubit.range(2)

# Add gates
circuit.append([cirq.H(q0), cirq.CNOT(q0, q1)])
# Measure quantum bits
circuit.append([cirq.measure(q0), cirq.measure(q1)])

print(circuit)

# Simulator
sim = cirq.Simulator()
results = sim.run(circuit, repetitions=10)
print(results)
