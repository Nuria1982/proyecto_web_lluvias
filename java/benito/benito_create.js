function guardar() {
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

    let url = "http://localhost:5000/benitos"
    var options = {
        body: JSON.stringify(benito),
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