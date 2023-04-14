function guardar() {
    let f = document.getElementById("txtFecha").value
    let c = parseFloat(document.getElementById("txtColina").value)
    let q = parseFloat(document.getElementById("txtQuerencia").value)
    let l = parseFloat(document.getElementById("txtLamadrid").value)


    let lamadrid = {
        fecha: f,
        colina: C,
        querencia: q,
        lamadrid: l,
    }

    let url = "http://localhost:5000/lamadrids"
    var options = {
        body: JSON.stringify(lamadrid),
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