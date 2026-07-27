def solution(rows, cols, goal_row, goal_col, queries):
    # 역추적을 위한 범위 초기화 (도착 지점 단 한 칸에서 시작)
    r_min, r_max = goal_row, goal_row
    c_min, c_max = goal_col, goal_col

    # 쿼리를 역순(뒤에서부터)으로 시뮬레이션
    for i in range(len(queries) - 1, -1, -1):
        direction, delta = queries[i][0], queries[i][1]

        match direction:
            # [Case 0] 정방향: 열 감소(좌) -> 역방향: 열 증가(우)
            case 0:
                if c_min > 0:                         # 왼쪽 끝이 경계에 붙어있지 않다면
                    c_min += delta                    # 왼쪽 끝도 함께 오른쪽으로 이동
                c_max = min(c_max + delta, cols - 1)  # 오른쪽 범위 확장/이동 (격자 경계 제한)
                if c_min >= cols:                     # 범위가 격자를 완전히 벗어난 경우
                    return 0

            # [Case 1] 정방향: 열 증가(우) -> 역방향: 열 감소(좌)
            case 1:
                if c_max < cols - 1:                  # 오른쪽 끝이 경계에 붙어있지 않다면
                    c_max -= delta                    # 오른쪽 끝도 함께 왼쪽으로 이동
                c_min = max(c_min - delta, 0)         # 왼쪽 범위 확장/이동 (경계 0 이하 방지)
                if c_max < 0:                         # 범위가 격자를 완전히 벗어난 경우
                    return 0

            # [Case 2] 정방향: 행 감소(상) -> 역방향: 행 증가(하)
            case 2:
                if r_min > 0:                         # 위쪽 끝이 경계에 붙어있지 않다면
                    r_min += delta                    # 위쪽 끝도 함께 아래로 이동
                r_max = min(r_max + delta, rows - 1)  # 아래쪽 범위 확장/이동 (격자 경계 제한)
                if r_min >= rows:                     # 범위가 격자를 완전히 벗어난 경우
                    return 0

            # [Case 3] 정방향: 행 증가(하) -> 역방향: 행 감소(상)
            case 3:
                if r_max < rows - 1:                  # 아래쪽 끝이 경계에 붙어있지 않다면
                    r_max -= delta                    # 아래쪽 끝도 함께 위로 이동
                r_min = max(r_min - delta, 0)         # 위쪽 범위 확장/이동 (경계 0 이하 방지)
                if r_max < 0:                         # 범위가 격자를 완전히 벗어난 경우
                    return 0

    # 최종 도착 가능한 시작점들의 사각형 영역 크기(칸 수) 계산
    return (r_max - r_min + 1) * (c_max - c_min + 1)

# 예제 실행
result = solution(2, 5, 0, 1, [[3, 1], [2, 2], [1, 1], [2, 3], [0, 1], [2, 1]])
print(result)  # 출력: 2