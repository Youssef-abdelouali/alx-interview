#!/usr/bin/python3
'''Coding challenge.
'''


def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n H characters.
    '''
    if not isinstance(n, int):
        return 0
    ops_co = 0
    clipbo = 0
    done = 1
    # print('H', end='')
    while done < n:
        if clipbo == 0:
            # init (the first copy all and paste)
            clipbo = done
            done += clipbo
            ops_co += 2
            # print('-(11)->{}'.format('H' * done), end='')
        elif n - done > 0 and (n - done) % done == 0:
            # copy all and paste
            clipbo = done
            done += clipbo
            ops_co += 2
            # print('-(11)->{}'.format('H' * done), end='')
        elif clipbo> 0:
            # paste
            done += clipbo
            ops_co += 1
            # print('-(01)->{}'.format('H' * done), end='')
    # print('')
    return ops_co
