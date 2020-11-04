var bar = document.getElementById('bar-toggle');
var times = document.getElementById('times-toggle');

bar.addEventListener('click', function() {
    document.querySelector('.logo-list').style.display = 'block';
    document.getElementById('bar-toggle').style.display = 'none';
    document.querySelector('.times').style.display ='block';
});


times.addEventListener('click', function() {
    document.querySelector('.logo-list').style.display = 'none';
    document.getElementById('bar-toggle').style.display = 'block';
    document.querySelector('.times').style.display ='none';
});


window.addEventListener('scroll', function() {
    const header = document.querySelector('header');
    header.classList.toggle('sticky', window.scrollY > 0);
});