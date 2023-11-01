/*
JavaScript script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr
and displays the value of hello from that fetch in the HTML tag DIV#hello.
*/

$(document).ready(function (){
  const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  $.ajax({
    method: "GET",
    url: apiUrl,
    dataType: "json",
    success: function (response) {
      console.log(response);
      $('#hello').text(response.hello);
    },
    error: function (error) {
      console.error("API request failed: " + JSON.stringify(error));
    }
  });
});