
# 1) Row traverse forward and backward
# 2) coloum traverse upward and downward
# 3) all diagonal traverse

# 4) find any obstacles in a row
# 5) find any obstacles in a coloumn
# 6) find any obstacles in all diagonals

def queensAttack(n, r_q, c_q, obstacles):


    def Traverser(r_q, c_q):


        # 1) ROW TRAVERSE FORWARD AND BACKWARD

        row_steps = 0
        row_forward = r_q

        while((0 <= row_forward  < n) and (row_forward != obstacles[0])):
            row_forward += 1
            row_steps += 1

        row_backward = r_q
        while((0 <= row_backward  < n) and (row_backward != obstacles[0])):
            row_backward-= 1
            row_steps += 1

        # 2) coloum traverse upward and downward

        coloum_steps = 0
        while((0 <= r_q  < n and 0 <= c_q  < n) or c_q == obstacles[1]):
            c_q += 1
            coloum_steps += 1

        while((0 <= r_q  < n and 0<= c_q  < n) or c_q == obstacles[1]):
            c_q -= 1
            coloum_steps += 1
        
        # 3.1) Right diagonal traverse 

        right_diagonal_steps = 0
        while((0 <= r_q  < n and 0 <= c_q  < n) or (r_q == obstacles[0] and c_q == obstacles[1])):
            r_q += 1
            c_q += 1
            right_diagonal_steps += 1

        while((0 <= r_q  < n and 0 <= c_q  < n) or (r_q == obstacles[0] and c_q == obstacles[1])):
            r_q -= 1
            c_q -= 1
            right_diagonal_steps += 1
            
        # 3.2) Left diagonal traverse

        left_diagonal_steps = 0
        while((0 <= r_q  < n and 0 <= c_q  < n) or (r_q == obstacles[0] and c_q == obstacles[1])):
            r_q += 1
            c_q -= 1
            left_diagonal_steps += 1

        while((0 <= r_q  < n and 0 <= c_q  < n) or (r_q == obstacles[0] and c_q == obstacles[1])):
            r_q -= 1
            c_q += 1
            left_diagonal_steps += 1

    
    # 4) find any obstacles in a row
    def obstacles_in_row():

        obstacles_in_row = []
        for x in range(len(obstacles)):

            if(c_q == obstacles[x][1]):
                obstacles_in_row.append([obstacles[x][0],obstacles[x][1]]) 
        
        print(obstacles_in_row)
    
    
    # 5) find any obstacles in a coloumn
    def obstacles_in_coloumn():

        obstacles_in_coloumn = []
        for x in range(len(obstacles)):

            if(r_q == obstacles[x][0]):
                obstacles_in_coloumn.append([obstacles[x][0],obstacles[x][1]]) 
        
        print(obstacles_in_coloumn)

    
    # 6) finding obstacles in diagonal by subtracting correspoding points
    def obstacles_in_diagonal():

        obstacles_in_diagonal = []
        for x in range(len(obstacles)):

            if(abs(r_q - obstacles[x][0]) == abs(c_q - obstacles[x][1])):
                obstacles_in_diagonal.append([obstacles[x][0],obstacles[x][1]])
        
        print(obstacles_in_diagonal)
    
    obstacles_in_diagonal()




# def queensAttack(n, r_q, c_q, obstacles):
queensAttack(5, 4, 3,[[5, 5],[4, 2],[2, 3],[5,4],[3,2]])