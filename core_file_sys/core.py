#! -*- coding: utf-8 -*-
import os, sys, shutil
import zlib

def file_to_text(filedict: dict):
    """File or dir into text
       -
       ({file='text1', file2='text2',
        dir={'file1': 'text1', 'file2': 'text2'}})
    """
    
    # Returns
    return_list = []
    return_text = b''
    
    # Compressobj and decompressobj
    compobj = zlib.compressobj()
    decompobj = zlib.decompressobj()
    
    for filename, info in filedict.items():
        # choose the file
        if type(info) == str or type(info) == bytes:
            comp_bytes = bytes(
                (filename + ':' + str(info) + '__NEWLINE__').encode())
            comped_bytes = compobj.compress(comp_bytes)
            return_list += filename
            return_text += comped_bytes
            
        elif type(info) == dict:
            # Create a copy of info called new_info
            new_info = {}
            for key, value in info.items():
                new_info[key] = value

            # Change keys in new_info
            for filename1, info1 in info.items():
                new_info[filename + '.' + filename1] = info1
                del new_info[filename1]

            #print(file_to_text(new_info))
            dg_return = file_to_text(new_info)
            return_list += dg_return[0]
            return_text += dg_return[1]

    # Return
    return return_list, return_text
            
            
if __name__ == '__main__':
    test_dict = {'file': 'text1', 'file2': 'text23',
                       'dir': {'file1': 'text1', 'file2': 'text23'}}
    #del test_dict['dir']
    #print(test_dict)
    print(file_to_text(test_dict))
