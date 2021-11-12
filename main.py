from FAException import FAException
from FiniteAutomaton import FiniteAutomaton
from Menu import Menu


try:
    finiteAutomaton = FiniteAutomaton("FA.in")
    print(finiteAutomaton)
    print("DFA: " + str(finiteAutomaton.DFA))
    print()

    menu = Menu(finiteAutomaton)
    menu.display_commands()
    menu.get_input()

    menu.start()
except FAException as fae:
    print(str(fae))


