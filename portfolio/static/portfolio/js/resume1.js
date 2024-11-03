// script.js
document.addEventListener('DOMContentLoaded', () => {
    const progressBars = document.querySelectorAll('.progress-bar');

    const fillProgressBar = (progressBar) => {
        const value = progressBar.getAttribute('data-value');
        progressBar.style.width = `${value}%`;
    };

    const handleScroll = () => {
        progressBars.forEach(progressBar => {
            const rect = progressBar.getBoundingClientRect();
            if (rect.top >= 0 && rect.bottom <= window.innerHeight) {
                fillProgressBar(progressBar);
            }
        });
    };

    window.addEventListener('scroll', handleScroll);
    window.addEventListener('load', handleScroll);
});


