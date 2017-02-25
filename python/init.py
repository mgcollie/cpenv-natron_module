import os
import sys
import NatronEngine

from pprint import pprint as pp

paths = {'output':{
    'win':'N:/proddev/dev/mcollie/NATRON/output.####.jpg',
    'linux':'/home/mcollie/output/output.####.jpg'},
    'source':{
    'win':'N:/render-layers/thomas/tf21/seq_00080/shot_0020/default/set_all/left/set_all_PRIMARY/set_all_PRIMARY.0001.exr',
    'linux':'/home/mcollie/source/set_all_PRIMARY.0001.exr'},
    }

READ_WRITES = ['fr.inria.built-in.Read', 'fr.inria.openfx.ReadOIIO', 'fr.inria.built-in.Write']

def swap(node):
    node_id = node.getPluginID()
    
    if node_id in READ_WRITES:
        cur_param = node.getParam('filename')
        cur_val = cur_param.getValue()

        key = 'source'
        
        if node_id.endswith('Write'):
            key = 'output'

        new_val = cur_val.replace(paths[key]['win'], paths[key]['linux'])
        cur_param.setValue(new_val)



def dirmap(app):
    print('\n\n\n executing callback\n\n\n')

    children = app.getChildren()

    for node in children:
        swap(node)


NatronEngine.natron.setOnProjectLoadedCallback("dirmap")

