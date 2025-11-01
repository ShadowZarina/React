function replaceElement() {
    let newElement = document.createElement('div');
    newElement.textContent = 'New Content';
    document.getElementById('original').replaceWith(newElement);
}