#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Aug 12 22:50:42 2018

@author: JardielJunior    
"""


import displaySettings
import tkinter as tk

if __name__ == '__main__':

    app = displaySettings.SampleApp()   
    app.title('REL_UFRJ')
#    app.tk.call('wm', 'iconphoto', app._w, tk.PhotoImage(file='poli_ufrj.gif'))
    app.resizable(width=False, height=False)
    app.mainloop()

             
#anaconda_bin = r'C:\Users\Jardiel\Anaconda3\Library\bin'

#for file in os.listdir(anaconda_bin):
#    if 'mkl' in file:
#        print(file)
###
#        shutil.copy2("%s\%s" % (anaconda_bin, file),r'C:\Users\Jardiel\Documents\TCC_Confiabilidade\Dev\build\exe.win-amd64-3.6\%s' % file)