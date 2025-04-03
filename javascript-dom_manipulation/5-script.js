const header = document.body.querySelector('header');

const updateHeader = document.body.querySelector('#update_header');
updateHeader.addEventListener('click', () => {
    header.textContent = 'New Header!!!';
});
