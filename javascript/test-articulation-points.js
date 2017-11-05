const { execFileSync } = require('child_process');

function run(stdin) {
    stdin = stdin.trim() + '\n';
    try {
        let result = execFileSync(process.execPath, ['./articulation-points.js'], {
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

if(1)run('0 1\n1 2\n2 0\n3 2\n4 3\n4 2\n5 4\n');
