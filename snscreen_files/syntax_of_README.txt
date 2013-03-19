snscreen expects README to follow a certain syntax.
Here are certain rules:

1. The name that you want to give it to your window needs to be placed after a keyword WINDOW.
"WINDOW" is a keyword that should be a start of the line.
The next work after a "space" after WINDOW, becomes you window name.
Anything after this, will be neglected.
----------- Example:
"WINDOW PDN runs a web server"
 -> Here, window name will be "PDN". The rest of the words are neglected.

2. The WINDOW line should be guarded above and below, by a line starting with "==="
Anything that follows "===" on that line will be neglected.
If the line just above or just below the WINDOW line does not meet this syntax, its an error.
----------- Example:
====These words make no difference
WINDOW boxer
====

3. Using "#": If you dont want the command to be executed at the target window 
but you still want that command to be pushed to the target window, start it with "#"
----------- Example:
#./callgen
  -> This command will be sent to the target window. But it will not be executed

4. Using "##": You may want to place some comments in your readme.
Such comments do not make a shell command. Hence these shall not be pushed to the target window.
Start such lines with "##"
----------- Example:
## This is just a comment

5. Using "UNUSED": You may not want to one of the tool in one run but use it in a next run.
Then just put the keywork "UNUSED" anywhere in the "WINDOW" line.
Then this window will not be created and the commands that follow are neglected.
----------- Example:
===
WINDOW AAA-server UNUSED
===
  -> Here you decide to do local authentication, so you do not need a AAA-server.
  Why waste a screen space by creating unwanted extra window?
  So you mark it UNUSED. Next run, just remove this keywork and you will have AAA-server window.
