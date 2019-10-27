import re
def generate_list(input_):
    input_ = input_[1:-1]
    input_ = [word.replace(" ", ",") for word in list(input_)]
    print("["+"".join(input_)+"]")

# this is an example to figure out how the code works...
input_ = "(-3 +4 +1 +5 -2)"
obj = generate_list(input_)

sp = [-3,+4,+1,+5,-2]
def GreedySorting(sp,i):
    elements = sorted(([abs(x) for x in sp]))[1:]
    for ind in range(len(sp)-1):
        if i not in sp:
            i = -i
        for j in sp:
            if j!=i:
                continue
            else:
                index_ = sp.index(j)
                sp[ind:index_+1] = [-x for x in sp[ind:index_+1]][::-1]

        return_output(sp)
        if sp[ind] < 0:
            sp[ind] = -1*sp[ind]
            return_output(sp)
        i = elements[ind]

    print('(' + ' '.join('{:+}'.format(n) for n in sorted(([abs(x) for x in sp]))) + ')')
