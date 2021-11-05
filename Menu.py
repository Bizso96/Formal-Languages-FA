class Menu:
    def __init__(self, finite_automaton):
        self.commands = {}
        self._add_command("exit", ExitCommand)
        self._add_command("check", CheckSequenceCommand)
        self.finite_automaton = finite_automaton

    def _add_command(self, key, command):
        self.commands[key] = command(key, self)

    def display_commands(self):
        for key in self.commands.keys():
            print(" " + str(self.commands[key]))

    def get_input(self):
        i = input(">")
        if i in self.commands.keys():
            self.commands[i].execute()
        else:
            print("Unknown command")


class Command:
    def __init__(self, key, description, menu):
        self.key = key
        self.description = description
        self.menu = menu

    def __str__(self):
        return "[" + self.key + "]" + " - " + self.description

class ExitCommand(Command):
    def __init__(self, key, menu):
        Command.__init__(self, key, "Exit the application", menu)

    def execute(self):
        exit()

class CheckSequenceCommand(Command):
    def __init__(self, key, menu):
        Command.__init__(self, key, "Check the validity of a sequence", menu)

    def execute(self):
        sequence = input("Sequence: ")
        print("Valid sequence\n" if self.menu.finite_automaton.check_sequence_validity(sequence) else "Invalid sequence\n")