// 정규표현식 사용
// function solution(babbling) {
//     const regexp1 = /(aya|ye|woo|ma)\1+/;
//     const regexp2 = /^(aya|ye|woo|ma)+$/;
  
//     return babbling.reduce((ans, word) => (
//       !regexp1.test(word) && regexp2.test(word) ? ++ans : ans
//     ), 0);
//   }


function solution(babbling) {
    const can_speak = ["aya", "ye", "woo", "ma"];
    
    return babbling.reduce((possible, babbl, index) => {
        for (let i=0; i<can_speak.length; i++) {
            if (babbl.includes(can_speak[i].repeat(2))) return possible;
        }
        
        for (let j=0; j<can_speak.length; j++) {
            babbl = babbl.split(can_speak[j]).join(' ').trim();
        }
        
        if (babbl) return possible;
        
        return possible += 1;
    }, 0)
}