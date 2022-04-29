If there is a weird error and we don't know what the error is:

enter 

`import pdb; pdb.set_trace()`

the line above where the bug is supposed to be.

When the code encounters this state, it temporarily halts. On terminal by entering the variable name, it can tell us what the value is instantly.

Entering `n` in terminal goes to the next line of the code (with the program still halting). We can exit this state by `exit`