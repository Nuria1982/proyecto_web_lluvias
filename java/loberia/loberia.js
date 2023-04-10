if (document.getElementById("app")) {
    const { createApp } = Vue
 
    createApp({
        data() {
            return {
                loberias: [],
                errored: false,
                loading: true,
                url: "http://localhost:5000/loberias"
                }
        },
        methods: {
            fetchData(url) {
                fetch(url)
                    .then(response => response.json())
                    .then(data => {
                        this.loberias = data;
                        this.loading = false;
                    })
                    .catch(err => {
                        this.errored = true
                    })},
                    eliminar(loberia) {
                        const url = 'http://localhost:5000/loberias/' + loberia;
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