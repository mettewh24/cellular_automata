# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 21:29:22 2024

@author: mettewh24
"""

rule30 = {"000": '.',
          "00.": '.',
          "0.0": '.',
          "...": '.',
          "0..": '0',
          ".00": '0',
          ".0.": '0',
          "..0": '0',
         }


def generate_state():
    return "....0...."



def evolve(state):
    new_state=""
    for i in range(len(state)):
        if i+1>len(state)-1:
            triplet=state[i-1]+state[i]+state[0]    
        else:
            triplet=state[i-1]+state[i]+state[i+1]
        new_state=rule30[triplet]+new_state
    
    return new_state
    

def simulation(nsteps):

    initial_state = generate_state()
    states_seq = [initial_state]
    for i in range(nsteps):
        old_state = states_seq[-1]
        new_state = evolve(old_state)
        states_seq.append(new_state)
    return states_seq

n=input('Insert number of steps \n')
n=int(n)
print(simulation(n))