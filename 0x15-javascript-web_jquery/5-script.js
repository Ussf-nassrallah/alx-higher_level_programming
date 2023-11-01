/*
script that adds a <li> element to a list
  when the user clicks on the tag DIV#add_item:
*/

$(document).ready(function () {
  $('#add_item').click(function () {
    // create a new li element
    var newLi = $('<li>');
    // add text into new li element
    newLi.text('Item');
    // append the new li element into my_list
    newLi.appendTo('.my_list');
  });
});