import pandas as pd
from exceptions import LoanStatException
from category_encoders import TargetEncoder
import  numpy as np
import os,sys

class DataPreprocess:

    """
    This class help to preprocess the data
    
    """
    def columns_by_missing_percent(self, df : pd.DataFrame, threshold : float):
        """
        Function to find missing data above the threshold
        """
        
        try:
            missing_prct=df.isnull().sum()/len(df)*100
            all_columns = df.columns
            null_variables = [ ]
            
            for col in df.columns:
                if missing_prct[col] >= threshold:  
                    null_variables.append(col)
            
            return null_variables

        except Exception as e:
                raise LoanStatException(e, sys) from e
                
                
    def remove_static_columns(self, df : pd.DataFrame):
        """
        Function to remove static columns
        """

        try:
            for col in df.columns:
                if df[col].nunique() == 1:
                    df.drop(col, axis=1, inplace=True)
            
            
            return df

        except Exception as e:
                raise LoanStatException(e, sys) from e
                
                
    def get_non_numeric_columns(self, df : pd.DataFrame):
        """
        Function to get object columns
        """

        try:
            obj_columns = df.loc[:, df.dtypes == object].columns
            
            return obj_columns

        except Exception as e:
                raise LoanStatException(e, sys) from e
                
                
    def ordinal_encoding(self, df : pd.DataFrame):

        """
        Function to encode categorical variables with orders
        """
        
        try:
            term_encode = {' 36 months': 1,
                           ' 60 months': 2}
            grade_encode = dict(zip(['A', 'B', 'C', 'D', 'E', 'F', 'G'], np.arange(7, 0, -1)))
            
            #copied from above, we can write a function to generate this dict
            sub_grade_sorted = {'G5': 0, 'G4': 1, 'G3': 2, 'G2': 3, 'G1': 4,
                                'F5': 5, 'F4': 6, 'F3': 7, 'F2': 8, 'F1': 9,
                                'E5': 10, 'E4': 11, 'E3': 12, 'E2': 13, 'E1': 14,
                                'D5': 15, 'D4': 16, 'D3': 17, 'D2': 18, 'D1': 19,
                                'C5': 20, 'C4': 21, 'C3': 22, 'C2': 23, 'C1': 24,
                                'B5': 25, 'B4': 26, 'B3': 27, 'B2': 28, 'B1': 29,
                                'A5': 30, 'A4': 31, 'A3': 32, 'A2': 33, 'A1': 34}  
            
            home_encode = {'OWN': 5, 'MORTGAGE': 4, 'RENT': 3, 'ANY': 2,'OTHER': 1, 'NONE':0 }
            
            ver_stat_encode = {'Source Verified':2,'Verified': 1,'Not Verified': 0} 
            
            emp_length_encode = {'10+ years' : 10, '< 1 year' :0 , '1 year' : 1, '3 years' : 3 , '8 years' : 8, '9 years' : 9,
                   '4 years' : 4, '5 years' : 5, '6 years' : 6, '2 years' : 2 , '7 years': 7}
            
            loan_status_encoded =  {'Fully Paid' : 0, 'Charged Off' : 1,} 
            
            debt_settlement_flag_encoded =  {'N' : 0, 'Y' : 1}
            
            df.replace({'term': term_encode, 
                            'grade':grade_encode,
                            'sub_grade': sub_grade_sorted,
                            'home_ownership':home_encode,
                            'verification_status':ver_stat_encode,
                           'emp_length' : emp_length_encode,
                           'loan_status' : loan_status_encoded,
                           'debt_settlement_flag' : debt_settlement_flag_encoded}, inplace=True)

            return df
            
        except Exception as e:
            raise LoanStatException(e, sys) from e
        
        
    def target_encoding(self, df : pd.DataFrame, cat_columns : list):
    
        """
        Function to encode categorical variables with Target Mean
        """
        try:
            encoder = TargetEncoder()   
            enc_cols = []
            for col in cat_columns:
                enc_cols.append(col + '_enc')
                
            df[enc_cols] = encoder.fit_transform(df[cat_columns], df['loan_status'])

            df.drop(cat_columns, axis=1, inplace = True)

            return df
            
        except Exception as e:
            raise LoanStatException(e, sys) from e
        
        
    def drop_columns(self, df : pd.DataFrame, columns_to_drop : list):
        try:
            df = df.drop(columns_to_drop, axis = 1)
            return df
            
        except Exception as e:
            raise LoanStatException(e, sys) from e