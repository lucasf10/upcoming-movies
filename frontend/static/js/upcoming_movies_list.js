upcoming_movies_vue = new Vue({
    el: '#upcoming_movies_app',
    delimiters: ['[[', ']]'],
  	data: {
  		movies: [],
  		total_pages: null,
  		page_number: null,
  	},
  	mounted() {
  		let url_string = window.location.href;
		let url = new URL(url_string);
		this.page_number = url.searchParams.get("page") ? url.searchParams.get("page") : '1';

		axios.get("/api/get_upcoming_movies?page="+this.page_number)
		.then(response => {
			this.movies = response.data.movies;
			this.total_pages = response.data.total_pages;
			this.render_pagination();
		});
	},
	methods: {
		render_pagination: function(){
			if(this.page_number!="1")
				$('.pagination ul').append("<li><a href='/'><<</a></li>");
			for(let i = 1; i <= this.total_pages; i++){
				if(this.page_number == i)
					$('.pagination ul').append("<li><a class='active' href='/?page="+i+"'>"+i+"</a></li>");
				else
					$('.pagination ul').append("<li><a href='/?page="+i+"'>"+i+"</a></li>");
			}
			if(this.page_number!=this.total_pages)
				$('.pagination ul').append("<li><a href='/?page="+this.total_pages+"'>>></a></li>");
		}
	}
});