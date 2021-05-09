#! -*- coding: utf-8 -*-
import os, sys, shutil
import zlib, json, io
import logging, string, warnings

FORMAT = 'format'
CONTENT = 'content'

class Notebook:
    """A notebook by a dict
    - {'file1': 'value1', 'file2': 'value2', 'list1': ['file1.1', 'file2.2']}"""

    # Initialization
    def __init__(self, note_dict: dict):
        self.note_dict = note_dict


    # Compression and decompression
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

    def compress_self(self):
        return Notebook.compress(self.note_dict)


    # Analisis
    # format example:(('name', str), ':', ('isman', bool))
    @staticmethod
    def analize(to_analize: dict, add_space = True):
        if FORMAT not in to_analize.keys():
            raise AnalisisError('no formats in dict:%s'
                                %(to_analize.__repr__()))
            return
        fm = to_analize[FORMAT]

        # TODO: Get a Formatting template
        template = ''
        first = True
        for char in fm:
            
            if add_space and not first:
                template += ' '
                
            if char[1] == True:
                # It's an input!
                template += '{%s}'%(char[0])
            else:
                # It's a constant!
                template += char[0]
                
            if first:
                first = False
            

        # Format the full dict into a list
        formatted = []
        for content in to_analize[CONTENT]:
            formatted.append(template.format(**content))

        # Return the formatted list
        return formatted

    def analize_self(self):
        return Notebook.analize(self.note_dict)


class AnalisisError(Exception):
    """Only trigers when analizing a notebook-dict"""
    pass


if __name__ == '__main__':
    """Test if exceptions"""
    td = {'file1': 'value1', 'file2': 'value2', 'list1': ['file1.1', 'file2.2']}
    test_notebook1 = Notebook(td)
    
    a = Notebook.compress(test_notebook1.note_dict)
    a1 = Notebook.decompress(a)

    
    