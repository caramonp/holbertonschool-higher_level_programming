// script that adds a <li> element to a lis
$('div#add_item').click(function () {
  $('ul.my_list').append('<li>Item</li>');
});
