const ulist = document.body.querySelector('.my_list');

const addItem = document.querySelector('#add_item');
addItem.addEventListener('click', () => {
    const item = document.createElement('li');
    item.textContent = 'Item';
    ulist.appendChild(item);
});
