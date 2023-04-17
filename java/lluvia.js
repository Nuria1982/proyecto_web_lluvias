if (document.getElementById("app")) {
    const { createApp } = Vue;
 
    createApp({
        data() {
            
            return {
                lluvias: [],
                errored: false,
                loading: true,
                url: "http://localhost:5000/lluvias",
                result: null,
                };
        },
        methods: {
            fetchData(url) {
                fetch(url)
                    .then(response => response.json())
                    .then(data => {
                        this.lluvias = data;
                        this.loading = false;
                        this.result = JSON.parse(JSON.stringify(data));
                        console.log(this.result);
                    })
                    .catch((err) => {
                        this.errored = true
                        this.var = err;
                        console.log(this.result);
                    });
                },
                    eliminar(lluvia) {
                        const url = 'http://localhost:5000/lluvias/' + lluvia;
                        var options = {
                            method: 'DELETE',
                            headers: {
                                'Content-Type': 'application/json'}
                        };
                        fetch(url, options)
                            .then(response => response.json())
                            .then(data => {
                                console.log(data);
                                this.fetchData(this.url);
                            })
                            .catch((err) => {
                                this.errored = true
                                this.var = err;
                                console.log(this.result);
                                console.log(err);
                            });
                    },
                },
                created() {
                    this.fetchData(this.url);
                },
            }).mount('#app');
        }
  