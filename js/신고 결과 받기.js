function solution(id_list, report, k) {

    const reportDict = new Map();
    const reportCount = new Map();

    
    
    id_list.forEach((user) => {
        reportDict.set(user, new Set());
        reportCount.set(user ,0);
    });
    
    report.forEach((elem) => {
        const [reporter, reported] = elem.split(' ');
        if (!reportDict.get(reporter).has(reported)) {
            reportDict.get(reporter).add(reported);
            reportCount.set(reported, reportCount.get(reported) + 1);
        }
    })
    
    const bannedUsers = new Set(
        Array.from(reportCount.entries())
            .filter(([user, count]) => count >= k)
            .map(([user]) => user)
    );
    
    return id_list.map((user) => {
        return Array.from(reportDict.get(user)).filter((reported) => {
            return bannedUsers.has(reported)
        }).length;
    });
}