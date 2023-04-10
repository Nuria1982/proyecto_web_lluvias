function guardar() {
    let f = document.getElementById("txtFecha").value
    let c = parseFloat(document.getElementById("txtCuda").value)
    let s = parseFloat(document.getElementById("txtSerrana").value)
    let b = parseFloat(document.getElementById("txtBiocca").value)

    let mdp = {
        fecha: f,
        cuda: c,
        serrana: s,
        biocca: b,
    }

    let url = "http://localhost:5000/mdps"
    var options = {
        body: JSON.stringify(mdp),
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