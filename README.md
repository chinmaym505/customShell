# customShell
## About
customShell is a module that allows you to create a custom shell
### Author
The author is [chinmaym505](https://github.com/chinmaym505)
### License
customShell has been released under the MIT license
## How to use this module
```
import customShell.shell as shell
myShell = shell.shell({command (type: string):[has arguments? (1 for yes 0 for no),variable to store argument (type: string, keep as empty string if no argument)),code to run for command (type: string)], (other things if any)})
myShell.run()

```
### Example
```
import customShell.shell as shell
myShell = shell.shell({"sayHi":[1,"name","""print(f"Hello there, {name}!")"""],"sayMeow":[0,"","""print("meow!")"""]})
myShell.run()
```
