
def solution(rows, cols, goal_row, goal_col, queries):
        top_left_row, top_left_col, btm_right_row, btm_right_col = goal_row, goal_col, goal_row, goal_col

        for i in range(len(queries) - 1, -1, -1):
            dir = queries[i][0]
            delta = queries[i][1]
            
            match (dir):
                # // 오른쪽
                case 0:
                    btm_right_col = min(btm_right_col+delta,cols-1)
                    if(top_left_col > 0):
                        top_left_col += delta
                    if(top_left_col > cols-1):
                        return 0 # 범위 밖으로 나가는지 체크

                # 왼쪽
                case 1:
                    if(btm_right_col < cols-1):
                        btm_right_col -= delta
                    top_left_col = max(top_left_col-delta,0)
                    if(btm_right_col < 0):
                        return 0

                # 아래
                case 2:
                    if(top_left_row > 0):
                        top_left_row += delta
                    btm_right_row = min(btm_right_row+delta,rows-1)
                    if(top_left_row > rows-1):
                        return 0

                # 위
                case 3:
                    if(btm_right_row < rows-1):
                        btm_right_row -= delta
                    top_left_row = max(top_left_row-delta,0)
                    if(btm_right_row < 0):
                        return 0


        return (btm_right_row-top_left_row+1)*(btm_right_col-top_left_col+1) # 최종 계산


# solution(2,2,0,0,[[2,1],[0,1],[1,1],[0,1],[2,1]])
solution(2,5,0,1,[[3,1],[2,2],[1,1],[2,3],[0,1],[2,1]])
# solution(1,3,0,1,[[1, 10]])
# solution(2,2,0,0,[
#     [1, 100],
#     [3, 100],
#     [0, 100],
#     [2, 100],
# ])
