from exceptions import LoanStatException
from utils import utils
import pandas as pd
import os,sys

class DataImport:


    
    """
    This class help to read data from csv and provide dataframe
    
    """

    def __init__(self):
        """
        """
        try:
            util = utils()
            self.file_path = utils.read_yaml_file("config.yml")["DATA_FILE_PATH"]
            print(self.file_path)
        except Exception as e:
            raise LoanStatException(e, sys)

    def load_data(self):

        try:
            df = pd.read_csv(self.file_path, skiprows=1, low_memory=False)
            df = df[df.loan_status.isin(["Fully Paid", "Charged Off"])]
        except Exception as e:
            raise LoanStatException(e, sys)
            
        return df