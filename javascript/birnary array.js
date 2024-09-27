// function ArrayChallenge(strArr) {
//     const numbers = strArr.flatMap(item => {
//         return item.replace(/[()]/g, '').split(',').map(Number);
//     });
//     let map = new Map()

//     for (let num of numbers) {
//         if (!map.get(num)) {
//             map.set(num, 1)
//         }
//         else if (map.get(num) != 3) {
//             map.set(num, map.get(num) + 1)
//         }
//         else return false
//     }
//     // code goes here  
//     return true;

// }

// function ArrayChallenge(strArr) {
//     const varOcg = strArr.map(item => {
//         return item.replace(/[()]/g, '').split(',').map(Number);
//     });

//     let childToParent = new Map();
//     let parentToChildren = new Map();

//     for (let pair of varOcg) {
//         let [child, parent] = pair;

//         if (childToParent.has(child)) {
//             return false;  
//         }

//         childToParent.set(child, parent);

//         if (!parentToChildren.has(parent)) {
//             parentToChildren.set(parent, []);
//         }

//         parentToChildren.get(parent).push(child);

//         if (parentToChildren.get(parent).length > 2) {
//             return false;
//         }


//     }

//     let roots = new Set(parentToChildren.keys());

//     for (let child of childToParent.keys()) {
//         roots.delete(child);
//     }

//     return roots.size === 1 ? "true" : false;
// }

// console.log(ArrayChallenge(["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]
// ))

// function SearchingChallenge(strArr) {
//     const varOcg = strArr.map(row => row.split('').map(Number));
//     const rows = varOcg.length;
//     const cols = varOcg[0].length;

//     let holeCount = 0;

//     function markHole(r, c) {
//         if (r < 0 || r >= rows || c < 0 || c >= cols || varOcg[r][c] !== 0) {
//             return;
//         }
//         varOcg[r][c] = 1;

//         markHole(r + 1, c);
//         markHole(r - 1, c);
//         markHole(r, c + 1);
//         markHole(r, c - 1);
//     }

//     for (let r = 0; r < rows; r++) {
//         for (let c = 0; c < cols; c++) {
//             if (varOcg[r][c] === 0) {
//                 holeCount++;
//                 markHole(r, c);
//             }
//         }
//     }

//     return holeCount;
// }

// console.log(SearchingChallenge(["01111", "01101", "00011", "11110"]));
// console.log(SearchingChallenge(["1011", "0010"])); 



// function StringChallenge(str) { 


//     let map=new Map()

//     for(let char of str){
//         if(map.has(char)){
//             map.set(char,0)
//         }
//     }
//     // code goes here  
//     return str; 

//   }

//   // keep this function call here 
//   console.log(StringChallenge(readline()));

// function StringChallenge(str) {
//     let maxUniqueCount = 0;

//     for (let i = 0; i < str.length; i++) {
//         const currentChar = str[i];

//         const lastIndex = str.lastIndexOf(currentChar);

//         if (lastIndex > i) {
//             const substring = str.substring(i + 1, lastIndex);

//             const uniqueChars = new Set(substring);


//             if (uniqueChars.size > maxUniqueCount) {
//                 maxUniqueCount = uniqueChars.size;
//             }
//         }
//     }

//     return maxUniqueCount;
// }

// // Test cases
// console.log(StringChallenge("ahyjakh")); // Output: 4
// console.log(StringChallenge("ghececgkaem")); // Output: 5
// console.log(StringChallenge("mmmerme")); // Output: 3
// console.log(StringChallenge("abccdefghi")); // Output: 0

// function reverseBySeparator(string, separator) {
//     return string.split(separator).reverse().join(separator);
// }
// console.log(reverseBySeparator('hello world', " "))
// console.log(reverseBySeparator('hello world', ""))
// console.log(reverseBySeparator(reverseBySeparator('hello world', ""), " "))


// var array = [1, 2, 3, 5, 1, 5, 9, 1, 2, 8];

// Array.from(new Set(array)); // [1, 2, 3, 5, 9, 8]

// console.log(Array.from(new Set(array)))

// const student = {
//     registration: '12342',
//     name: 'Sandeep',
//     age: 27,
// };

// Object.defineProperty(student, 'marks', {
//     value: 98,
//     configurable: true,
//     writable: false,
//     enumerable: false,
// });

// console.log(student);

function makeAdder(x) {
	// parameter `x` is an inner variable

	// inner function `add()` uses `x`, so
	// it has a "closure" over `x`
	function add(y) {
		return y + x;
	};

	return add;
}


var plusOne = makeAdder( 1 ); // x is 1, plusOne has a reference to add(y)
var plusTen = makeAdder( 10 ); // x is 10

console.log(plusOne(3)); // 1 (x) + 3 (y) = 4
console.log(plusTen(13)); // 10 (x) + 13 (y) = 23 