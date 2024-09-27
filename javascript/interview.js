
// const num = '262';

// const str = 'str';

// console.log(parseInt(num)) //262
// console.log(parseInt(str)) //NaN

// const obj1 = [{
//     "name": "asmita",
//     "age": "24"
// },
// { "name": "ashii", "age": "24" }]

// const obj2 = [...obj1];

// obj2[1]["name"] = "anshu"
// console.log("obj1 : ", obj1)
// console.log("obj2 : ", obj2)
/*
    obj1 :  [ { name: 'asmita', age: '24' }, { name: 'anshu', age: '24' } ]
    obj2 :  [ { name: 'asmita', age: '24' }, { name: 'anshu', age: '24' } ]
 */

/*
const obj3 = { name: "Ashii", age: 24, place: 'ranchi' };

const obj1 = { name: "Asmita", details: { age: 24, country: "India" } };
const obj2 = { details: { country: "USA", occupation: "Developer" } };

// const mergedObj = Object.assign({},obj3, obj1, obj2,);
const mergedObj = { ...obj1, ...obj2, ...obj3 };

console.log(mergedObj);
*/
/* Output: {
  name: 'Ashii',
  details: { country: 'USA', occupation: 'Developer' },
  age: 24,
  place: 'ranchi'
}
  */


// function deepMerge(target, source) {
//     for (let key in source) {
//         if (source[key] instanceof Object && key in target) {
//             // Recursively merge nested objects
//             target[key] = deepMerge(target[key], source[key]);
//         } else {
//             // For non-object or non-existing keys, just assign
//             target[key] = source[key];
//         }
//     }
//     return target;
// }

// const obj1 = { name: "Asmita", details: { age: 24, country: "India" } };
// const obj2 = { details: { country: "USA", occupation: "Developer" } };

// const mergedObj = deepMerge({}, obj1, obj2);

// console.log(mergedObj);

// const obj2 = { name: "Ashii", age: 24, place: 'ranchi' };

// const obj1 = { name: "Asmita", country: "chaina" };

// console.log({ ...obj1, ...obj2 })

// const arr1 = [1, 2, 3, 4, 4]
// const arr2 = [2, 3, 4, 4, 2, 5]
// const spread=[...arr1, ...arr2]
// const conacat=arr1.concat(arr2)


// console.log(spread)
// console.log(conacat)
// Array.prototype.push.apply(arr1, arr2);
// console.log(arr1)


// const arr=[10,20,30]
// const [,...rest]=arr
// console.log(rest)

/*
Normal Function vs	Arrow Function
function show1() { console.log("show1",this); }
const show2 = () => console.log("show2",this);

function assume(hey){
    console.log(hey)
    show1()
    show2()
}
assume()

*/