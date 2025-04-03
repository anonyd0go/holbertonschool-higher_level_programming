fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then((response) => response.json())
  .then((data) => {
    const helloDiv = document.querySelector('#hello');
    helloDiv.textContent = data.hello;
  })
  .catch((error) => {
    console.error('Error fetching translation:', error);
  });