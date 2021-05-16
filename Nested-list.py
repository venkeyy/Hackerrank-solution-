 if __name__ == '__main__':

    score_lst = []

    marksheet = []  # marksheet=[[name,mark],[name,mark]....]

    for _ in range(int(input())):

        name = input()

        score = float(input())

        marksheet.append([name,score]) #list of name, score 
                       #We need to find second lowest score by using the set in storted method. 
                       #Set will delete duplicate entries in the list. 
        score_lst.append(score)

    second_lowest = sorted(list(set(score_lst)))[1] #To get the second largest element 

    names = [name for name,marks in sorted(marksheet) if marks == second_lowest]

    print('\n'.join(names)) #To pass list. 
