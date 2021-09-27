// JavaScript script that fetches and lists the title for all movies by using a URL
$.ajax({
  url: 'https://swapi.co/api/films/?format=json',
  type: 'GET',
  dataType: 'json'
})
  .done(function (json) {
    const titles = json.results;
    for (let i = 0; i < titles.length; i++) {
      $('UL#list_movies').append('<li>' + titles[i].title + '</li>');
    }
  });
