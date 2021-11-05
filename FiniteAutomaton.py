from FAException import FAException


class FiniteAutomaton:
    def __init__(self, file_name):
        self.states = []
        self.alphabet = []
        self.transitions = []
        self.initial_state = None
        self.final_states = []
        self.valid = True
        self.DFA = True

        self.interpreters = {
            "Set of states": self.interpret_states,
            "Alphabet": self.interpret_alphabet,
            "Transitions": self.interpret_transitions,
            "Final states": self.interpret_final_states
        }

        self.readfile(file_name)

    def readfile(self, file_name):
        file = open("input/" + file_name, "r")
        if not file:
            return

        lines = file.readlines()
        file.close()
        for line in lines:
            split_by_comma = line.split(':')
            key = split_by_comma[0]
            value = split_by_comma[1]

            if key in self.interpreters.keys():
                self.interpreters[key](value)

    def interpret_states(self, states_string):
        self.states = states_string.strip().replace(' ', '').split(';')
        if len(self.states) > 0:
            self.initial_state = self.states[0]

    def interpret_alphabet(self, alphabet_string):
        alphabet = alphabet_string.strip().replace(' ', '').split(';')

        if any(a in self.states for a in alphabet):
            raise FAException("Alphabet element appears in states")

        self.alphabet = alphabet

    def interpret_transitions(self, transitions_string):
        for action_string in transitions_string.split(';'):
            split_by_eq = action_string.replace(' ', '').split('=')
            split_by_comma = split_by_eq[0][2:-1].split(',')

            origin = split_by_comma[0].strip()
            action = split_by_comma[1].strip()
            destination = split_by_eq[1].strip()

            if origin not in self.states:
                raise FAException(action_string + " -> " + "Origin: " + origin + " not a valid state")

            if destination not in self.states:
                raise FAException(action_string + " -> " + "Destination: " + destination + " not a valid state")

            if action not in self.alphabet:
                raise FAException(action_string + " -> " + "Action: " + action + " not a valid action")

            new_transition = Transition(origin, action, destination)

            if not any(t == new_transition for t in self.transitions):
                self.transitions.append(new_transition)

            if any(t != new_transition and t.like(new_transition) for t in self.transitions):
                self.DFA = False

    def interpret_final_states(self, final_states_string):
        final_states = final_states_string.replace(' ', '').split(';')

        for fs in final_states:
            if fs not in self.states:
                raise FAException("Final state: " + fs + " not a valid state")

            self.final_states.append(fs)

    def __str__(self):
        buffer = ""
        buffer += "States: "
        for s in self.states:
            buffer += s + ", "

        buffer += "\nAlphabet: "
        for a in self.alphabet:
            buffer += a + ", "

        buffer += "\nTransitions: "
        for t in self.transitions:
            buffer += str(t) + ", "

        buffer += "\nFinal states: "
        for b in self.final_states:
            buffer += b + ", "

        return buffer

    def check_sequence_validity(self, sequence):
        if not self.DFA:
            print("Not a DFA")
        current_state = self.initial_state
        for step in sequence:
            print("Current state: " + current_state)
            go = False
            for t in self.transitions:
                if t.origin == current_state and t.action == step:
                    current_state = t.destination
                    print("Transition: " + str(t))
                    go = True
                    break

            if not go:
                return False

        if current_state not in self.final_states:
            return False

        return True

class Transition:
    def __init__(self, origin, action, destination):
        self.origin = origin
        self.action = action
        self.destination = destination

    def __eq__(self, other):
        if not isinstance(other, Transition):
            return False

        return self.origin == other.origin and self.action == other.action and self.destination == other.destination

    def like(self, other):
        if not isinstance(other, Transition):
            return False

        return self.origin == other.origin and self.action == other.action

    def __str__(self):
        return "d(" + self.origin + ", " + self.action + ") = " + self.destination
