const header = document.querySelector('header');

const changeColor = document.body.querySelector('#red_header');
changeColor.addEventListener('click', () => {
    header.style.color = '#FF0000';
});
