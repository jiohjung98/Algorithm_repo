function solution(num_list) {
    // if (num_list.length >= 11) {
    //     return [...num_list].reduce((sum, acc) => {
    //         return sum + acc;
    //     }, 0);
    // } else {
    //     return [...num_list].reduce((sum, acc) => {
    //         return sum * acc;
    //     }, 1);
    // }
    
    return [...num_list].reduce((ans, acc) => num_list.length > 10 ? ans + acc : ans * acc);
}