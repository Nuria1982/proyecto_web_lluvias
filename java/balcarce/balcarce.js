if (document.getElementById("app")) {
    const { createApp } = Vue
 
    createApp({
        data() {
            return {
                balcarces: [],
                errored: false,
                loading: true,
                url: "http://localhost:5000/balcarces"
                }
        },
        methods: {
            fetchData(url) {
                fetch(url)
                    .then(response => response.json())
                    .then(data => {
                        this.balcarces = data;
                        this.loading = false;
                    })
                    .catch(err => {
                        this.errored = true
                    })},
                    eliminar(balcarce) {
                        const url = 'http://localhost:5000/balcarces/' + balcarce;
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
        