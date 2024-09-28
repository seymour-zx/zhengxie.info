const toggleButton = document.querySelector('.toggle-button');
const sidebar = document.querySelector('.sidebar');
const content = document.querySelector('.content');
toggleButton.addEventListener('click', function() {
  if (sidebar.style.width === '0') {
    sidebar.style.width = '20%';
    content.style.width = '80%';
  } else {
    sidebar.style.width = '0';
    content.style.width = '100%';
  }
});