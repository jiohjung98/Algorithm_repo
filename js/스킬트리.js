function solution(skill, skill_trees) {
    var answer = 0;
    
    skill_trees.forEach(x => {
        const arr = x.split('');
        const filteredArray = [];
        
        for (elem of arr) {
            if (skill.includes(elem)) {
                filteredArray.push(elem);
            }
        }
        
        if (skill.startsWith(filteredArray.join(''))) {
            answer += 1;
        }

    })
    return answer;
}