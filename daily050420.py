'''
Daily problem about skipping stairs
'''

def recursive_stairs(step_sizes,num_steps,cache):
    if num_steps in cache:
        return cache[num_steps]
    elif num_steps<0:
        return 0
    else:
        combinations = 0
        for s in step_sizes:
            combinations += recursive_stairs(step_sizes,num_steps-s,cache)
        return combinations

def stairs(step_sizes,num_steps):
    cache = {0: 1}
    return recursive_stairs(step_sizes,num_steps,cache)    