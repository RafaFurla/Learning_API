var request = new XMLHttpRequest();
request.open('GET', 'http://api.giphy.com/v1/gifs/random?api_key=8zYE3837FQa3T3XvB64AUgahkZO8asXP&tag=houses');
request.onload = function() {
    var response = request.response;
    var parsedData = JSON.parse(response);
    console.log(parsedData);
    var OriginalUrl = parsedData.data.images.downsized.url;
    var img = document.createElement('img');
    img.setAttribute('src', OriginalUrl);
    document.body.appendChild(img);
};

request.send();
