console.log(location.search)     // lee los argumentos pasados a este formulario
var args = location.search.substr(1).split('&');  
//separa el string por los “&” creando una lista [“id=3” , “nombre=’tv50’” , ”precio=1200”,”stock=20”]
console.log(args)
var parts = []
for (let i = 0; i < args.length; ++i) {
    parts[i] = args[i].split('=');
}
//decodeUriComponent elimina los caracteres especiales que recibe en la URL 
document.getElementById("txtId").value = decodeURIComponent(parts[0][1])
document.getElementById("txtFecha").value = decodeURIComponent(parts[1][1])
document.getElementById("txtRefugio").value = decodeURIComponent(parts[2][1])
document.getElementById("txtSara").value = decodeURIComponent(parts[3][1])
document.getElementById("txtPozos").value = decodeURIComponent(parts[4][1])
document.getElementById("txtRural").value = decodeURIComponent(parts[5][1])
document.getElementById("txtTegua").value = decodeURIComponent(parts[6][1])
document.getElementById("txtAlegre").value = decodeURIComponent(parts[7][1])


function modificar() {
    let id = document.getElementById("txtId").value
    let f = document.getElementById("txtFecha").value
    let re = parseFloat(document.getElementById("txtRefugio").value)
    let s = parseFloat(document.getElementById("txtSara").value)
    let p = parseFloat(document.getElementById("txtPozos").value)
    let ru = parseFloat(document.getElementById("txtRural").value)
    let t = parseFloat(document.getElementById("txtTegua").value)
    let a = parseFloat(document.getElementById("txtAlegre").value)

    let laprida = {
        fecha: f,
        refugio: re,
        sara: s,
        pozos: p,
        rural: ru,
        tegua: t,
        alegre: a,
    }
    let url = "http://localhost:5000/lapridas/"+id
    var options = {
        body: JSON.stringify(laprida),
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        redirect: 'follow'
    }
    fetch(url, options)
        .then(function () {
            console.log("modificado")
            alert("Registro modificado")
        })
        .catch(err => {
            //this.errored = true
            console.error(err);
            alert("Error al Modificar")
        })      
}
