// update header text to "New Header!!!"
//  when the user clicks on div#update_header

$(document).ready(function () {
  $('#update_header').click(function () {
    $('header').text('New Header!!!');
  });
});