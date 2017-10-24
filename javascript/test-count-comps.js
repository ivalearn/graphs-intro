const { execFileSync } = require('child_process');

function run(stdin) {
    stdin = stdin.trim() + '\n';
    try {
        let result = execFileSync(process.execPath, ['./count-comps.js'], {
            cwd: process.cwd(),
            input: stdin,
            stdio: 'pipe'
        });
        stdout = String(result);
        retval = 0;
    } catch (ex) {
        stdout = ex.output.join('\n');
        retval = 1;
    }
    console.log(
        ' stdout=' + JSON.stringify(stdout.trim()) +
        ' stdin=' + JSON.stringify(stdin) +
        ' retval=' + retval
    );
    return [retval, stdout];
}

if(1)run(`
4 2
1 2
3 2
`);

if(1)run(`
4 3
1 2
3 2
4 3
`);

if(1)run(`
6 10
1 1
2 2
3 3
4 4
5 1
1 5
3 2
4 3
2 1
6 6
`);
