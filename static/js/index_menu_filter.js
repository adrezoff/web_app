document.addEventListener('DOMContentLoaded', () => {
    const filterLinks = document.querySelectorAll('.popular_filter a');
    const items = document.querySelectorAll('.p_recype_item_main .col-md-6');

    filterLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const filter = e.target.getAttribute('data-filter');

            items.forEach(item => {
                if (filter === 'all' || item.classList.contains(`category-${filter}`)) {
                    item.style.display = '';
                } else {
                    item.style.display = 'none';
                }
            });

            filterLinks.forEach(link => link.parentElement.classList.remove('active'));
            e.target.parentElement.classList.add('active');
        });
    });
});
