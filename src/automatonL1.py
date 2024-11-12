class AutomatonL1:
    def __init__(self):
        """
        Initialize the automaton with its states, input symbols, transition function,
        initial state, and accepting states.
        """
        self.states = {"q0", "q1", "q2", "q3", "q4"}
        self.input_symbols = {"a", "b"}
        self.transition_function = {
            ("q0", "a"): "q1",
            ("q0", "b"): "q0",
            ("q1", "a"): "q2",
            ("q1", "b"): "q1",
            ("q2", "a"): "q3",
            ("q2", "b"): "q2",
            ("q3", "a"): "q4",
            ("q3", "b"): "q3",
            ("q4", "a"): "q4",
            ("q4", "b"): "q4"
        }
        self.initial_state = "q0"
        self.accept_states = {"q4"}

    def transition(self, state, input_symbol):
        """
        Given a state and an input symbol, return the next state according to the transition function.
        If no transition is possible, return None.
        """
        return self.transition_function.get((state, input_symbol))

    def accepts(self, input_string):
        """
        Determine if the automaton accepts the given input string by processing
        it through its states and transition function.
        """
        state = self.initial_state
        for symbol in input_string:
            state = self.transition(state, symbol)
            if state is None:
                return False
        return state in self.accept_states

    def start(self):
        """
        Run the automaton interactively, prompting the user for input and displaying
        whether the string is accepted or not.
        """
        print("Welcome to Automaton L1! This automaton accepts strings containing at least 4 consecutive 'a's.")
        
        while True:
            word = input("Enter a word (or 'exit' to quit): ").strip()
            if word.lower() == 'exit':
                print("Exiting the program. Goodbye!")
                break

            # Validate input
            if not all(symbol in self.input_symbols for symbol in word):
                print(f"Invalid input! Only characters {', '.join(self.input_symbols)} are allowed.")
                continue

            # Check if the word is accepted
            if self.accepts(word):
                print(f"The word '{word}' is accepted!")
            else:
                print(f"The word '{word}' is not accepted.")


# Instantiate and run the automaton
if __name__ == "__main__":
    automaton = AutomatonL1()
    automaton.start()
