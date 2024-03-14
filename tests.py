# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 21:36:32 2024

@author: mette
"""

from cellular_automata import generate_state, evolve

def test_valid_state():
    state=generate_state()
    assert set(state)=={"0","."}
    
def test_generation_single_alive():
    state = generate_state()
    num_of_0 = sum(1 for i in state if i=='0')
    assert num_of_0 == 1
    
    
def test_state_lenght():
    new_state=evolve(generate_state())
    assert len(new_state)==len(generate_state())
    
    
def test_evolve_generate_state():
    new_state=evolve("..000..")
    assert new_state ==".00..0."
