#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 08:30:12 2018

@author: JardielJunior
"""

import numpy as np
import pandas as pd
from scipy import special
from utils import *
import ast
import sympy as sym
import scipy.stats as stats

class ReliabilityStudy(ReadTxt):
    
    def __init__(self, samples=1e6):
        path_variables = path_inputs + '/variables.txt'
        self.variables = []
        ReadTxt.__init__(self, path_variables)
        self.variables_inputs = strToFloat(ast.literal_eval(self.result_txt)[1:]) 
        path_samples = path_inputs + '/monte_carlo_samples.txt'
        ReadTxt.__init__(self, path_samples)
        self.samples = self.result_txt
      
        if self.samples == '':
            self.samples = samples
        else:    
            self.samples = int(float(self.result_txt))
        values = {}
        
        for i in range(len(self.variables_inputs)-1):
            
            if self.variables_inputs[i]['name'] != '':
                exec("{0} = sym.Symbol('{1}')".format(self.variables_inputs[i]['name'], self.variables_inputs[i]['name']))
                
                if self.variables_inputs[i]['type'].upper() == 'NORMAL':
                    
                    if self.variables_inputs[i]['min'] != '' and self.variables_inputs[i]['max'] != '':
                         values[self.variables_inputs[i]['name']] = stats.truncnorm((self.variables_inputs[i]['min']- self.variables_inputs[i]['avg']) / self.variables_inputs[i]['std'], (self.variables_inputs[i]['max']- self.variables_inputs[i]['avg']) / self.variables_inputs[i]['std'], loc=self.variables_inputs[i]['avg'], scale=self.variables_inputs[i]['std']).rvs(int(self.samples))
                         exec("{0} = stats.truncnorm((self.variables_inputs[i]['min']- self.variables_inputs[i]['avg']) / self.variables_inputs[i]['std'], (self.variables_inputs[i]['max']- self.variables_inputs[i]['avg']) / self.variables_inputs[i]['std'], loc=self.variables_inputs[i]['avg'], scale=self.variables_inputs[i]['std']).rvs(int(self.samples))".format(self.variables_inputs[i]['name']))
                         exec("self.{0} = stats.truncnorm((self.variables_inputs[i]['min']- self.variables_inputs[i]['avg']) / self.variables_inputs[i]['std'], (self.variables_inputs[i]['max']- self.variables_inputs[i]['avg']) / self.variables_inputs[i]['std'], loc=self.variables_inputs[i]['avg'], scale=self.variables_inputs[i]['std']).rvs(int(self.samples))".format(self.variables_inputs[i]['name']))
                    else:
                        values[self.variables_inputs[i]['name']] = np.random.normal(float(self.variables_inputs[i]['avg']), float(self.variables_inputs[i]['std']), int(self.samples))
                        exec("{0} = np.random.normal(float(self.variables_inputs[i]['avg']), float(self.variables_inputs[i]['std']), int(self.samples))".format(self.variables_inputs[i]['name']))
                        exec("self.{0} = np.random.normal(float(self.variables_inputs[i]['avg']), float(self.variables_inputs[i]['std']), int(self.samples))".format(self.variables_inputs[i]['name']))               
                elif self.variables_inputs[i]['type'].upper() ==  'GUMBEL': 
                     values[self.variables_inputs[i]['name']] = np.random.gumbel(float(self.variables_inputs[i]['avg']) , float(self.variables_inputs[i]['std']), int(self.samples))
                     beta = (np.sqrt(6)*self.variables_inputs[i]['std'])/np.pi
                     values[self.variables_inputs[i]['name']] = np.random.gumbel(float(self.variables_inputs[i]['avg'] - beta*0.5772157), float(beta), int(self.samples))
#                    values[self.variables_inputs[i]['name']] = np.random.gumbel(float(self.variables_inputs[i]['avg'] - (0.57721*(6*(self.variables_inputs[i]['std'])**2)/(np.pi**2))), float((6*(self.variables_inputs[i]['std'])**2)/np.pi**2 ), int(self.samples))
                     exec("{0} = np.random.gumbel(float(self.variables_inputs[i]['avg'] - beta*0.5772157), float((beta*np.pi)/np.sqrt(6)), int(self.samples))".format(self.variables_inputs[i]['name']))
                     exec("self.{0} = np.random.gumbel(float(self.variables_inputs[i]['avg'] - beta*0.5772157), float((beta*np.pi)/np.sqrt(6)), int(self.samples))".format(self.variables_inputs[i]['name']))
#                     exec("{0} = np.random.gumbel(float(self.variables_inputs[i]['avg']) , float(self.variables_inputs[i]['std']), int(self.samples))".format(self.variables_inputs[i]['name']))

                elif self.variables_inputs[i]['type'].upper() in ['LOG NORMAL', 'LOGNORMAL', 'LN']:
                    values[self.variables_inputs[i]['name']] = np.random.lognormal(float(self.variables_inputs[i]['avg']), float(self.variables_inputs[i]['std']), int(self.samples))
                    exec("{0}  = np.random.lognormal(float(self.variables_inputs[i]['avg']), float(self.variables_inputs[i]['std']), int(self.samples)) ".format(self.variables_inputs[i]['name']))
                    exec("self.{0}  = np.random.lognormal(float(self.variables_inputs[i]['avg']), float(self.variables_inputs[i]['std']), int(self.samples)) ".format(self.variables_inputs[i]['name']))             
                else:
                    raise ('Distribution type not available')
               
        self.values = values
        list_variables = []        
        for i in range(len(self.variables_inputs)-1):
            if self.variables_inputs[i]['name'] == '':
                pass
            else:
                list_variables.append(self.variables_inputs[i]['name'])
        self.list_variables = list_variables
        path_function = path_inputs + '/failureFunction.txt'
        ReadTxt.__init__(self, path_function)
        parseFunction(self.result_txt, list_variables)
        self.string_function = self.result_txt
        self.function = eval(self.result_txt)
#        
#        
        path_check_parametric = path_inputs + '/check_parametric.txt'
        ReadTxt.__init__(self, path_check_parametric)
        self.check_parametric = float(self.result_txt)
        if self.check_parametric == 1.0:    
            self.parametricAnalysis()
#            
    
    def monteCarlo(self):   
       
        failureProbabilityValues = []
        failure = 1
        for i in range(len(self.function)):     
            if np.round(self.function[i],0) <= 0:
                failure = 1
                failureProbabilityValues.append(failure)
            else:
                failure = 0
                failureProbabilityValues.append(failure)
        
        self.failureProbabilityValues = failureProbabilityValues
        failureProbability = sum(failureProbabilityValues)/len(failureProbabilityValues)
        self.failureProbability = failureProbability
        
        beta = stats.norm.ppf(self.failureProbability)
        self.function_std = np.std(self.function)
#        beta = special.ndtri(self.failureProbability)
        self.beta = beta
        self.solution_mean = np.mean(self.function)
        
        df = pd.DataFrame({'Parameters':['Failure Probability', 'Beta', 'Mean', 'Std'], 'Values':
            [self.failureProbability, np.abs(self.beta), self.solution_mean, self.function_std]})
        
        return df
    
    
    def parametricAnalysis(self):
        
        self.live_loads = {}
        self.dead_loads = {}
        self.resistance = {}
        self.resistance_factor = {}
        self.loads_factor = {}
        
        for i in range(len(self.variables_inputs)):
            if self.variables_inputs[i] != {}:
                if self.variables_inputs[i]['name'] != '':
                    if self.variables_inputs[i]['classification'] == look_up_classifications['Live Load']:
                        self.live_loads[self.variables_inputs[i]['name']] = self.values[self.variables_inputs[i]['name']]
                    elif self.variables_inputs[i]['classification'] == look_up_classifications['Dead Load']:
                        self.dead_loads[self.variables_inputs[i]['name']] = self.values[self.variables_inputs[i]['name']]
                    elif self.variables_inputs[i]['classification'] == look_up_classifications['Resistance']:
                        self.resistance[self.variables_inputs[i]['name']] = self.values[self.variables_inputs[i]['name']]
                    elif self.variables_inputs[i]['classification'] == look_up_classifications['Resistance Factor Model']:
                        self.resistance_factor[self.variables_inputs[i]['name']] = self.values[
                            self.variables_inputs[i]['name']]
                    elif self.variables_inputs[i]['classification'] == look_up_classifications['Loads Factor Model']:
                        self.loads_factor[self.variables_inputs[i]['name']] = self.values[
                            self.variables_inputs[i]['name']]

        step_variation = np.linspace(0, 1, 10)
        self.calculateParametricResults()
        self.parametricPfResults = list(map(lambda x: self.getFailure(x), self.parametric_results))
        self.parametricBetaResults = list(map(lambda x: -special.ndtri(x), self.parametricPfResults))
        self.parametricBetaResultsDataFrame = pd.DataFrame({'Beta': self.parametricBetaResults, 'Parameter': step_variation })
        
    
    def calculateParametricResults(self):

        self.parametric_results = []
        step_variation = np.linspace(0, 1, 10)
        for i in range(len(self.variables_inputs) - 1):
            if self.variables_inputs[i]['name'] != '':
                exec("{0} = sym.Symbol('{1}')".format(self.variables_inputs[i]['name'],
                                                      self.variables_inputs[i]['name']))
        for i in range(len(step_variation)):

            for key in list(self.live_loads.keys()):
                if len(self.live_loads.keys()) != 0:
                    exec('{0} = self.live_loads[key] * step_variation[i] '.format(key))

            for key in list(self.dead_loads.keys()):
                if len(self.dead_loads.keys()) != 0:
                    exec('{0} = self.dead_loads[key]* (1-step_variation[i])'.format(key))


            for key in list(self.resistance_factor.keys()):
                exec('{0} = self.resistance_factor[key]'.format(key))
                if len(self.resistance_factor.keys()) != 0:
                    pass

            for key in list(self.resistance.keys()):
                if len(self.resistance.keys()) != 0:
                    exec('{0} = self.resistance[key] '.format(key))

            for key in list(self.loads_factor.keys()):
                if len(self.loads_factor.keys()) != 0:
                    exec('{0} = self.loads_factor[key] '.format(key))


            self.parametric_results.append(eval(self.string_function))


    # @staticmethod

    # def calculateParametricResults(live_loads, dead_loads, resistance):
    #
    #     all_loads = []
    #     print("Calculating Parametric Results...")
    #
    #     for i in range(len(live_loads)):
    #         all_loads.append(live_loads[i] + dead_loads[i])
    #
    #     final_results = []
    #     for i in range(len(live_loads)):
    #         final_results.append(resistance[i] - all_loads[i])
    #
    #     return final_results
    #




    @staticmethod
    def getFailure(results):
        failureProbabilityValues = []
        failure = 0
        for i in range(len(results)):     
            if results[i] < 0:
                failure = 1
                failureProbabilityValues.append(failure)
            else:
                failure = 0
                failureProbabilityValues.append(failure)
        
        failureProbability = sum(failureProbabilityValues)/len(failureProbabilityValues)

        return failureProbability