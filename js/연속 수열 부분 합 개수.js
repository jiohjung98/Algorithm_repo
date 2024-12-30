function solution(elements) {
    var lengths = elements.length;
    var set = new Set();
    
    for (i=0; i < lengths; i++) {
        var tmp = elements[i];
        set.add(tmp);
        
        for (j=i+1; j < i+lengths; j++) {
            tmp += elements[j%lengths];
            set.add(tmp);
        }
    }
    return set.size;
}