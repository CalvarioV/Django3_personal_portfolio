// script.js
window.addEventListener('load', function() {
  var loader = document.getElementById('loader');
  var minimumTimeElapsed = false;
  var pageFullyLoaded = false;

  // Set a timeout for 10 seconds
  setTimeout(function() {
    minimumTimeElapsed = true;
    if (pageFullyLoaded) {
      loader.style.display = 'none';
    }
  }, 10000);

  // Check if page is fully loaded
  pageFullyLoaded = true;
  if (minimumTimeElapsed) {
    loader.style.display = 'none';
  }
});