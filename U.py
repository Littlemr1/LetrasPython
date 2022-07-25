#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#   *** 

for i in range(7):
    for j in range(7):
        if 1 <= i <= 5 and (j == 1 or j == 5):
            print('*', end='')
        elif i == 6 and (2 <= j <= 4):
            print('*', end='')
        else:
            print(' ', end='')
    print()
