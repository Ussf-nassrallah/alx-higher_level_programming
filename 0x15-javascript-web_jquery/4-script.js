/*
script that toggles the class of the <header> element
when the user clicks on the tag DIV#toggle_header
*/

$(document).ready(function () {
  $('#toggle_header').click(function () {
    const hdr = $('header');
    if (hdr.hasClass('green')) {
      hdr.removeClass('green');
      hdr.addClass('red');
    } else {
      hdr.removeClass('red');
      hdr.addClass('green');
    }
  });
});