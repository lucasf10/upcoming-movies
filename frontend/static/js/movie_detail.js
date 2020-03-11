Vue.config.devtools = true

movie_detail_vue = new Vue({
	el: '#movie_detail_app',
	delimiters: ['[[', ']]'],
		data: {
			movie_data: []
		},
	mounted() {
		axios.get("/api/get_movie_detail/"+movie_id)
		.then(response => {this.movie_data = response.data.movie_detail_data})
	}
});