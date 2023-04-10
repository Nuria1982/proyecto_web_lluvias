function guardar() {
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

    let url = "http://localhost:5000/necocheas"
    var options = {
        body: JSON.stringify(necochea),
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
       // redirect: 'follow'
    }
    fetch(url, options)
        .then(function () {
            console.log("Lluvia ingresada")
            alert("Lluvia ingresada correctamente")
            // Handle response we get from the API
        })
        .catch(err => {
            //this.errored = true
            alert("Error al grabar" )
            console.error(err);
        })
}