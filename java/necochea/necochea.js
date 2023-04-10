if (document.getElementById("app")) {
    const { createApp } = Vue
 
    createApp({
        data() {
            return {
                necocheas: [],
                errored: false,
                loading: true,
                url: "http://localhost:5000/necocheas"
                }
        },
        methods: {
            fetchData(url) {
                fetch(url)
                    .then(response => response.json())
                    .then(data => {
                        this.necocheas = data;
                        this.loading = false;
                    })
                    .catch(err => {
                        this.errored = true
                    })},
                    eliminar(necochea) {
                        const url = 'http://localhost:5000/necocheas/' + necochea;
                        var options = {
                            method: 'DELETE',
                        }
                        fetch(url, options)
                            .then(res => res.text()) // or res.json()
                            .then(res => {
                                location.reload();
                            })
                    }
                },
                created() {
                    this.fetchData(this.url)
                }
            }).mount('#app')
        }
        