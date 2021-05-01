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
        """Compresses: dict -> str -> encodedstr -> compedbytes"""
        compressor = zlib.compressobj(COMPRESS_LEVEL)
        chunk_size = 100000
        
        str_comp = str(to_comp)
        encoded_comp = str_comp.encode('utf-8')
        # Create an io with encoded_comp
        # And use .read() to iterate
        encoded_io = io.BytesIO(encoded_comp)
        comped = b''
        for chunk in encoded_io.read(chunk_size):
            chunk = bytes(chunk)
            if not chunk:
                break
            c = compressor.compress(chunk)
            if c:
                comped += c
        comped += compressor.flush()
        
        # Returns the comped
        return comped

    @staticmethod
    def decompress(to_decomp: bytes):
        """Decompresses: tocompbytes -> str -> dict"""
        decompressor = zlib.decompressobj()
        chunk_size = 100000
    
        decomped_b = b''
        decomp_io = io.BytesIO(to_decomp)
        for chunk in decomp_io.read(chunk_size):
            chunk = bytes(chunk)
            if not chunk:
                break
            d = decompressor.decompress(chunk)
            if d:
                decomped_b += d
        decomped_b += compressor.flush()
        decomped_str = decomped_b.decode('utf-8')
        
        decomped_dict = eval(decomped_str)
        
        # Returns the comped and its chunk_size
        return decomped_dict


if __name__ == '__main__':
    td = {'file1': 'value1', 'file2': 'value2', 'list1': ['file1.1', 'file2.2']}
    test_notebook1 = Notebook(td)
    
    a = Notebook.compress(test_notebook1.note_dict)
    aa = zlib.compress(str(test_notebook1.note_dict).encode('utf-8'))
    print(a)
    print(aa)
    b = zlib.decompress(a)
    bb = zlib.decompress(aa)
    print(b)
    print(bb)
    c = b.decode('utf-8')
    cc = bb.decode('utf-8')
    print(c)
    print(cc)
    
    a1 = Notebook.decompress(a)
    assert a1 == td, 'a1 does not equals to td'
    
    