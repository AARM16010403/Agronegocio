(function(){
    var actualizarHora=function(){
    var date = new Date();
    var hr = date.getHours();
    var min = date.getMinutes();
    var seg = date.getSeconds();
    cambiarHora(hr,min,seg);
    };
    var cambiarHora=function(hr,min,seg){
    document.getElementById("fyh").innerHTML=hr + ':' + min + ':' + seg;
    };
    actualizarHora();
    var intervalo = setInterval(actualizarHora,1000);
}());