function solution(myString, pat) {
    return [...myString].map((v) => v = v == "A" ? "B" : "A").join("").indexOf(pat) > -1 ? 1 : 0;
}