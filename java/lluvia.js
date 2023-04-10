if (document.getElementById("app")) {
    const { createApp } = Vue
 
    createApp({
        data() {
            return {
                lluvia: [],
                errored: false,
                loading: true,
                url: "http://localhost:5000/lluvia"
                }
        },
        methods: {
            fetchData(url) {
                fetch(url)
                    .then(response => response.json())
                    .then(data => {
                        this.lluvia = data;
                        this.loading = false;
                    })
                    .catch(err => {
                        this.errored = true
                    })},
                    eliminar(lluvia) {
                        const url = 'http://localhost:5000/lluvia/' + lluvia;
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
