from FAException import FAException
from FiniteAutomaton import FiniteAutomaton
from Menu import Menu

fa = FiniteAutomaton("FA.in")

menu = Menu(fa)
menu.display_commands()
menu.get_input()

try:
    finiteAutomaton = FiniteAutomaton("FA.in")
    print(finiteAutomaton)
    print("DFA: " + str(finiteAutomaton.DFA))
    print()

    print("Valid sequence" if finiteAutomaton.check_sequence_validity("aabaabb") else "Invalid sequence")
except FAException as fae:
    print(str(fae))


