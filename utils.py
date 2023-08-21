import yaml
from exceptions import LoanStatException
import scipy
from scipy.stats import shapiro
import numpy as np
import os,sys

class utils:
    
    def read_yaml_file(file_path: str) -> dict:
        try:
            with open(file_path, "rb") as yaml_file:
                return yaml.safe_load(yaml_file)
        except Exception as e:
            raise LoanStatException(e, sys) from e
            
    
    def perform_ttest_ind_samples(self, sample1 : np.array, sample2 : np.array):
    
        """
        Function to perform t-test for individual samples
        """
        try:
            stat, p_value = scipy.stats.ttest_ind(sample1, sample2)
            print('Statistics=%.3f, p=%.3f' % (stat, p_value))
            if p_value > 0.05:
                print('average annual incomes of the residents of West Virginia and New Mexico have same distribution')
            else:
                print('average annual incomes of the residents of West Virginia and New Mexico have different distribution')
                
        except Exception as e:
            raise LoanStatException(e, sys) from e
            
     
    def perform_mannwhitneyu(self, sample1 : np.array, sample2 : np.array):
        """
        Function to perform mannwhitneyu test for individual samples
        """
        try:
            stat, p_value = scipy.stats.mannwhitneyu(sample1, sample2)
            print('Statistics=%.3f, p=%.3f' % (stat, p_value))
            if p_value > 0.05:
                print('average annual incomes of the residents of West Virginia and New Mexico have same distribution')
            else:
                print('average annual incomes of the residents of West Virginia and New Mexico have different distribution')
                
        except Exception as e:
            raise LoanStatException(e, sys) from e
            
            
    def perform_normality_test(self, data_array : np.array):
        """
        Function to perform normality test on data
        """
        try:
            # normality test
            stat, p = shapiro(data_array)
            print('Statistics=%.3f, p=%.3f' % (stat, p))
            # interpret results
            alpha = 0.05
            if p > alpha:
                print('Sample looks Gaussian (fail to reject H0)')
            else:
                print('Sample does not look Gaussian (reject H0)')

        except Exception as e:
                raise LoanStatException(e, sys) from e
