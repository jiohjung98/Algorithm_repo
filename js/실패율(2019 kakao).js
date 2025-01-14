function solution(N, stages) {
    var stage_count = Array.from({length: N+2}, () => 0);
    
    for (let i=0; i<stages.length; i++) {
        stage_count[stages[i]] += 1;
    }
    
    var total_people = stages.length;
    var fail_rates = [];
    for (let i=1; i<N+1; i++) {
        if (total_people > 0) {
            var fail = stage_count[i];
            var fail_rate = fail / total_people;
            total_people -= fail;
        } else {
            fail_rate = 0;
        }
        fail_rates.push([i, fail_rate]);
    }
    
    fail_rates.sort((a,b) => {
        if (a[0] === b[0]) {
            return a[0] - b[0];
        }
        return b[1] - a[1];
    })
    
    var answer = [];
    for (let i=0; i<fail_rates.length; i++) {
        answer.push(fail_rates[i][0]);
    }
    
    return answer;
}