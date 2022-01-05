# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 08:34:30 2022

@author: Wolf
"""

class Block:
    """
    Block: a unit of storage.
    Store transactions in theblockchian that supports a cryptocurrency.
    """
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f'Block - data: {self.data}'

def main():

    block = Block('foo')
    print(block)

    print(f'block.py __name__: ')

if __name__ == '__main__':
    main()