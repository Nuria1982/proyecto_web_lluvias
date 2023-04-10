function guardar() {
    let f = document.getElementById("txtFecha").value
    let p = parseFloat(document.getElementById("txtPieres").value)
    let l = parseFloat(document.getElementById("txtLoberia").value)
    let m = parseFloat(document.getElementById("txtManuel").value)
    let c = parseFloat(document.getElementById("txtCantabria").value)

    let loberia = {
        fecha: f,
        pieres: p,
        loberia: l,
        manuel: m,
        cantabria: c,
    }

    let url = "http://localhost:5000/loberias"
    var options = {
        body: JSON.stringify(loberia),
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