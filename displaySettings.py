#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Aug 18 13:18:26 2018

@author: JardielJunior
"""

import tkinter as tk
from tkinter import font  as tkfont
import utils
import statisticsAnalysis
from tkinter import ttk
from tabulate import tabulate
import copy
import matplotlib.pyplot as plt
from tkinter import filedialog
#from bokeh.layouts import gridplot
#from bokeh.plotting import figure, show, output_file, save
#from bokeh.io import export_png
import numpy as np
from PIL import ImageTk, Image
#import scipy
import os
import matplotlib
#matplotlib.use('GTKAgg')
import matplotlib.pyplot as plt
#import selenium
#plt.switch_backend("backend")
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)
        self.title_font = tkfont.Font(family='Helvetica', size=25, weight="bold", slant="italic")
      

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
        
    
        
class StartPage(tk.Frame):
    
    def __init__(self, master):
        
        tk.Frame.__init__(self, master)

        start_label = tk.Label(self, text="Reliability Analysis Program - UFRJ")
        page_1_button = tk.Button(self, text="Monte Carlo Simulation",
                                  command=lambda: master.switch_frame(VariablesPage))
            
        welcome_label = tk.Label(self, text = 'Developped by Polytechnic School of the Federal University of Rio de Janeiro')
#        page_2_button = tk.Button(self, text="Parametric Simulation",
#                                  command=lambda: master.switch_frame(ParametricPage))
        
        start_label.pack(side="top", fill="x", pady=10)
        welcome_label.pack(side = "top", fill = 'x', pady = 15)
        page_1_button.pack()

#        page_2_button.pack()


         


class VariablesPage(tk.Frame, statisticsAnalysis.ReliabilityStudy):
    
    def __init__(self, master):
        self.entry_fields = [{}, {'var': 'Variable 1', 'name':'', 'type': '', 'avg': '', 'std': '', 'min': '', 'max': '', 'classification':''}, {'var': 'Variable 2', 'name':'', 'type': '', 'avg': '', 'std': '', 'min': '', 'max': '', 'classification': ''}, {'var': 'Variable 3', 'name':'', 'type': '', 'avg': '', 'std': '', 'min': '', 'max': '' , 'classification': ''}]
        self.fields = [{}, {'var': 'Variable 1', 'name':'', 'type': '', 'avg': '', 'std': '', 'min': '', 'max': '' , 'classification' : ''}, {'var': 'Variable 2', 'name':'', 'type': '', 'avg': '', 'std': '', 'min': '', 'max': '', 'classification' :'' }, {'var': 'Variable 3', 'name':'', 'type': '', 'avg': '', 'std': '', 'min': '', 'max': '', 'classification': ''}]

        tk.Frame.__init__(self, master)
        page_1_label = tk.Label(self, text= "Variables Parameters")  
        page_1_label.grid(row = 0, column = 2)
        self.start_button = tk.Button(self, text="Back", command=lambda: master.switch_frame(StartPage))
        variable_name = tk.Label(self, text= 'Variable Name')
        variable_name.grid(row = 1, column = 2)
        distribution_type = tk.Label(self, text = 'Distribution Type')
        distribution_type.grid(row = 1, column = 3)
        variable_mean = tk.Label(self, text = 'Variable Average')
        variable_mean.grid(row = 1, column = 4)
        variable_std = tk.Label(self, text = 'Variable Std')
        variable_std.grid(row = 1, column = 5) 
        sample_label = tk.Label(self, text = 'Monte Carlo Samples')
        sample_label.grid(row = 0, column = 3)
        self.n_sample = tk.Entry(self, width = 5)
        self.n_sample.grid(row = 0, column = 4, padx = 4, pady  =4 )
        bins_label = tk.Label(self, text = 'Number of Bins')
        bins_label.grid(row = 0, column = 5)
        self.n_bins = tk.Entry(self, width = 5)
        self.n_bins.grid(row = 0, column = 6)
        min_label = tk.Label(self, text = 'Min')
        min_label.grid(row = 1, column = 6)
        max_label = tk.Label(self, text = 'Max')
        max_label.grid(row = 1, column = 7)
        variable_class = tk.Label(self, text = 'Classification')
        variable_class.grid(row = 1, column = 8)
        
    
        self.parametric_check = tk.IntVar()
        parametric_button = tk.Checkbutton(self, text = "Parametric Study", variable = self.parametric_check)
        parametric_button.grid(row = 0, column = 7)
        

        n = 1
        lb1 = tk.Label(self, text="Variable 1")
        lb1.grid(row = 2, column = 1)       
        self.entry_fields[n]['name'] = tk.Entry(self, textvariable = self.entry_fields[n]['name'],  width = 7)
        self.entry_fields[n]['name'].grid(row = 2, column = 2)
        self.entry_fields[n]['type'] = tk.StringVar(self)
        self.entry_fields[n]['type'].set('Normal')  
        dropMenu1 = tk.OptionMenu(self, self.entry_fields[n]['type'], *utils.available_types)     
        dropMenu1.grid(row = 2, column = 3)   
        self.entry_fields[n]['avg'] = tk.Entry(self, textvariable=self.entry_fields[n]['avg'],  width = 7)
        self.entry_fields[n]['avg'].grid(row = 2, column = 4)
        self.entry_fields[n]['std'] = tk.Entry(self, textvariable=self.entry_fields[n]['std'],  width = 7)
        self.entry_fields[n]['std'].grid(row = 2, column = 5)
        self.entry_fields[n]['min'] = tk.Entry(self, textvariable = self.entry_fields[n]['min'],  width = 7)
        self.entry_fields[n]['min'].grid(row=2, column = 6)
        self.entry_fields[n]['max'] = tk.Entry(self, textvariable = self.entry_fields[n]['max'],  width = 7)
        self.entry_fields[n]['max'].grid(row=2, column = 7)
        self.entry_fields[n]['classification'] = tk.StringVar(self)
        self.entry_fields[n]['classification'].set('Resistance')           
        drop_class_3 = tk.OptionMenu(self, self.entry_fields[n]['classification'], *utils.classifications)
        drop_class_3.grid(row=2, column = 8)
        
        
        n = 2
        lb2 = tk.Label(self, text="Variable 2")     
        lb2.grid(row=3, column = 1)     
        self.entry_fields[n]['name'] = tk.Entry(self, textvariable = self.entry_fields[n]['name'], width = 7)
        self.entry_fields[n]['name'].grid(row = 3, column = 2)
        self.entry_fields[n]['type'] = tk.StringVar(self)    
        dropMenu2 = tk.OptionMenu(self, self.entry_fields[n]['type'], *utils.available_types)
        self.entry_fields[n]['type'].set('Normal')
        dropMenu2.grid(row = 3, column = 3)
        self.entry_fields[n]['avg'] = tk.Entry(self, textvariable=self.entry_fields[n]['avg'], width = 7)
        self.entry_fields[n]['avg'].grid(row = 3, column = 4)
        self.entry_fields[n]['std'] = tk.Entry(self, textvariable=self.entry_fields[n]['std'], width = 7)
        self.entry_fields[n]['std'].grid(row = 3, column = 5)
        self.entry_fields[n]['min'] = tk.Entry(self, textvariable = self.entry_fields[n]['min'], width = 7)
        self.entry_fields[n]['min'].grid(row=3, column = 6)
        self.entry_fields[n]['max'] = tk.Entry(self, textvariable = self.entry_fields[n]['max'], width = 7)
        self.entry_fields[n]['max'].grid(row=3, column = 7)
        self.entry_fields[n]['classification'] = tk.StringVar(self)
        self.entry_fields[n]['classification'].set('Resistance')           
        drop_class_3 = tk.OptionMenu(self, self.entry_fields[n]['classification'], *utils.classifications)
        drop_class_3.grid(row=3, column = 8)       
        
        
        
        n = 3
        lb3 = tk.Label(self, text="Variable 3")
        lb3.grid(row=4, column = 1)   
        self.entry_fields[n]['name'] = tk.Entry(self, textvariable = self.entry_fields[n]['name'], width = 7)        
        self.entry_fields[n]['name'].grid(row=4, column = 2)
        self.entry_fields[n]['type'] = tk.StringVar(self)
        self.entry_fields[n]['type'].set('Normal')
        dropMenu3 = tk.OptionMenu(self, self.entry_fields[n]['type'], *utils.available_types)
        dropMenu3.grid(row = 4, column = 3) 
        self.entry_fields[n]['avg'] = tk.Entry(self,  textvariable=self.entry_fields[n]['avg'], width = 7)
        self.entry_fields[n]['avg'].grid(row = 4, column = 4) 
        self.entry_fields[n]['std'] = tk.Entry(self, textvariable=self.entry_fields[n]['std'], width = 7)
        self.entry_fields[n]['std'].grid(row = 4, column = 5) 
        self.entry_fields[n]['min'] = tk.Entry(self, textvariable = self.entry_fields[n]['min'], width = 7)
        self.entry_fields[n]['min'].grid(row=4, column = 6)
        self.entry_fields[n]['max'] = tk.Entry(self, textvariable = self.entry_fields[n]['max'], width = 7)
        self.entry_fields[n]['max'].grid(row=4, column = 7)
        self.entry_fields[n]['classification'] = tk.StringVar(self)
        self.entry_fields[n]['classification'].set('Resistance')           
        drop_class_3 = tk.OptionMenu(self, self.entry_fields[n]['classification'], *utils.classifications)
        drop_class_3.grid(row=4, column = 8)        
        
        
        self.function_button = tk.Button(self, text = 'Insert Failure Function', command=lambda: self.getFailureFunction()) 
        self.add_variable = tk.Button(self, text="Add Variable", command = self.add_field)
        self.write_variables = tk.Button(self, text = 'Write parameters', command = lambda: self.send_toTxt())
        self.analysisButton = tk.Button(self, text = 'Analysis', command = lambda: self.analysisPage())
        
        self.add_field()
        self.add_variable.bind("<Return>", self.add_field)
        self.add_variable.grid(row=len(self.entry_fields)+1, column = 3, padx=4, pady=6, sticky="W")
        self.start_button.grid(row = len(self.entry_fields) + 1, column = 2)
        self.function_button.grid(row = len(self.entry_fields)+1, column = 4)
        self.write_variables.grid(row = len(self.entry_fields)+1, column = 5)
        self.analysisButton.grid(row = len(self.entry_fields)+1, column = 6)
    
 
    def send_toTxt(self):
        send = [None] * len(self.entry_fields)
        for i in range(len(send)):
            send[i] = {}
        for i in range(len(self.entry_fields)):  

            for key in self.entry_fields[i].keys():   
                send[i][key] = None
                if key not in ('name', 'var'):
                       
                    if key not in ('classification'):                     
                        send[i][key] = self.entry_fields[i][key].get()
                  
                    else :

                        send[i][key] = utils.look_up_classifications[self.entry_fields[i][key].get()]
    
                elif key  == 'var':
                    self.entry_fields[i][key] = 'Variable {0}'.format(i)
                    send[i][key] = 'Variable {0}'.format(i)
                else:
                    if type(self.entry_fields[i][key]) != str:
                        send[i][key] = self.entry_fields[i][key].get()
        
        if not(os.path.isdir(utils.path_inputs)):
            os.mkdir(utils.path_inputs)
            
#        print(send)                        
#        if os.path.isdir(utils.path_inputs + '/variables.txt'):
#            os.mkdir(utils.path_inputs + '/variables.txt')
#            
        with open(utils.path_inputs + '/variables.txt', 'w') as _file:
            _file.write(str(send))
        
        
        if self.n_sample.get() == '':
            top_sample_message = tk.Toplevel(self)
            sample_message = tk.Label(top_sample_message, text = 'Using 1.000.000 as SMC sample')
            sample_message.grid(row = 1, column = 1)
            
            
#        if not(os.path.isdir(utils.path_inputs + '/monte_carlo_samples.txt')):
#            os.mkdir(utils.path_inputs + '/monte_carlo_samples.txt')
        with open(utils.path_inputs + '/monte_carlo_samples.txt', 'w') as _file:
            _file.write(str(self.n_sample.get()))
            
        
#        if os.path.isdir(utils.path_inputs + '/n_bins_chart.txt'):
#            os.mkdir(utils.path_inputs + '/n_bins_chart.txt')    
#            
        with open(utils.path_inputs + '/n_bins_chart.txt', 'w') as _file:
            _file.write(str(self.n_bins.get()))
            
        
#        if os.path.isdir(utils.path_inputs + '/check_parametric.txt'):
#            os.mkdir(utils.path_inputs + '/check_parametric.txt')
            
        with open(utils.path_inputs + '/check_parametric.txt', 'w') as _file:
            print(self.parametric_check.get())
            _file.write(str(self.parametric_check.get()))
    
    

    def add_field(self):
       
        self.fields.append({})
        self.entry_fields.append({})
#        print(self.entry_fields)
#        print(len(self.fields)-1)
        print("Reading all the inputs ")
        n = len(self.entry_fields)-1
           
        self.entry_fields[n-1]['var'] = tk.StringVar(self)
        self.entry_fields[n-1]['var'] = tk.Label(self, text = 'Variable {0}'.format(n-1))
        self.entry_fields[n-1]['var'].grid(row = n, column =1)
        self.entry_fields[n-1]['name'] = tk.StringVar(self)
        self.entry_fields[n-1]['name'] = tk.Entry(self, textvariable = self.entry_fields[n-1]['name'], width = 7)
        self.entry_fields[n-1]['name'].grid(row=n, column=2)
         
        self.entry_fields[n-1]['type'] = tk.StringVar(self)
        self.entry_fields[n-1]['type'].set('Normal')
         
        dropMenuN = tk.OptionMenu(self, self.entry_fields[n-1]['type'], *utils.available_types)
        dropMenuN.grid(row = n, column = 3)
        
        
        self.entry_fields[n-1]['avg'] = tk.StringVar(self)
        self.entry_fields[n-1]['avg'] = tk.Entry(self, textvariable = self.entry_fields[n-1]['avg'], width = 7)
        self.entry_fields[n-1]['avg'].grid(row = n, column = 4)
           
        self.entry_fields[n-1]['std'] = tk.StringVar(self)
        self.entry_fields[n-1]['std'] = tk.Entry(self, textvariable = self.entry_fields[n-1]['std'], width = 7)
        self.entry_fields[n-1]['std'].grid(row = n, column = 5)

        self.entry_fields[n-1]['min'] = tk.StringVar(self)
        self.entry_fields[n-1]['min'] = tk.Entry(self, textvariable = self.entry_fields[n-1]['min'], width = 7)
        self.entry_fields[n-1]['min'].grid(row=n, column = 6)
        self.entry_fields[n-1]['max'] = tk.StringVar(self)
        self.entry_fields[n-1]['max'] = tk.Entry(self, textvariable = self.entry_fields[n-1]['max'], width = 7)
        self.entry_fields[n-1]['max'].grid(row=n, column = 7)
        
        self.entry_fields[n-1]['classification'] = tk.StringVar(self)
        self.entry_fields[n-1]['classification'].set('Resistance')   
        drop_class_N = tk.OptionMenu(self, self.entry_fields[n-1]['classification'], *utils.classifications)
        drop_class_N.grid(row=n, column = 8)        
    
    
        if n:
           self.write_variables.grid(row = n + 1)
           self.add_variable.grid(row=n + 1, column=3, padx=4, pady=6, sticky="W")
           self.start_button.grid(row = n + 1)
           self.function_button.grid(row = n + 1)
           self.analysisButton.grid(row = n +1)

           
   
    def getFailureFunction(self):
        top_function = tk.Toplevel()
        self.label_function = tk.Label(top_function, text = 'Failure Function = ')
        self.label_function.grid(row = 3, column = 1)
        self.writeFunction = tk.Button(top_function, text = 'Write Function', command = lambda: self.sendFunctionTxt())
        self.writeFunction.grid(row = 5, column = 3)
        self.failure_function = tk.Entry(top_function, textvariable = 'Failure Function')
        self.failure_function.grid(row = 3, column = 2, ipadx =200,
                                   ipady = 20)
        
        

    def sendFunctionTxt(self):

        print("Failure Function: {0}".format(str(self.failure_function.get())))
        
        if not(os.path.isdir(utils.path_inputs)):
            os.mkdir(utils.path_inputs)
        
#        if os.path.isdir(utils.path_inputs + '/failureFunction.txt'):
#            os.mkdir(utils.path_inputs + '/FailureFunction.txt')
        with open(utils.path_inputs + '/failureFunction.txt', 'w') as _file:
            if self.failure_function.get() != '':
                _file.write(str(self.failure_function.get()))
                _file.close()

        
    def analysisPage(self):
        self.top_analysis = tk.Toplevel()
        analysisLabel = tk.Label(self.top_analysis, text="Monte Carlo Results")
        analysisLabel.grid(row = 1, column = 1)
        statisticsAnalysis.ReliabilityStudy.__init__(self)
        self.saveOutputs()
        self.displayResults()
        

        
    def plotParametricResults(self):
        pass
        
        
        
        
    def displayResults(self):
        monteCarloResultsLabel = tk.Label(self.top_analysis, text = tabulate(self.monteCarlo().set_index('Parameters')))
        monteCarloResultsLabel.grid(row = 1, column = 4)
    
    def saveOutputs(self):
        utils.ReadTxt.__init__(self, utils.path_inputs + '/n_bins_chart.txt')
        self.number_bins = self.result_txt
        self.top_selectFile = tk.Toplevel()
        ask_saveOutputs = tk.Label(self.top_selectFile, text = 'Do you want to save the output in an specific file?')
        ask_saveOutputs.grid(row = 1, column = 2)
        save_outputs_yes = tk.Button(self.top_selectFile, text = 'Yes', command = lambda: self.selectFile())
        save_outputs_yes.grid(row = 2, column = 1)
        save_outputs_no = tk.Button(self.top_selectFile, text = 'No', command = lambda: self.dontSelectFile())
        save_outputs_no.grid(row = 2, column = 2)


        
    def dontSelectFile(self):
        if not(os.path.isdir(utils.path_outputs)):
            os.mkdir(utils.path_outputs)

        self.top_selectFile.destroy()
        
        print("Saving Outputs on the working directory")
        
        def getVariableInfo(variables_inputs, key):
            for i in range(len(variables_inputs)):
                if variables_inputs[i] != {}:
                    if variables_inputs[i]['name'] == key:
                        info = (variables_inputs[i]['avg'],variables_inputs[i]['std'])
            return info
                
        if self.number_bins == '':
            n_bins = 1000
        else:
            self.number_bins = int(float(self.result_txt))
            n_bins = self.number_bins
        
        
        print("Outputs Saved!")
#        self.top_progressbar = tk.Toplevel()
        
#        progress = ttk.Progressbar(self.top_progressbar)
#        
#        progress.grid(column = 0, row = 0)
        
        for key in self.values.keys():
            
            if key != '':
                    
        
                    plt.figure()
                    plt.title('{0} distribution'.format(key))
                    plt.xlabel('Variable Value')
                    plt.ylabel('Absolute Frequency')
                    plt.hist(self.values[key], bins = n_bins)
                    plt.savefig(utils.path_outputs + '\{0} distribution'.format(key))
#                
                
                
#                    plt.show()
#                    p1 = figure(title="{0} Distribution (μ={1}, σ={2})".format(key, getVariableInfo(self.variables_inputs, key)[0], getVariableInfo(self.variables_inputs, key)[1]),tools="save", background_fill_color="#E8DDCB")
#                    mu = getVariableInfo(self.variables_inputs, key)[0]
#                    sigma = getVariableInfo(self.variables_inputs, key)[1]                                  
#                    measured = np.random.normal(mu, sigma, 1000)
#                    hist, edges = np.histogram(measured, density=True, bins=50)
#                    hist = hist *100
#                    x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
#                    pdf = 1/(sigma * np.sqrt(2*np.pi)) * np.exp(-(x-mu)**2 / (2*sigma**2))*100
#                    cdf = (1+scipy.special.erf((x-mu)/np.sqrt(2*sigma**2)))/2                    
#                    p1.quad(top=max(hist), bottom=0, left=edges[:-1], right=edges[1:], fill_color="#036564", line_color="#033649")
#                    p1.line(x, pdf, line_color="#D95B43", line_width=8, alpha=0.7, legend="PDF")
#                    p1.line(x, cdf, line_color="white", line_width=2, alpha=0.7, legend="CDF")
#                    p1.legend.location = "center_right"
#                    p1.legend.background_fill_color = "darkgrey"
#                    p1.xaxis.axis_label = 'x'
#                    p1.yaxis.axis_label = 'Pr(x)'
#                    if not(os.path.isdir('otherPlots')):
#                        os.mkdir('otherPlots')
#                    options = selenium.webdriver.ChromeOptions()
#
#                    export_png(p1, filename="otherPlots/{0} Distribution.png".format(key))


#
        fig = plt.figure()    
        plt.title('Failure Function distribution')
        plt.xlabel('Function Value')
        plt.ylabel('Absolute Frequency')
        plt.hist(self.function, bins = n_bins)
        plt.savefig(utils.path_outputs + '\Solution')
#        plt.show()
        
        if self.check_parametric == 1.0:
            print("Getting Prepared for the Parametric Study")
#            self.plotParametricResults()
            plt.figure()
            plt.plot(self.parametricBetaResultsDataFrame['Parameter'], self.parametricBetaResultsDataFrame['Beta'])
            plt.title('Parametric Analysis')
            plt.savefig(utils.path_outputs + '\ParametricAnalysis')
            self.parametricBetaResultsDataFrame.to_excel(utils.path_outputs + '\ParametricAnalysisDataFrame.xlsx')
            plt.figure()
            plt.plot(self.x_smooth, self.y_smooth)
            plt.savefig(utils.path_outputs + '\ParametricAnalysisSmoothed')
            
        
    def selectFile(self):
        self.top_selectFile.destroy()
        self.folder_selected =  filedialog.askdirectory()
        print("Saving Outputs on the following folder {0}".format(self.folder_selected))

        
        if self.number_bins == '':
            n_bins = 1000
        else:
            self.number_bins = int(float(self.result_txt))
            n_bins = self.number_bins
            
        for key in self.values.keys():
            if key != '':
                fig = plt.figure()
                plt.title('{0} distribution'.format(key))
                plt.xlabel('Variable Value')
                plt.ylabel('Absolute Frequency')
                plt.hist(self.values[key], bins = n_bins)
                plt.savefig(self.folder_selected + '\{0} distribution'.format(key))
#                print(self.folder_selected)
#                plt.show()
        
        print("Outputs Saved!")

        plt.figure()
        plt.title('Failure Function distribution')
        plt.xlabel('Function Value')
        plt.ylabel('Absolute Frequency')
        plt.hist(self.function, bins = n_bins)
        plt.savefig(self.folder_selected + '\Solution')
#        plt.show()
         
        if self.check_parametric == 1.0:
            print("Getting Prepared for the Parametric Study")
#            self.plotParametricResults()
            plt.figure()
            plt.plot(self.parametricBetaResultsDataFrame['Parameter'], self.parametricBetaResultsDataFrame['Beta'])
            plt.title('Parametric Analysis')
            plt.savefig(self.folder_selected + '\ParametricAnalysis')
            self.parametricBetaResultsDataFrame.to_excel(self.folder_selected + '\ParametricAnalysisDataFrame.xlsx')


    def plotSolution(self):
        
        
        if self.folder_selected in locals():
                   
            for key in self.values.keys():
                if key != '':
#                    plt.figure()
                    plt.title('{0} distribution'.format(key))
                    plt.xlabel('Variable Value')
                    plt.ylabel('Absolute Frequency')
                    plt.hist(self.values[key], bins = 50)
                    plt.savefig(self.folder_selected + '{0} distribution'.format(key))
#                    plt.show()
                    
#            plt.figure()
            plt.title('{0} distribution'.format(self.result_txt))
            plt.xlabel('Function Value')
            plt.ylabel('Absolute Frequency')
            plt.hist(self.function, bins = 50)
            plt.savefig(self.folder_selected + 'Solution')
#            plt.show()
        
        else:
             
            for key in self.values.keys():
                if key != '':
#                    plt.figure()
                    plt.title('{0} distribution'.format(key))
                    plt.xlabel('Variable Value')
                    plt.ylabel('Absolute Frequency')
                    plt.hist(self.values[key], bins = 50)
                    plt.savefig('{0} distribution'.format(key))
#                    plt.show()
                    
#            plt.figure()
            plt.title('{0} distribution'.format(self.result_txt))
            plt.xlabel('Function Value')
            plt.ylabel('Absolute Frequency')
            plt.hist(self.function, bins = 50)
            plt.savefig( 'Solution')
#            plt.show()
            if self.check_parametric == 1.0:
                print("Getting Prepared for the Parametric Study")
    #            self.plotParametricResults()
                plt.figure()
                plt.plot(self.parametricBetaResultsDataFrame['Parameter'], self.parametricBetaResultsDataFrame['Beta'])
                plt.title('Parametric Analysis')
                plt.savefig(self.folder_selected + '\ParametricAnalysis')
                plt.figure()
                plt.plot(self.x_smooth, self.y_smooth)
                plt.savefig(utils.path_outputs + '\ParametricAnalysisSmoothed')


class ParametricPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        page_2_label = tk.Label(self, text="Parametric Simulation")
        self.start_button = tk.Button(self, text="Back",
                                 command=lambda: master.switch_frame(StartPage))
        

        self.entry_fields = [{}, {'var': 'Variable 1', 'name':'', 'type': '', 'avg': '', 'std': '', 'min': '', 'max': '', 'classification':''}, {'var': 'Variable 2', 'name':'', 'type': '', 'avg': '', 'std': '', 'min': '', 'max': '', 'classification': ''}, {'var': 'Variable 3', 'name':'', 'type': '', 'avg': '', 'std': '', 'min': '', 'max': '' , 'classification': ''}]
        self.fields = [{}, {'var': 'Variable 1', 'name':'', 'type': '', 'avg': '', 'std': '', 'min': '', 'max': '' , 'classification' : ''}, {'var': 'Variable 2', 'name':'', 'type': '', 'avg': '', 'std': '', 'min': '', 'max': '', 'classification' :'' }, {'var': 'Variable 3', 'name':'', 'type': '', 'avg': '', 'std': '', 'min': '', 'max': '', 'classification': ''}]
        page_1_label = tk.Label(self, text= "Variables Parameters")  
        page_1_label.grid(row = 0, column = 2)
        variable_name = tk.Label(self, text= 'Variable Name')
        variable_name.grid(row = 1, column = 2)
        distribution_type = tk.Label(self, text = 'Distribution Type')
        distribution_type.grid(row = 1, column = 3)
        variable_mean = tk.Label(self, text = 'Variable Average')
        variable_mean.grid(row = 1, column = 4)
        variable_std = tk.Label(self, text = 'Variable Std')
        variable_std.grid(row = 1, column = 5) 
        
        sample_label = tk.Label(self, text = 'Monte Carlo Sample')
        sample_label.grid(row = 0, column = 3)
        self.n_sample = tk.Entry(self, width = 5)
        self.n_sample.grid(row = 0, column = 4)
        bins_label = tk.Label(self, text = 'Number of Bins')
        bins_label.grid(row = 0, column = 5)
        self.n_bins = tk.Entry(self, width = 5)
        self.n_bins.grid(row = 0, column = 6)
        min_label = tk.Label(self, text = 'Min')
        min_label.grid(row = 1, column = 6)
        max_label = tk.Label(self, text = 'Max')
        max_label.grid(row = 1, column = 7)
        variable_class = tk.Label(self, text = 'Classification')
        variable_class.grid(row = 1, column = 8)
        
        
        
        n = 1
        lb1 = tk.Label(self, text="Variable 1")
        lb1.grid(row = 2, column = 1)       
        self.entry_fields[n]['name'] = tk.Entry(self, textvariable = self.entry_fields[n]['name'], width = 7)
        self.entry_fields[n]['name'].grid(row = 2, column = 2)
        self.entry_fields[n]['type'] = tk.StringVar(self)
        self.entry_fields[n]['type'].set('Normal')  
        dropMenu1 = tk.OptionMenu(self, self.entry_fields[n]['type'], *utils.available_types)     
        dropMenu1.grid(row = 2, column = 3)   
        self.entry_fields[n]['avg'] = tk.Entry(self, textvariable=self.entry_fields[n]['avg'], width = 7)
        self.entry_fields[n]['avg'].grid(row = 2, column = 4)
        self.entry_fields[n]['std'] = tk.Entry(self, textvariable=self.entry_fields[n]['std'], width = 7)
        self.entry_fields[n]['std'].grid(row = 2, column = 5)
        self.entry_fields[n]['min'] = tk.Entry(self, textvariable = self.entry_fields[n]['min'], width = 7)
        self.entry_fields[n]['min'].grid(row=2, column = 6)
        self.entry_fields[n]['max'] = tk.Entry(self, textvariable = self.entry_fields[n]['max'], width = 7)
        self.entry_fields[n]['max'].grid(row=2, column = 7)
        self.entry_fields[n]['classification'] = tk.StringVar(self)
        self.entry_fields[n]['classification'].set('Resistance')      

        drop_class_1 = tk.OptionMenu(self, self.entry_fields[n]['classification'], *utils.classifications)
        drop_class_1.grid(row=2, column = 8)
        
        n = 2
        lb2 = tk.Label(self, text="Variable 2")     
        lb2.grid(row=3, column = 1)     
        self.entry_fields[n]['name'] = tk.Entry(self, textvariable = self.entry_fields[n]['name'], width = 7)
        self.entry_fields[n]['name'].grid(row = 3, column = 2)
        self.entry_fields[n]['type'] = tk.StringVar(self)    
        dropMenu2 = tk.OptionMenu(self, self.entry_fields[n]['type'], *utils.available_types)
        self.entry_fields[n]['type'].set('Normal')
        dropMenu2.grid(row = 3, column = 3)
        self.entry_fields[n]['avg'] = tk.Entry(self, textvariable=self.entry_fields[n]['avg'], width = 7)
        self.entry_fields[n]['avg'].grid(row = 3, column = 4)
        self.entry_fields[n]['std'] = tk.Entry(self, textvariable=self.entry_fields[n]['std'], width = 7)
        self.entry_fields[n]['std'].grid(row = 3, column = 5)
        self.entry_fields[n]['min'] = tk.Entry(self, textvariable = self.entry_fields[n]['min'], width = 7)
        self.entry_fields[n]['min'].grid(row=3, column = 6)
        self.entry_fields[n]['max'] = tk.Entry(self, textvariable = self.entry_fields[n]['max'], width = 7)
        self.entry_fields[n]['max'].grid(row=3, column = 7)
        self.entry_fields[n]['classification'] = tk.StringVar(self)
        self.entry_fields[n]['classification'].set('Resistance')   
        drop_class_2 = tk.OptionMenu(self, self.entry_fields[n]['classification'], *utils.classifications)
        drop_class_2.grid(row=3, column = 8)
        
        
       
        
        n = 3
        lb3 = tk.Label(self, text="Variable 3")
        lb3.grid(row=4, column = 1)   
        self.entry_fields[n]['name'] = tk.Entry(self, textvariable = self.entry_fields[n]['name'], width = 7)        
        self.entry_fields[n]['name'].grid(row=4, column = 2)
        self.entry_fields[n]['type'] = tk.StringVar(self)
        self.entry_fields[n]['type'].set('Normal')
        dropMenu3 = tk.OptionMenu(self, self.entry_fields[n]['type'], *utils.available_types)
        dropMenu3.grid(row = 4, column = 3) 
        self.entry_fields[n]['avg'] = tk.Entry(self,  textvariable=self.entry_fields[n]['avg'], width = 7)
        self.entry_fields[n]['avg'].grid(row = 4, column = 4) 
        self.entry_fields[n]['std'] = tk.Entry(self, textvariable=self.entry_fields[n]['std'], width = 7)
        self.entry_fields[n]['std'].grid(row = 4, column = 5) 
        self.entry_fields[n]['min'] = tk.Entry(self, textvariable = self.entry_fields[n]['min'], width = 7)
        self.entry_fields[n]['min'].grid(row=4, column = 6)
        self.entry_fields[n]['max'] = tk.Entry(self, textvariable = self.entry_fields[n]['max'], width = 7)
        self.entry_fields[n]['max'].grid(row=4, column = 7)
        self.entry_fields[n]['classification'] = tk.StringVar(self)
        self.entry_fields[n]['classification'].set('Resistance')           
        drop_class_3 = tk.OptionMenu(self, self.entry_fields[n]['classification'], *utils.classifications)
        drop_class_3.grid(row=4, column = 8)
        
        
        
        self.function_button = tk.Button(self, text = 'Insert Failure Function', command=lambda: self.getFailureFunction()) 
        self.add_variable = tk.Button(self, text="Add Variable", command = self.add_field)
        self.write_variables = tk.Button(self, text = 'Write parameters', command = lambda: self.send_toTxt())
        self.analysisButton = tk.Button(self, text = 'Analysis', command = lambda: self.analysisPage())
        
        self.add_field()
        self.add_variable.bind("<Return>", self.add_field)
        self.add_variable.grid(row=len(self.entry_fields) + 1, column = 3, padx=4, pady=6, sticky="W")
        self.start_button.grid(row = len(self.entry_fields) + 1, column = 2)
        self.function_button.grid(row = len(self.entry_fields)+1, column = 4)
        self.write_variables.grid(row = len(self.entry_fields)+1, column = 5)
        self.analysisButton.grid(row = len(self.entry_fields)+1, column = 6)
    
    
    def add_field(self):
       
        self.fields.append({})
        self.entry_fields.append({})
        print(self.entry_fields)
        print(len(self.fields)-1)   
        n = len(self.entry_fields)-1
        
           
        self.entry_fields[n-1]['var'] = tk.StringVar(self)
        self.entry_fields[n-1]['var'] = tk.Label(self, text = 'Variable {0}'.format(n-1))
        self.entry_fields[n-1]['var'].grid(row = n, column =1)
        self.entry_fields[n-1]['name'] = tk.StringVar(self)
        self.entry_fields[n-1]['name'] = tk.Entry(self, textvariable = self.entry_fields[n-1]['name'], width = 7)
        self.entry_fields[n-1]['name'].grid(row=n, column=2)
         
        self.entry_fields[n-1]['type'] = tk.StringVar(self)
        self.entry_fields[n-1]['type'].set('Normal')
         
        dropMenuN = tk.OptionMenu(self, self.entry_fields[n-1]['type'], *utils.available_types)
        dropMenuN.grid(row = n, column = 3)
        
        
        self.entry_fields[n-1]['avg'] = tk.StringVar(self)
        self.entry_fields[n-1]['avg'] = tk.Entry(self, textvariable = self.entry_fields[n-1]['avg'], width = 7)
        self.entry_fields[n-1]['avg'].grid(row = n, column = 4)
           
        self.entry_fields[n-1]['std'] = tk.StringVar(self)
        self.entry_fields[n-1]['std'] = tk.Entry(self, textvariable = self.entry_fields[n-1]['std'], width = 7)
        self.entry_fields[n-1]['std'].grid(row = n, column = 5)
        self.entry_fields[n-1]['min'] = tk.StringVar(self)

        self.entry_fields[n-1]['min'] = tk.Entry(self, textvariable = self.entry_fields[n-1]['min'], width = 7)
        self.entry_fields[n-1]['min'].grid(row=n, column = 6)
        self.entry_fields[n-1]['max'] = tk.StringVar(self)

        self.entry_fields[n-1]['max'] = tk.Entry(self, textvariable = self.entry_fields[n-1]['max'], width = 7)
        self.entry_fields[n-1]['max'].grid(row=n, column = 7)
        self.entry_fields[n-1]['classification'] = tk.StringVar(self)
        self.entry_fields[n-1]['classification'].set('Resistance')   
        drop_class_N = tk.OptionMenu(self, self.entry_fields[n-1]['classification'], *utils.classifications)
        drop_class_N.grid(row=n, column = 8)        
    
        
        if n:
           self.write_variables.grid(row = n + 1)
           self.add_variable.grid(row=n + 1, column=3, padx=4, pady=6, sticky="W")
           self.start_button.grid(row = n + 1)
           self.function_button.grid(row = n + 1)
           self.analysisButton.grid(row = n +1)
           
           
    def send_toTxt(self):
        send = [None] * len(self.entry_fields)
        for i in range(len(send)):
            send[i] = {}
        for i in range(len(self.entry_fields)):  

            for key in self.entry_fields[i].keys():   
                send[i][key] = None
                if key not in ('name', 'var'):
                    send[i][key] = self.entry_fields[i][key].get()
    
                elif key  == 'var':
                    self.entry_fields[i][key] = 'Variable {0}'.format(i)
                    send[i][key] = 'Variable {0}'.format(i)
                else:
                    if type(self.entry_fields[i][key]) != str:
                        self.entry_fields[i][key].get()
                        send[i][key] = self.entry_fields[i][key].get()
        
        print(send)                        
        with open(utils.path_inputs + 'parametricStudy/variables.txt', 'w') as _file:
            _file.write(str(send))
        
        
        if self.n_sample.get() == '':
            top_sample_message = tk.Toplevel(self)
            sample_message = tk.Label(top_sample_message, text = 'Using 1.000.000 as SMC sample')
            sample_message.grid(row = 1, column = 1)

        with open(utils.path_inputs + 'parametricStudy/monte_carlo_samples.txt', 'w') as _file:
            _file.write(str(self.n_sample.get()))
            
        with open(utils.path_inputs + 'parametricStudy/n_bins_chart.txt', 'w') as _file:
            _file.write(str(self.n_bins.get()))
    
        

        
        
