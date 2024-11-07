const darkModeBtn = document.getElementById("dark-mode-btn");
const themeImage = document.getElementById("themeImage");

darkModeBtn.addEventListener("click", function () {
  document.body.classList.toggle("dark-mode");

  // Fade out the image
  themeImage.style.opacity = 0.1;

  // Wait for the fade-out to complete before changing the src
  setTimeout(() => {
    if (document.body.classList.contains("dark-mode")) {
      themeImage.src = "https://calvariov.pythonanywhere.com/site/subfolder/calvario1Oct23.png"; // Image for dark mode
    } else {
      themeImage.src = "https://calvariov.pythonanywhere.com/site/subfolder/myquotecvlogoFinal.jpg"; // Image for light mode
    }

    // Fade the image back in after changing the src
    themeImage.onload = () => {
      themeImage.style.opacity = 1;
    };
  }, 1000); // Match this with the transition duration (0.5s)
});


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
