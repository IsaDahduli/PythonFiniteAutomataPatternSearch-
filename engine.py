def get_next_state(pattern, pattern_length, state, input_char):
    pattern = pattern;
    pattern_length = pattern_length;
    state = state;
    input_char = input_char;

    #Function to calculate the next state in the finite automaton.

    if state < pattern_length and input_char == pattern[state]:
        return state + 1

    i = 0
    for next_state in range(state, 0, -1):
        if pattern[next_state - 1] == input_char:
            while i < next_state - 1:
                if pattern[i] != pattern[state - next_state + 1 + i]:
                    break
                i += 1
            if i == next_state - 1:
                return next_state
    return 0


def construct_transition_functionDFA(pattern, pattern_length):

    #Function to compute the Transition Function (TF) for the finite automaton.

    states = ['q' + str(i) for i in range(pattern_length + 1)]  # Define states q0, q1, ..., qN
    transition_function = {state: {} for state in states}

    for state in states:
        for input_char in range(256):
            next_state = get_next_state(pattern, pattern_length, int(state[1:]), chr(input_char))
            transition_function[state][chr(input_char)] = 'q' + str(next_state)

    return transition_function


def find_pattern(pattern, input_text):

    #Function to find occurrences of a pattern in the input text using the finite automaton.

    pattern_length = len(pattern)
    transition_function = construct_transition_functionDFA(pattern, pattern_length)

    current_state = 'q0'
    for i, input_char in enumerate(input_text):
        current_state = transition_function[current_state][input_char]
        if current_state == 'q' + str(pattern_length):
            print(f"ACCEPTED at index {i - pattern_length + 1}")
        else:
            print("REJECTED")


def main():
    try:
        with open('text.txt', 'r') as file:
            input_text = file.read().strip()  # Read input text from file and remove leading/trailing whitespace
            pattern = "aabcab"  # Pattern to search for
            find_pattern(pattern, input_text)  # Find occurrences of the pattern in the input text
    except IOError as e:
        print(f"Error reading file: {e}")


if __name__ == "__main__":
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/