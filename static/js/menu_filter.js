document.addEventListener('DOMContentLoaded', () => {
    const filterLinks = document.querySelectorAll('.popular_filter a');
    const items = document.querySelectorAll('.item');

    filterLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();

            filterLinks.forEach(link => link.parentElement.classList.remove('active'));

            link.parentElement.classList.add('active');

            const filter = link.getAttribute('data-filter');

            items.forEach(item => {
                if (filter === 'all' || item.getAttribute('data-category') === filter) {
                    item.style.display = 'block';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    });
});
