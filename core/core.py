#! -*- coding: utf-8 -*-
import os, sys, shutil
import zlib, json, io
import logging

class Notebook:
    """A notebook by a dict
    - {'file1': 'value1', 'file2': 'value2', 'list1': ['file1.1', 'file2.2']}"""
    
    def __init__(self, note_dict: dict):
        self.note_dict = note_dict
        
    @staticmethod
    def compress(to_comp: dict, chunk_size = 100000):
        """Compresses: dict -> str -> encodedstr -> compedbytes"""
        compressor = zlib.compressobj()
        str_comp = str(to_comp)
        encoded_comp = str_comp.encode()
        
        # Debug
        logging.info(type(encoded_comp))
        
        # Compress through iteration
        comped = b''
        if len(encoded_comp) <= chunk_size:
            comped += compressor.compress(encoded_comp)
            
        else:
            i = 0
            for chunk in encoded_comp[i : i + chunk_size]:
                comped += compressor.compress(chunk)
                i += chunk_size
                
                if len(encoded_comp) < i + chunk_size:
                    # No enough bytes to index
                    # Always goes here in the end
                    comped += compressor.compress(encoded_comp[i:])
                    break
                    
        # Return
        return comped
        

if __name__ == '__main__':
    test_notebook1 = Notebook(
        {'file1': 'value1', 'file2': 'value2', 'list1': ['file1.1', 'file2.2']}
    )
    print(Notebook.compress(test_notebook1.note_dict))
    print(Notebook.compress(test_notebook1.note_dict, 2))