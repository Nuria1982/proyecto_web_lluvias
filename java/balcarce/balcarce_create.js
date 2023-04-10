function guardar() {
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

    let url = "http://localhost:5000/balcarces"
    var options = {
        body: JSON.stringify(balcarce),
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