Vue.config.devtools = true

upcoming_movies_vue = new Vue({
    el: '#upcoming_movies_app',
    delimiters: ['[[', ']]'],
  	data: {
  		movies: []
  	},
  	mounted() {
		axios.get("/api/get_upcoming_movies")
		.then(response => {this.movies = response.data.movies})
	}
});