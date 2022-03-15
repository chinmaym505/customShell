import sys
class shell:
    def __init__(self,commands):
        self.commands = commands
    def run(self):
        while True:
            a=input(">").split(" ")
            command = a[0]
            if not command in self.commands.keys():
                print('command not found')
            else:
                if self.commands.get(command)[0] == 0 and len(a)==2:
                    print(f"{command} takes no arguments")
                else:
                    if self.commands.get(command)[0] == 1:
                        try:
                            exec(f"{self.commands.get(command)[1]} = \"{a[1]}\"\n{self.commands.get(command)[2]}")
                        except:
                            print('Didn\'t get any arguments')
                            pass
                    else:
                        exec(self.commands.get(command)[2])
