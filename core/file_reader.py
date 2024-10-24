import random


class Car:
    """
    Represents a delivery car.

    Attributes:
        state (string): The current state of the car.
    """

    def __init__(self, state):
        """
        Initializes a new Car instance.

        Parameters:
            state (string): The initial state of the car.
        """
        self.state = state


# Introduction
print("Welcome to CarEfficiencySimulator")

# Defining constants
INITIAL_STATE = "D0"
STATE_D1 = "D1"
STATE_D2 = "D2"
FAILURE = "F"

# Defining variables
file_name = 'config.txt'

# Reading from file
def read_file(file_name):
    maintance_policy = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                maintance_policy.append(line.strip())
    except FileNotFoundError:
        print(f"File '{file_name}' doesn't exist")

    return maintance_policy

maintance_policy = read_file(file_name)

# Validate that the correct number of policies are read
if len(maintance_policy) < 7:
    print("Error: Configuration file does not have enough parameters.")
else:
    # Parameters (convert string to integer)
    transition_intensity01 = int(maintance_policy[0])
    transition_intensity12 = int(maintance_policy[1])
    transition_intensity23 = int(maintance_policy[2])
    decision_probability1 = int(maintance_policy[3])
    decision_probability2 = int(maintance_policy[4])
    maintance_range1 = int(maintance_policy[5])
    maintance_range2 = int(maintance_policy[6])

    # Defining inspection logic
    def inspection(state):
        if state == STATE_D1:
            random_number = random.randint(0, 100)
            if random_number <= decision_probability1:
                print("Car inspection required at state D1.")
                return True
        elif state == STATE_D2:
            random_number = random.randint(0, 100)
            if random_number <= decision_probability2:
                print("Car inspection required at state D2.")
                return True
        return False

    # Maintenance logic: return the new state after maintenance
    def maintance(state):
        if state == STATE_D1:
            print("The car is in state D1 and needs maintenance.")
            return INITIAL_STATE
        elif state == STATE_D2:
            print("The car is in state D2 and needs maintenance.")
            return STATE_D1
        return state

    # Main loop
    def mainLoop():
        state = INITIAL_STATE
        while state != FAILURE:
            if state == INITIAL_STATE:
                print("The car is in the initial state.")
                state = STATE_D1
            elif state == STATE_D1:
                print("The car is in state D1.")
                if inspection(state):
                    state = maintance(state)
                else:
                    state = STATE_D2
            elif state == STATE_D2:
                print("The car is in state D2.")
                if inspection(state):
                    state = maintance(state)
                else:
                    state = FAILURE
            print(f"Current car state: {state}")

    mainLoop()
