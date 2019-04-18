#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 15:31:39 2018

@author: JardielJunior
"""


path_inputs = "inputs" 
path_outputs = "outputs"

available_types = ['Normal', 'Gumbel', 'Log Normal', 'Gamma']

look_up_classifications = {'Dead Load':0, 'Live Load': 1,'Resistance': 2, 'Resistance Factor Model': 3,
                           'Loads Factor Model': 4}
classifications = ['Dead Load', 'Live Load', 'Resistance', 'Resistance Factor Model', 'Loads Factor Model']

import sympy as sym
                
class ReadTxt():
    
    def __init__(self, path):
        with open(path, 'r') as _file:
            self.result_txt = _file.read()       
            
            
            
def strToFloat(json_variables):
    
    for i in range(len(json_variables)-1):
        
        for key in json_variables[i].keys():
            if key not in ('type', 'var', 'name'):
                if json_variables[i][key] != '':
                    json_variables[i][key] = float(json_variables[i][key])
                elif key in ('max', 'min'):
                    pass
                else:
                    json_variables[i][key] = 0 
    return json_variables


def parseFunction(failure_function, list_variables):
    
    
    for i in range(len(list_variables)):
        
        exec("{0} = sym.Symbol('{1}')".format(list_variables[i], list_variables[i]))
        
        
        