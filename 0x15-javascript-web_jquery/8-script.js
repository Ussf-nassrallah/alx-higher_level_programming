/*
JavaScript script that fetches and lists the title for all movies by using this URL:
  https://swapi-api.alx-tools.com/api/films/?format=json
*/

$(document).ready(function () {
  const apiUrl = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.ajax({
    url: apiUrl,
    method: 'GET',
    dataType: 'json',
    success: function (data) {
      console.log('API req success: ' + JSON.stringify(data, null, 2));
      const movies = data.results;
      for (let movieIndex in movies) {
        let movieTitle = movies[movieIndex].title;
        let newLi = $('<li>');
        newLi.text(movieTitle);
        newLi.appendTo('#list_movies')
      }
    },
    error: function (error) {
      console.error("API request failed: " + JSON.stringify(error));
    }
  });
})