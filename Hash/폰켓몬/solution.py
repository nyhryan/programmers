def solution(nums):
    # { 폰켓몬: 마릿수 } 맵 생성
    d = {}
    for n in nums:
        d[n] = d.get(n, 0) + 1

    # 폰켓몬의 종류 수
    total_pokemons = len(d)

    # 가져갈 수 있는 마릿수
    n = len(nums) // 2

    # 가져갈 수 있는 마릿수가 주어진 종류 수보다 많으면 
    # 최대는 주어진 종류 수이다.
    # 아니라면(종류 수가 더 많다면) 서로 다른 n 마리 가져가면 된다.
    return total_pokemons if n > total_pokemons else n