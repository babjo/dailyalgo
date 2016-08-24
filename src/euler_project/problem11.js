/*
var MATRIX_SIZE = 20;
var SLICE_SIZE = 4;

fs = require('fs')
fs.readFile('problem11_input.txt', 'utf8', function (err,data) {
    var numbers = parseIntArray(data, MATRIX_SIZE);

    var max = 0;
    var result;
    var func = [horizontal, vertical, rightDownDiagonal, rightUpDiagonal];
    for(var row=0; row<numbers.length; row++){
        for(var col=0; col<numbers[row].length; col++){
            for(var i=0; i<func.length; i++){
                result = func[i](numbers, row, col, SLICE_SIZE);
                if(result.success && max < result.mul) max = result.mul;
            }
        }
    }

    console.log(max);
});

function parseIntArray(data, size){
    var twoDimension = new Array(size);
    var i=0;
    var oneDimension;
    var lines = data.split('\n');
    for(var i=0; i<lines.length; i++){
        oneDimension = new Array(size);
        var strNums = lines[i].split(' ');
        for(var j=0; j<strNums.length; j++){
            oneDimension[j] = parseInt(strNums[j]);
        }
        twoDimension[i] = oneDimension;
    }
    return twoDimension;
}

function horizontal(numbers, row, beginCol, length){
    var mul=1;
    var slice = new Array(length);
    var j=0;
    for(var i=beginCol; i<numbers[row].length && i<beginCol+length; i++){
        slice[j++] = numbers[row][i];
        mul *= numbers[row][i];
    }

    return { slice : slice, mul : mul, success : i === beginCol+length };
}

function vertical(numbers, beginRow, col, length){
    var mul=1;
    var slice = new Array(length);
    var j=0;
    for(var i=beginRow; i<numbers.length && i<beginRow+length; i++){
        slice[j++] = numbers[i][col];
        mul *= numbers[i][col];
    }

    return { slice : slice, mul : mul, success : i === beginRow+length };
}

function rightDownDiagonal(numbers, beginRow, beginCol, length){
    var mul=1;
    var slice = new Array(length);
    var j=0;

    var i=beginRow;
    var k=beginCol;
    while(i < numbers.length && k < numbers[i].length && i < beginRow+length && k < beginCol+length){
        slice[j++] = numbers[i][k];
        mul *= numbers[i][k];
        i++;
        k++;
    }

    return { slice : slice, mul : mul, success : i === beginRow+length && k === beginCol +length };
}

function rightUpDiagonal(numbers, beginRow, beginCol, length){
    var mul=1;
    var slice = new Array(length);
    var j=0;

    var i=beginRow;
    var k=beginCol;
    while(i >= 0 && k < numbers[i].length && i > beginRow-length && k < beginCol+length){
        slice[j++] = numbers[i][k];
        mul *= numbers[i][k];
        i--;
        k++;
    }

    return { slice : slice, mul : mul, success : i === beginRow-length && k === beginCol+length };
}*/

fs = require('fs')
fs.readFile('problem11_input.txt', 'utf8', function (err,data) {
    var numbers = parseIntArray(data, 20);

    var max = 0;
    var result;

    for(var row=0; row<20; row++){
        for(var col=0; col<20; col++){
            if(col<17){
                result = mul(numbers, row, col, 0, +1);
                if(max < result) max = result;
            }
            if(row<17){
                result = mul(numbers, row, col, +1, 0);
                if(max < result) max = result;
            }
            if(col<17 && row<17){
                result = mul(numbers, row, col, +1, +1);
                if(max < result) max = result;
            }

            if(col<17 && 3<row){
                result = mul(numbers, row, col, -1, +1);
                if(max < result) max = result;
            }
        }
    }

    console.log(max);
});

function mul(numbers, row, col, incRow, incCol){
    var mul=1;
    for(var i=0; i<4; i++)
        mul *= numbers[row+incRow*i][col+incCol*i];
    return mul;
}

function parseIntArray(data, size){
    var twoDimension = new Array(size);
    var i=0;
    var oneDimension;
    var lines = data.split('\n');
    for(var i=0; i<lines.length; i++){
        oneDimension = new Array(size);
        var strNums = lines[i].split(' ');
        for(var j=0; j<strNums.length; j++){
            oneDimension[j] = parseInt(strNums[j]);
        }
        twoDimension[i] = oneDimension;
    }
    return twoDimension;
}