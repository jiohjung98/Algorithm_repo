function solution(n, lost, reserve) {
    // 여벌 체육복이 있으나 도난당한 학생 제외
    let setReserve = reserve.filter(r => !lost.includes(r));
    let setLost = lost.filter(l => !reserve.includes(l));

    // 여벌 체육복을 빌려줌
    setReserve.forEach(r => {
        if (setLost.includes(r - 1)) {
            setLost = setLost.filter(l => l !== r - 1); // 체육복을 빌렸으므로 제거
        } else if (setLost.includes(r + 1)) {
            setLost = setLost.filter(l => l !== r + 1);
        }
    });

    // 체육복을 못 빌린 학생 수 제외
    return n - setLost.length;
}