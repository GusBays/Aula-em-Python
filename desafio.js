//var contador = prompt("Quantos segundos você quer contar?");
//while(contador >=0){
//    alert("faltam " + contador + " segundos!");
//    contador --;
//}

var segundos; 
var tempo = prompt("Quantos segundos você quer contar?");
function contador() {
    tempo = setInterval(alertFunc, 1000);
}
function alertFunc() {
    alert(tempo + " segundos")
    tempo --;
}

