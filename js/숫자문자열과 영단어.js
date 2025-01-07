function solution(s) {
    const num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"};
    var answer = s;
    for (value in num_dic) {
        // 주의: replace를 쓰면 중복된 단어가 나올 때 앞의 하나만 바뀌게 됨. 따라서 replaceAll 사용
        answer = answer.replaceAll(value, num_dic[value]);
    }
    return Number(answer);
}