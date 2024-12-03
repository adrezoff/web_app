document.addEventListener('DOMContentLoaded', () => {
    flatpickr('.form_datetime input', {
        locale: 'ru',
        dateFormat: 'd.m.Y',
        minDate: 'today',
    });

    flatpickr('.form_time input', {
        enableTime: true,
        noCalendar: true,
        time_24hr: true,
        dateFormat: 'H:i',
    });
});
