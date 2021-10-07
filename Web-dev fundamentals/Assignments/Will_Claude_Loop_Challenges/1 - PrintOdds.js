// 1. Print odds 1-20
function printOdds() {
    for(let i = 1; i <= 20; i++) {
        if(i % 2 === 0) {
            continue;
        }
        else 
        {
            console.log(i);
        }
    }
}

printOdds();