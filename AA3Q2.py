# Function to simulate a railway level crossing intelligent agent
def level_crossing_agent(inbound, outbound, obstacle, emergency):

    # Priority 1: If there is an emergency situation
    if emergency == "Active":
        # Immediately lower gate, stop traffic, and turn hooter ON
        return ("Lower Gate", "Red Signal", "Hooter On")

    # Priority 2: Train detected from either side AND obstacle present
    if (inbound == "TrainDetected" or outbound == "TrainDetected") and obstacle == "Blocked":
        # Dangerous situation → Stop everything
        return ("Lower Gate", "Red Signal", "Hooter On")

    # Priority 3: Train detected but track is clear
    if (inbound == "TrainDetected" or outbound == "TrainDetected") and obstacle == "Clear":
        # Train can pass safely → Gate down, green for train, hooter ON
        return ("Lower Gate", "Green Signal", "Hooter On")

    # Priority 4: No train and no obstacle
    if inbound == "NoTrain" and outbound == "NoTrain" and obstacle == "Clear":
        # Safe condition → Raise gate for vehicles, green signal, hooter OFF
        return ("Raise Gate", "Green Signal", "Hooter Off")

    # Default condition: If none of the above cases match
    # Maintain current system state
    return ("Hold State", "Hold Signal", "Hooter Off")


# ------------------- TEST CASES -------------------

# Different input scenarios to test the agent
test_cases = [
    ("NoTrain", "NoTrain", "Clear", "Neutral"),          # Normal safe condition
    ("TrainDetected", "NoTrain", "Clear", "Neutral"),   # Train approaching
    ("TrainDetected", "NoTrain", "Blocked", "Neutral"), # Train + obstacle
    ("NoTrain", "NoTrain", "Blocked", "Active")         # Emergency case
]

# Print heading
print("\n---- LEVEL CROSSING SIMULATION ----\n")

# Loop through each test case
for case in test_cases:

    # Unpack tuple values into separate variables
    inbound, outbound, obstacle, emergency = case

    # Call the intelligent agent function
    action = level_crossing_agent(inbound, outbound, obstacle, emergency)

    # Display percept and corresponding action
    print("Percept:", case, "=> Action:", action)