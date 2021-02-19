# -*- coding: utf-8 -*-
"""
Randomly choose a quote from several csv files.

Created on Tue Feb 16 12:32:43 2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


import pandas as pd
import random


class Quotes:
    """Randomly choose a quote from several csv files from GitHub."""
    
    def __init__(self):
        """
        Initilize the values with the links to the GitHub directory with the
        csv files.
        
        url_de : str ; link to the quotes in German
        url_es : str ; link to the quotes in Spanish
        url_en : str ; link to the quotes in English
        """
        
        self.url_de = 'https://raw.githubusercontent.com/PedroBiel/quotes/main/csv/zitate.csv'
        self.url_es = 'https://raw.githubusercontent.com/PedroBiel/quotes/main/csv/citas.csv'
        self.url_en = 'https://raw.githubusercontent.com/PedroBiel/quotes/main/csv/quotes.csv'

    def choose_quote(self):
        """
        Choose a quote from the csv files with quotes

        Returns
        -------
        quote : str
        """
        
        # Read quotes.
        data_de = pd.read_table(self.url_de, names=['Quotes'])  # Zitate.
        data_es = pd.read_table(self.url_es, names=['Quotes'])  # Citas.
        data_en = pd.read_table(self.url_en, names=['Quotes'])  # Quotes.
        
        # Concatenate DataFrames.
        data = pd.concat([data_de, data_es, data_en])
        
        # To list.
        l = data['Quotes'].to_list()
        
        # Randomly choose.
        quote = random.choice(l)
        
        return quote


if __name__ == '__main__':
    
    quotes = Quotes()
    print(quotes.choose_quote())