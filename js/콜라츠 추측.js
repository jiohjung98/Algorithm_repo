function solution(num) {
    let value = num;
    let cnt = 0;
    while (value > 1 && cnt < 500) {
        if (value % 2 == 0) {
            value /= 2;
        } else {
            value = value * 3 + 1;
        }
        cnt++;
    }
    if (cnt == 500) {
        return -1;
    } else {
        return cnt;
    }
}