document.getElementById("jurisdiccion").value = "CABA"

document.addEventListener('keydown', function init(event){
    if (event.keyCode === 13) {
        tomarValores();
    }
})




function scrap (calle, min, max, lado, jurisdiccion, cp, timestamp) {

    
    var ws_data = []
    ws_data.push(["DIRECCIÓN", "TELÉFONO", "CP", "LUGAR"])
    min = 1190
    max = 1198

    for (j=min; j<=max; j++) {
        var numero = j
        calle = "bonifacio"
        var url = "http://www.paginasblancas.com.ar/direccion/s/" + calle + "-" + numero + "/" +jurisdiccion;
        console.log("Consultando " + url)
        contador = 0



        var req = new XMLHttpRequest();
        req.open('GET', url, true);  // third param is async/sync
        req.onreadystatechange = function(addEventListener) {
            //contador += 1
            if (contador == 0) {
                var texto = decodeURIComponent(req.response)
                console.log("Contador: " + contador)
                var direcciones = texto.split('itemprop="streetAddress"')
                for (i=1; i<direcciones.length; i++) {
                    //console.log("DIRECCIÓN: " + direcciones[i])
                    try {
                        let pos = direcciones[i].indexOf('</span>');
                        direcciones[i] = direcciones[i].slice(1, pos).trim().replace(/\s+/g, ' ');
                        console.log("\n Dirección: " + direcciones[i]);
                        //ws_data.push([direcciones[i], "tel", "cp", jurisdiccion]);
                    } catch (e) {
                           console.log("Nada en " + i)
                       }   
                    }
            }



        };
        req.send(null)
        new Promise(r => setTimeout(r, 2000))
    }

}





var searchBtn = document.getElementById("searchBtn")
searchBtn.addEventListener('click', function() {
    tomarValores();
});


function depurar (calle) {

    var calle = calle.toLowerCase().trim()
    while (calle.indexOf('ñ') != -1) {
        pos = calle.indexOf('ñ')
        calle = calle.splice(0, pos) + 'n' + calle.splice(pos+1, )
    }

    while (calle.indexOf(' ') != -1) {
        pos = calle.indexOf(' ')
        calle = calle.splice(0, pos) + '-' + calle.splice(pos+1, )
    }

    while (calle.indexOf('á') != -1) {
        pos = calle.indexOf('á')
        calle = calle.splice(0, pos) + 'a' + calle.splice(pos+1, )
    }

    while (calle.indexOf('é') != -1) {
        pos = calle.indexOf('é')
        calle = calle.splice(0, pos) + 'e' + calle.splice(pos+1, )
    }

    while (calle.indexOf('í') != -1) {
        pos = calle.indexOf('í')
        calle = calle.splice(0, pos) + 'i' + calle.splice(pos+1, )
    }

    while (calle.indexOf('ó') != -1) {
        pos = calle.indexOf('ó')
        calle = calle.splice(0, pos) + 'o' + calle.splice(pos+1, )
    }

    while (calle.indexOf('ú') != -1) {
        pos = calle.indexOf('ú')
        calle = calle.splice(0, pos) + 'u' + calle.splice(pos+1, )
    }

    while (calle.indexOf('ü') != -1) {
        pos = calle.indexOf('ü')
        calle = calle.splice(0, pos) + 'u' + calle.splice(pos+1, )
    }

    console.log(calle)
    return calle;
}



function tomarValores() {
    document.getElementById("message").style.display = 'block';
    var calle = document.getElementById('calle').value
    calle = depurar(calle);
    var min = document.getElementById('min').value
    var max = document.getElementById('max').value
    var jurisdiccion = document.getElementById('jurisdiccion').value
    jurisdiccion = depurar(jurisdiccion);
    var cp = document.getElementById('cp').value
    var lado = "pares"
    var timestamp = new Date().getTime()
    timestamp = timestamp.toString().slice(0, 10);
    
    console.log("Calle: " + calle + ", min: " + min + ", max: " + max + ", lado: " + lado
        + ", jurisdicción: " + jurisdiccion + ", cp: " + cp + ", tiempo: " + timestamp)

    scrap (calle, min, max, lado, jurisdiccion, cp, timestamp);
}





