const fs=require('fs')

let data="Hello my name is something and i can do something without doing nothing and here everything is done while being nothing."

fs.writeFile("write.txt",data,(err)=>{
    if(err) console.log(err)
})

fs.readFile('write.txt',(err,data)=>{
    if(err) throw err;

    if(data)
    console.log(data.toString());
})



