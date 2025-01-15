function solution(s, skip, index) {
    var answer = '';
    var alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];
    
    var filteredAplha = alphabets.filter(v => ![...skip].includes(v));
    
    for (let i=0; i<s.length; i++) {
        var newIdx = filteredAplha.indexOf(s[i]) + index;
        answer += filteredAplha[newIdx % filteredAplha.length];
    }
    return answer;
}