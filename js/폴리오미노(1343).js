// board = input()

// board = board.replace('XXXX', 'AAAA')
// board = board.replace('XX', 'BB')

// if 'X' in board:
//     print(-1)
// else:
//     print(board)

const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

let board = input[0];

let board_a = board.replace(/XXXX/g, 'AAAA');
let board_b = board_a.replace(/XX/g, 'BB');

if (board_b.includes('X')) {
    console.log(-1);
} else {
    console.log(board_b);
}