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
document.getElementById("txtColina").value = decodeURIComponent(parts[2][1])
document.getElementById("txtQuerencia").value = decodeURIComponent(parts[3][1])
document.getElementById("txtLamadrid").value = decodeURIComponent(parts[4][1])


function modificar() {
    let id = document.getElementById("txtId").value
    let f = document.getElementById("txtFecha").value
    let c = parseFloat(document.getElementById("txtColina").value)
    let q = parseFloat(document.getElementById("txtQuerencia").value)
    let l = parseFloat(document.getElementById("txtLamadrid").value)


    let lamadrid = {
        fecha: f,
        colina: c,
        querencia: q,
        lamadrid: l,
    }
    let url = "http://localhost:5000/lamadrids/"+id
    var options = {
        body: JSON.stringify(lamadrid),
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