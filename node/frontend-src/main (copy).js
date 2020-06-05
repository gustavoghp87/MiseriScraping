document.getElementById("jurisdiccion").value = "CABA"

document.addEventListener('keydown', function init(event){
    if (event.keyCode === 13) {
        tomarValores();
    }
})




function scrap (calle, min, max, lado, jurisdiccion, cp, timestamp) {

    if (max < min) {
        let auxiliar = min
        min = max
        max = auxiliar
    }
    var cantidad = max - min + 1

    var wb = XLSX.utils.book_new();
    wb.Props = {
        Title: calle,
        Subject: "Subject",
        Author: "MS",
        CreatedDate: new Date(2020, 01, 31)
    };
    wb.SheetNames.push(calle);
    var ws_data = []
    ws_data.push(["DIRECCIÓN", "TELÉFONO", "CP", "LUGAR"])

    calle = "bonifacio"
    var url = "http://www.paginasblancas.com.ar/direccion/s/" + "bonifacio" + "-1192" + "/" +jurisdiccion;
    console.log("Consultando " + url)
    contador = 0

    var req = new XMLHttpRequest();
    req.open('GET', url, false);  // third param is sync/async
    //contador += 1
    //console.log(contador)
    
    req.onreadystatechange = function (aEvt) {
        var dumpy = dump(req.responseText)
        //decoded = decodeURIComponent(req.responseText);
        console.log(dumpy)
        //var direcciones = decoded.split('itemprop="streetAddress"')
        console.log("por empezar a iterar")
        // for (i=1; i<direcciones.length; i++) {
        //     console.log("DIRECCIÓN: " + direcciones[i])
        //     try {
        //         let pos = direcciones[i].indexOf('</span>');
        //         direcciones[i] = direcciones[i].slice(1, pos).trim().replace(/\s+/g, ' ');
        //         console.log("\n Dirección: " + direcciones[i]);
        //         ws_data.push([direcciones[i], "tel", "cp", jurisdiccion]);
        //     } catch (e) {
        //         console.log("Nada en " + i)
        //     }   
        // }
    }
    
    

    
    

    for (j=0; j<0; j++) {
        var numero = j;
        var url = "http://www.paginasblancas.com.ar/direccion/s/" + calle + "-" +numero + "/" +jurisdiccion;
        console.log("Consultando " + url)
        contador = 0

        var req = new XMLHttpRequest();
        req.open('GET', url, true);  // third param is sync/async
        contador += 1
        console.log(contador)
        

        var decoded = decodeURIComponent(req.responseText);

        var direcciones = decoded.split('itemprop="streetAddress"')
    
        console.log("por empezar a iterar")
        for (i=1; i<direcciones.length; i++) {
            console.log("DIRECCIÓN: " + direcciones[i])
            try {
                let pos = direcciones[i].indexOf('</span>');
                direcciones[i] = direcciones[i].slice(1, pos).trim().replace(/\s+/g, ' ');
                console.log("\n Dirección: " + direcciones[i]);
                ws_data.push([direcciones[i], "tel", "cp", jurisdiccion]);
            } catch (e) {
                console.log("Nada en " + i)
            }
            
        }

        var contador = 1
        if (contador%3 == 0) {
            
            req.onreadystatechange = function (aEvt) {
        
                var decoded = decodeURIComponent(req.responseText);
                //console.log(decoded)
                if (decoded.indexOf('itemprop="streetAddress"') != -1) {
                    var direcciones = decoded.split('itemprop="streetAddress"')
    
                    console.log("por empezar a iterar")
                    for (i=1; i<direcciones.length; i++) {
                        console.log("DIRECCIÓN: " + direcciones[i])
                        try {
                            let pos = direcciones[i].indexOf('</span>');
                            direcciones[i] = direcciones[i].slice(1, pos).trim().replace(/\s+/g, ' ');
                            console.log("\n Dirección: " + direcciones[i]);
                            ws_data.push([direcciones[i], "tel", "cp", jurisdiccion]);
                        } catch (e) {
                            console.log("Nada en " + i)
                        }
                        
                    }
                }
            }
        }
        
        

        
    }
    

    console.log("por empezar a XLSX");    
    wb.Sheets[calle] = XLSX.utils.aoa_to_sheet(ws_data);    // array of arrays
    var wbout = XLSX.write(wb, {bookType:'xlsx',  type: 'binary'});

    function s2ab(s) { 
        var buf = new ArrayBuffer(s.length); //convert s to arrayBuffer
        var view = new Uint8Array(buf);  //create uint8array as viewer
        for (var i=0; i<s.length; i++) view[i] = s.charCodeAt(i) & 0xFF; //convert to octet
        return buf;    
    }
    
    saveAs(new Blob([s2ab(wbout)],{type:"application/octet-stream"}), calle + "_" + timestamp + ".xlsx");
    

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





