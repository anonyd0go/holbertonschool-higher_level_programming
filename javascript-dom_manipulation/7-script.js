fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then((response) => response.json())
  .then((data) => {
    const movieUl = document.querySelector('#list_movies');
    data.results.forEach((movie) => {
        const item = document.createElement('li');
        item.textContent = movie.title;
        movieUl.appendChild(item);
    });
  })
  .catch((error) => {
    console.error('Error fetching movies:', error);
  });