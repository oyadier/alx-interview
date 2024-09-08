#!/usr/bin/python3
def isWinner(x: int, nums: list) -> str:
    '''
    The prime game between Mariam And Ben
    x (Integer):
        the number of rounds
    nums (List):
    List of numbers to pick from
    Return:
        Name of the winner
    '''
    nums = [2, 5, 1, 4, 3, 7]
    isBen = True
    winner = []

    for value in range(x + 1):
        print(f"{value} is accessed")
        if value > 1:
            for i in range(2, int(value**0.5) + 1):
                if value % i == 0:
                    break 
            else:
                print('Prime number {}'.format(value))
                news = value
                count = 0
                while count <= len(nums):
                    for i in nums:
                        if i % news == 0:
                            nums.remove(i)
                        count += 1
                
                if isBen:
                    isBen = False
                    winner.append(True)
                    
                else:
                    isBen = True
                    winner.append(False)
            print(winner)
            print(nums)
    if len(nums) % 2 == 0:
        return 'Ben'
    else:
        return 'Maria'
