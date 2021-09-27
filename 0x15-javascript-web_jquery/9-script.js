// script that fetches froma URL and displays the value of hello
$.get('https://fourtonfish.com/hellosalut/?lang=fr', (data) => {
  $('#hello').text(data.hello);
});
