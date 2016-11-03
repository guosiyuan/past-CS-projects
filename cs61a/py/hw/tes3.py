def towers_of_hanoi(n, start, end):
    """Print the moves required to solve the towers of hanoi game, starting
    with n disks on the start pole and finishing on the end pole.

    The game is to assumed to have 3 poles.

    >>> towers_of_hanoi(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> towers_of_hanoi(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> towers_of_hanoi(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    def move_disk(start,end):
        print('Move the top disk from rod',start, 'to rod',end)
    assert 0 < start <= 3 and 0 < end <= 3 and start != end, "Bad start/end"
    if n==1:
        move_disk(start,end)
    else:
        towers_of_hanoi(n-1,start,6-start-end)
        move_disk(start,end)
        towers_of_hanoi(n-1,6-start-end,end)

    



