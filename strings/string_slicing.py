def join_middle(bound_by, tag_name):
    n = int(len(bound_by)/2)
    return bound_by[:n] + tag_name + bound_by[n:]
print(join_middle('[[]]', 'tag')) 
