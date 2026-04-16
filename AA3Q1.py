# Import random module to allow random movement decisions
import random

# List of rooms in the vacuum environment
rooms = ["A", "B", "C"]

# Dictionary representing the environment
# Each room is initially Dirty
environment = {
    "A": "Dirty",
    "B": "Dirty",
    "C": "Dirty"
}

# Initial position of the vacuum agent
agent_location = "A"

# Performance measure (score) of the agent
score = 0

# Display program heading
print("\n---- RANDOMIZED VACUUM AGENT ----\n")

# Maximum number of steps the agent can take
steps = 15

# ------------------------------------------------
# RANDOMIZED AGENT FUNCTION
# Decides action based on current room status
# ------------------------------------------------
def randomized_agent(location, status):

    # If the current room is dirty, clean it
    if status == "Dirty":
        return "Suck"

    # If the room is clean, move randomly
    else:
        return random.choice(["MoveLeft", "MoveRight"])

# ------------------------------------------------
# MAIN LOOP: runs the agent for a fixed number of steps
# ------------------------------------------------
for step in range(steps):

    # Agent perceives its current location and room condition
    percept = (agent_location, environment[agent_location])

    # Agent chooses an action based on the percept
    action = randomized_agent(agent_location, environment[agent_location])

    # Display the percept and chosen action
    print(f"Percept: {percept} -> Action: {action}")

    # ---------------- ACTION EXECUTION ----------------

    # If agent decides to clean the room
    if action == "Suck":
        environment[agent_location] = "Clean"   # Clean the room
        score -= 1                               # Cost for cleaning

    # If agent moves left
    elif action == "MoveLeft":

        # Penalty if agent leaves a dirty room
        if environment[agent_location] == "Dirty":
            score -= 5

        # Movement logic for left direction
        if agent_location == "C":
            agent_location = "B"
        elif agent_location == "B":
            agent_location = "A"

        score -= 1  # Cost for movement

    # If agent moves right
    elif action == "MoveRight":

        # Penalty if agent leaves a dirty room
        if environment[agent_location] == "Dirty":
            score -= 5

        # Movement logic for right direction
        if agent_location == "A":
            agent_location = "B"
        elif agent_location == "B":
            agent_location = "C"

        score -= 1  # Cost for movement

    # ---------------- GOAL TEST ----------------

    # Check if all rooms are clean
    if all(state == "Clean" for state in environment.values()):
        score += 10  # Reward for cleaning all rooms
        print("\nAll rooms cleaned successfully!")
        break         # Stop the simulation