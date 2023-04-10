if (document.getElementById("app")) {
    const { createApp } = Vue
 
    createApp({
        data() {
            return {
                mdps: [],
                errored: false,
                loading: true,
                url: "http://localhost:5000/mdps"
                }
        },
        methods: {
            fetchData(url) {
                fetch(url)
                    .then(response => response.json())
                    .then(data => {
                        this.mdps = data;
                        this.loading = false;
                    })
                    .catch(err => {
                        this.errored = true
                    })},
                    eliminar(mdp) {
                        const url = 'http://localhost:5000/mdps/' + mdp;
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
        
