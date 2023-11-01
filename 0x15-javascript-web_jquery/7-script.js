/*
script that fetches the character name from this URL:
  https://swapi-api.alx-tools.com/api/people/5/?format=json
*/

$(document).ready(function (){
  const apiUrl = 'https://swapi-api.alx-tools.com/api/people/5/?format=json'
  $.ajax({
    url: apiUrl,
    method: 'GET',
    dataType: 'json',
    success: function (data) {
      // console.log('Api req success: ' + JSON.stringify(data, null, 2));
      const character = data;
      $('#character').text(character.name);
    },
    error: function (error) {
      console.error("API request failed: " + JSON.stringify(error));
    }
  });
});