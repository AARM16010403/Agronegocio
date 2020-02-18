(function(){
    var agregarCero=function(dato){
        if(dato<10){
            dato = '0'+dato;
        }
        return dato;
    };
    var actualizarHora=function(){
    var date = new Date();
    var hr = agregarCero(date.getHours());
    var min = agregarCero(date.getMinutes());
    var seg = agregarCero(date.getSeconds());
    var dia = agregarCero(date.getDate());
    var mes = agregarCero(date.getMonth()+1);
    var year = date.getFullYear();
    var tiempo = 'a. m.';
    if(hr>12){
        hr=hr-12;
        tiempo = 'p. m.';
    }
    cambiarHora(dia,mes,year,hr,min,seg,tiempo);
    };
    var cambiarHora=function(dia,mes,year,hr,min,seg,tiempo){
    document.getElementById("fyh").innerHTML= dia + '/' + mes + '/' + year + ' ' + hr + ':' + min + ':' + seg + ' ' + tiempo;
    };
    actualizarHora();
    var intervalo = setInterval(actualizarHora,1000);
}());