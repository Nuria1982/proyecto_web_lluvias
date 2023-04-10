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
document.getElementById("txtVolcan").value = decodeURIComponent(parts[2][1])
document.getElementById("txtAgrar").value = decodeURIComponent(parts[3][1])
document.getElementById("txtInta").value = decodeURIComponent(parts[4][1])
document.getElementById("txtPinos").value = decodeURIComponent(parts[5][1])
document.getElementById("txtAgustin").value = decodeURIComponent(parts[6][1])


function modificar() {
    let id = document.getElementById("txtId").value
    let f = document.getElementById("txtFecha").value
    let v = parseFloat(document.getElementById("txtVolcan").value)
    let a = parseFloat(document.getElementById("txtAgrar").value)
    let i = parseFloat(document.getElementById("txtInta").value)
    let p = parseFloat(document.getElementById("txtPinos").value)
    let ag = parseFloat(document.getElementById("txtAgustin").value)


    let balcarce = {
        fecha: f,
        volcan: v,
        agrar: a,
        inta: i,
        pinos: p,
        agustin: ag,
    }
    let url = "http://localhost:5000/balcarces/"+id
    var options = {
        body: JSON.stringify(balcarce),
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