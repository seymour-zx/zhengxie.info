const sidebar = document.querySelector('.sidebar');
const content = document.querySelector('.content');

sidebar.addEventListener('click', () => {
  sidebar.classList.toggle('active');
  content.classList.toggle('active');
});