function solution(weights) {
    let answer = 0;
    let count = new Map();

    // 몸무게 개수 저장 (중복 고려)
    for (let weight of weights) {
        count.set(weight, (count.get(weight) || 0) + 1);
    }

    for (let [weight, cnt] of count) {
        // 같은 몸무게 조합 (nC2 = n * (n-1) / 2)
        answer += (cnt * (cnt - 1)) / 2;

        // 거리 비율에 따른 짝꿍 찾기
        for (let ratio of [2 / 3, 1 / 2, 3 / 4]) {
            let target = weight * ratio;
            if (count.has(target)) {
                answer += cnt * count.get(target);
            }
        }
    }

    return answer;
}