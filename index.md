# Welcome to the official customShell website!
## About customShell
customShell is a module that allows you to create a custom shell

## Author
The author is [chinmaym505](https://github.com/chinmaym505)


## License
customShell has been released under the MIT license

## Link
customShell is curently on [TestPyPi](https://test.pypi.org/project/customShell-chinmaym505/)

## Installing
To install, use `pip install -i https://test.pypi.org/simple/ customShell-chinmaym505` or `python -m pip install -i https://test.pypi.org/simple/ customShell-chinmaym505`
![pip_install_stuff](https://user-images.githubusercontent.com/95156077/159143162-6f4f31e0-3618-46d6-808c-79776b1c2fba.gif)
## How to use:
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

