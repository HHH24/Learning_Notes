#! -*- coding: utf-8 -*-
import os, sys, shutil
import zlib, json, io
import logging

COMPRESS_LEVEL = 6


class Notebook:
    """A notebook by a dict
    - {'file1': 'value1', 'file2': 'value2', 'list1': ['file1.1', 'file2.2']}"""
    
    def __init__(self, note_dict: dict):
        self.note_dict = note_dict
        
    @staticmethod
    def compress(to_comp: dict):
        """Returns compressed bytes
        Compresses: dict -> str -> encodedstr -> compedbytes"""
        tc_str = str(to_comp)
        tc_bytes = tc_str.encode()
        comped = zlib.compress(tc_bytes)
        
        # Returns the comped
        return comped

    @staticmethod
    def decompress(to_decomp: bytes):
        """Returns a dict
        Decompresses: tocompbytes -> str -> dict"""
        dc_bytes = zlib.decompress(to_decomp)
        dc_str = dc_bytes.decode()
        decomped = eval(dc_str)
        
        # Returns the comped and its chunk_size
        return decomped


if __name__ == '__main__':
    td = {'file1': 'value1', 'file2': 'value2', 'list1': ['file1.1', 'file2.2']}
    test_notebook1 = Notebook(td)
    
    a = Notebook.compress(test_notebook1.note_dict)
    a1 = Notebook.decompress(a)
    
    assert a1 == test_notebook1.note_dict, \
    'a1 does not equal to the original dict'
    
    