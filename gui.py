

#https://www.devmedia.com.br/tkinter-interfaces-graficas-em-python/33956
# http://tmetsch.github.io/pytkgen/
#https://github.com/tmetsch/pytkgen/blob/master/examples/rsa_ui.py

try:
    from tkinter.constants import END
except ImportError:
    from Tkinter import END

import tkgen.gengui

if __name__ == '__main__':
    root = tkgen.gengui.TkJson('rsa_ui.json', title='RSA example') 
# basicamente mudar um pouco o exemplo RSA pra ter entrada grafica ER AF GR
# menor prioridade que o core;


# add button behaviour
    root.button('ok', ok)
    root.button('exit', root.destroy)

root.mainloop()
