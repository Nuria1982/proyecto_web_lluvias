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
document.getElementById("txtCampoamor").value = decodeURIComponent(parts[2][1])
document.getElementById("txtLopez").value = decodeURIComponent(parts[3][1])
document.getElementById("txtDionisia").value = decodeURIComponent(parts[4][1])
document.getElementById("txtSMN").value = decodeURIComponent(parts[5][1])
document.getElementById("txtUriburu").value = decodeURIComponent(parts[6][1])


function modificar() {
    let id = document.getElementById("txtId").value
    let f = document.getElementById("txtFecha").value
    let c = parseFloat(document.getElementById("txtCampoamor").value)
    let l = parseFloat(document.getElementById("txtLopez").value)
    let d = parseFloat(document.getElementById("txtDionisia").value)
    let s = parseFloat(document.getElementById("txtSMN").value)
    let u = parseFloat(document.getElementById("txtUriburu").value)

    let benito = {
        fecha: f,
        campoamor: c,
        lopez: l,
        dionisia: d,
        smn: s,
        uriburu: u,
    }
    let url = "http://localhost:5000/benitos/"+id
    var options = {
        body: JSON.stringify(benito),
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