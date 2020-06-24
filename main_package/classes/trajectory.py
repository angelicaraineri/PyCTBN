import pandas as pd
import numpy as np


class Trajectory():
    """ 
    Rappresenta una traiettoria come un numpy_array contenente n-ple (indx, T_k,S_i,.....,Sj)
    Offre i metodi utili alla computazione sulla struttura stessa.
    :actual_trajectory: il numpy_array contenente la successione di n-ple (indx, T_k,S_i,.....,Sj)

    """

    def __init__(self, list_of_columns):
        self.actual_trajectory = np.array(list_of_columns, dtype=object).T
        
    def get_trajectory(self):
        return self.actual_trajectory

    def merge_columns(self, list_of_cols):
        return np.vstack(list_of_cols).T

    """def get_states(self):
        
        Identifica gli stati visitati nella traiettoria.
        Parameters:
            void
        Returns:
            una lista contenente gli stati visitati nella traiettoria
        
        return self.actual_trajectory['State'].unique()"""
