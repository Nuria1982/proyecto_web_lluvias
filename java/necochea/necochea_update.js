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
document.getElementById("txtCooperativa").value = decodeURIComponent(parts[2][1])
document.getElementById("txtSantaMarina").value = decodeURIComponent(parts[3][1])
document.getElementById("txtZubillaga").value = decodeURIComponent(parts[4][1])
document.getElementById("txtBuck").value = decodeURIComponent(parts[5][1])
document.getElementById("txtFernandez").value = decodeURIComponent(parts[6][1])
document.getElementById("txtEnergia").value = decodeURIComponent(parts[7][1])
document.getElementById("txtOlivera").value = decodeURIComponent(parts[8][1])
document.getElementById("txtToscas").value = decodeURIComponent(parts[9][1])


function modificar() {
    let id = document.getElementById("txtId").value
    let f = document.getElementById("txtFecha").value
    let c = parseFloat(document.getElementById("txtCooperativa").value)
    let sm = parseFloat(document.getElementById("txtSantaMarina").value)
    let z = parseFloat(document.getElementById("txtZubillaga").value)
    let b = parseFloat(document.getElementById("txtBuck").value)
    let fe = parseFloat(document.getElementById("txtFernandez").value)
    let e = parseFloat(document.getElementById("txtEnergia").value)
    let o = parseFloat(document.getElementById("txtOlivera").value)
    let t = parseFloat(document.getElementById("txtToscas").value)

    let necochea = {
        fecha: f,
        cooperativa: c,
        santamarina: sm,
        zubillaga: z,
        buck: b,
        fernandez: fe,
        energia: e,
        olivera: o,
        toscas: t,
    }
    let url = "http://localhost:5000/necocheas/"+id
    var options = {
        body: JSON.stringify(necochea),
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
