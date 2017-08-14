##############################
# Created by HuskerDu (Pixie)#
##############################


from tkinter import *
from tkinter import ttk
from operator import add, sub, mul, truediv

equation = ''

####################################################
#Converting from infix notation to postfix notation#
####################################################

def infix_to_post(s):
    try:
        stack, b = [], []
        a = s.split()
        for i in a:
            if i not in '/*-+':
                b.append(i)
            else:
                if not stack:
                    stack.append(i)
                else:
                    if stack[-1] in '+-' and i in '*/':
                        stack.append(i)
                    else:
                        while stack:
                            b.append(stack.pop())
                        stack.append(i)
        while stack:
            b.append(stack.pop())
        return ' '.join(b)
    except:
        eqn.set('Error')

        
        
##########################
#Solving postfix notation#
##########################


def postfix_solve(s):
    try:
        op = {'+': add, '-': sub, '*': mul, '/': truediv}
        stack = []
        c = s.split()
        for i in c:
            if i in op:
                a, b = stack.pop(), stack.pop()
                stack.append(op[i](float(b), float(a)))
            elif i:
                stack.append(i)
        return stack.pop()
    except:
        eqn.set('Error')

        
###################################
#Getting the equation to be solved#
###################################


def get_eqn(s):
    global equation
    try:
        if s=='=':
            reverse_polish = infix_to_post(equation)
            ok = postfix_solve(reverse_polish)
            eqn.set(ok)
            equation=''
        elif s in '+-/*':
            equation+=" "+s+" "
            eqn.set(equation)
        else:
            equation+= s
            eqn.set(equation)
    except:
        eqn.set('Error')
        
        
################################################
#Creating the basic framework of the calculator#
################################################
        
root = Tk()
root.title('Calculator')  #Setting GUI Title


window = ttk.Frame(root, padding='10 10 10 10')
window.grid(row=0, column=0, sticky=(N, W, E, S))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

eqn = StringVar() #Variable for interacting with the GUI


########################################################
#Creating the space for equation and result to be shown#
########################################################

stuff = ttk.Frame(window)
stuff.grid(row=0, column=0, columnspan=3, sticky=(E))
ttk.Label(stuff, textvariable=eqn).grid(row=0, column=1)


####################################################
#Creating all the buttons needed for the calculator#
####################################################

ttk.Button(window, text='7', command=lambda: get_eqn('7')).grid(row=1, column=0, sticky=(N, W, E, S))
ttk.Button(window, text='8', command=lambda: get_eqn('8')).grid(row=1, column=1, sticky=(N, W, E, S))
ttk.Button(window, text='9', command=lambda: get_eqn('9')).grid(row=1, column=2, sticky=(N, W, E, S))
ttk.Button(window, text='4', command=lambda: get_eqn('4')).grid(row=2, column=0, sticky=(N, W, E, S))
ttk.Button(window, text='5', command=lambda: get_eqn('5')).grid(row=2, column=1, sticky=(N, W, E, S))
ttk.Button(window, text='6', command=lambda: get_eqn('6')).grid(row=2, column=2, sticky=(N, W, E, S))
ttk.Button(window, text='1', command=lambda: get_eqn('1')).grid(row=3, column=0, sticky=(N, W, E, S))
ttk.Button(window, text='2', command=lambda: get_eqn('2')).grid(row=3, column=1, sticky=(N, W, E, S))
ttk.Button(window, text='3', command=lambda: get_eqn('3')).grid(row=3, column=2, sticky=(N, W, E, S))
ttk.Button(window, text='0', command=lambda: get_eqn('0')).grid(row=4, column=0, sticky=(N, W, E, S))
ttk.Button(window, text='.', command=lambda: get_eqn('.')).grid(row=4, column=1, sticky=(N, W, E, S))
ttk.Button(window, text='=', command=lambda: get_eqn('=')).grid(row=4, column=2, sticky=(N, W, E, S))
ttk.Button(window, text='/', command=lambda: get_eqn('/')).grid(row=1, column=3, sticky=(N, W, E, S))
ttk.Button(window, text='*', command=lambda: get_eqn('*')).grid(row=2, column=3, sticky=(N, W, E, S))
ttk.Button(window, text='-', command=lambda: get_eqn('-')).grid(row=3, column=3, sticky=(N, W, E, S))
ttk.Button(window, text='+', command=lambda: get_eqn('+')).grid(row=4, column=3, sticky=(N, W, E, S))


#############################
#Getting input from keyboard#
#############################

root.bind('7', lambda x: get_eqn('7'))
root.bind('8', lambda x: get_eqn('8'))
root.bind('9', lambda x: get_eqn('9'))
root.bind('4', lambda x: get_eqn('4'))
root.bind('5', lambda x: get_eqn('5'))
root.bind('6', lambda x: get_eqn('6'))
root.bind('1', lambda x: get_eqn('1'))
root.bind('2', lambda x: get_eqn('2'))
root.bind('3', lambda x: get_eqn('3'))
root.bind('0', lambda x: get_eqn('0'))
root.bind('.', lambda x: get_eqn('.'))
root.bind('/', lambda x: get_eqn('/'))
root.bind('*', lambda x: get_eqn('*'))
root.bind('-', lambda x: get_eqn('-'))
root.bind('+', lambda x: get_eqn('+'))
root.bind('=', lambda x: get_eqn('='))
root.bind('<Return>', lambda x: get_eqn('='))


root.mainloop()
