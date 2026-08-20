import java.util.*;

class Solution {
    // 1. 스택 기반 DFS
    public int solution(int[] numbers, int target) {
        int answer = 0;
        Deque<int[]> stack = new ArrayDeque<>();
        // [방문할 인덱스, 방문시 누적합]
        stack.push(new int[]{0, numbers[0]});
        stack.push(new int[]{0, -numbers[0]});

        while (!stack.isEmpty()) {
            int[] popped = stack.pop();
            int idx = popped[0], acc = popped[1];
            int n = numbers[idx];

            if (idx < numbers.length - 1) {
                int nIdx = idx + 1;
                int nextNum = numbers[nIdx];

                if (nIdx == numbers.length - 1 && (acc + nextNum == target || acc - nextNum == target)) {
                    answer++;
                }
                else {
                    stack.push(new int[]{nIdx, acc + nextNum});
                    stack.push(new int[]{nIdx, acc - nextNum});
                }
            }
        }
        return answer;
    }

    // 2. 재귀 기반 DFS
    int recursive_solution(int[] numbers, int target) {
        return dfs(numbers, target, 0, 0);
    }
    int dfs(int[] numbers, int target, int idx, int acc) {
        if (idx == numbers.length) {
            return acc == target ? 1 : 0;
        }

        return dfs(numbers, target, idx + 1, acc + numbers[idx]) +
                dfs(numbers, target, idx + 1, acc - numbers[idx]);
    }

    // 3. DP
    int dp_solution(int[] numbers, int target) {
        // dp(i, sum) = dp(i-1, sum - numbers[i]) + dp(i-1, sum + numbers[i])
        //            = i번째 숫자까지 써서 총합이 target이 되는 경우의 수
        // dp = { sum: count }
        Map<Integer, Integer> dp = new HashMap<>();
        dp.put(0, 1); // 초기 상태: 0개의 숫자로 합 0을 만드는 경우 1가지

        for (int num : numbers) {
            Map<Integer, Integer> nextDp = new HashMap<>();
            
            // 최대 [- numbers.sum() ~ + numbers.sum()] 반복
            for (int sum : dp.keySet()) {
                // 현재 합계값을 만들 수 있는 모든 조합의 수
                int count = dp.get(sum);

                // sum+num 값을 만들 수 있는 조합의 수++
                nextDp.put(sum + num, nextDp.getOrDefault(sum + num, 0) + count);
                // sum-num 값을 만들 수 있는 조합의 수++
                nextDp.put(sum - num, nextDp.getOrDefault(sum - num, 0) + count);
            }
            dp = nextDp;
        }

        return dp.getOrDefault(target, 0);
    }
}