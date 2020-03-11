Vue.config.devtools = true

upcoming_movies_vue = new Vue({
    el: '#upcoming_movies_app',
    delimiters: ['[[', ']]'],
  	data: {
  		movies: []
  	},
  	mounted() {
  		let url_string = window.location.href
		let url = new URL(url_string);
		let page_number = url.searchParams.get("page");
		axios.get("/api/get_upcoming_movies?page="+page_number)
		.then(response => {this.movies = response.data.movies})
	}
});