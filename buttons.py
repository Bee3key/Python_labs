from functools import partial
mybutton = partial(Button, root, fg="black",bg="white",font="times",size="12")
b1 = mybutton(text="Ok") 
b2 = mybutton(text="Cancel") 
b3 = mybutton(text="Restart")