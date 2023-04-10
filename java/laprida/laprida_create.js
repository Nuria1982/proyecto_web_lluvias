function guardar() {
    let f = document.getElementById("txtFecha").value
    let re = parseFloat(document.getElementById("txtRefugio").value)
    let s = parseFloat(document.getElementById("txtSara").value)
    let p = parseFloat(document.getElementById("txtPozos").value)
    let ru = parseFloat(document.getElementById("txtRural").value)
    let t = parseFloat(document.getElementById("txtTegua").value)
    let a = parseFloat(document.getElementById("txtAlegre").value)

    let laprida = {
        fecha: f,
        refugio: re,
        sara: s,
        pozos: p,
        rural: ru,
        tegua: t,
        alegre: a,
    }

    let url = "http://localhost:5000/lapridas"
    var options = {
        body: JSON.stringify(laprida),
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