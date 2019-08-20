# -*- coding: utf-8 -*-
inf = float('inf')
def maximize(state,alpha,beta):

    if terminal_test(state):
        print(state,end=' ')
        return None,evaluation(state)

    bestChild, v = None, -inf
    for child in nextstates(state):
        _,utility = minimize(child,alpha,beta)
        if utility > v:
            v, bestChild = utility, child
        if v >= beta:
            print('#',end=' ')
            break
        if v > alpha:
            alpha = v
    return bestChild, v

def minimize(state,alpha,beta):

    if terminal_test(state):
        print(state,end=' ')
        return None,evaluation(state)

    v, bestChild = inf, None
    for child in nextstates(state):
        _,utility = maximize(child,alpha,beta)
        if utility < v:
            v, bestChild = utility, child
        if v <= alpha:
            print('#',end=' ')
            break
        if v < beta:
            beta = v
    return bestChild, v

def decision(state):
    child, _ = maximize(state,-inf,inf)
    return child

def nextstates(state):
    return nxt[state]

def terminal_test(state):
    return state in blatt

def evaluation(state):
    return blatt[state]

nxt = {'a':list('bc'),'b':list('de'),'c':list('fg')}   # wurzel 'a'
blatt = {'d':10,'e':8,'f':4,'g':50}
best = decision('a')
print('\nBester Zug',best)
#%%
#%% Baum4