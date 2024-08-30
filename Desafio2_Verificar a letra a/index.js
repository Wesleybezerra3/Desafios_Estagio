let fruta = 'Banana';
let contadorDeAs = 0

for (let i = 0; i <= fruta.length; i++ ){
     if(fruta[i] === 'a' || fruta[i] == 'A'){
        contadorDeAs = contadorDeAs + 1
     }
}

if(contadorDeAs > 0){
    console.log(`Na string contém a letra a. Quantidade de letras As presente ${contadorDeAs}`)
}else{
    console.log(`Na string não contém nenhuma letra a.`)
}
