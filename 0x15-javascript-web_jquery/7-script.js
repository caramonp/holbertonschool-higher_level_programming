// script that fetches the character name from a URL
$.get('https://swapi.co/api/people/5/?format=json', function (data) {
  $('div#character').text(data.name);
});
