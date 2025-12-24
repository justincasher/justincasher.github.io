document.addEventListener('DOMContentLoaded', function() {
  const filterButtons = document.querySelectorAll('.filter-btn');
  const articles = document.querySelectorAll('.article-preview');
  const dividers = document.querySelectorAll('.divider');

  function updateVisibility(filter) {
    // Filter articles
    articles.forEach(article => {
      const subject = article.getAttribute('data-subject');

      if (filter === 'all' || subject === filter) {
        article.classList.remove('hidden');
      } else {
        article.classList.add('hidden');
      }
    });

    // Hide dividers with no visible articles
    dividers.forEach((divider, index) => {
      let hasVisibleArticles = false;
      let currentElement = divider.nextElementSibling;

      // Check all elements until next divider or end
      while (currentElement) {
        if (currentElement.classList.contains('divider')) {
          break;
        }
        if (currentElement.classList.contains('article-preview') &&
            !currentElement.classList.contains('hidden')) {
          hasVisibleArticles = true;
          break;
        }
        currentElement = currentElement.nextElementSibling;
      }

      if (hasVisibleArticles) {
        divider.classList.remove('hidden');
      } else {
        divider.classList.add('hidden');
      }
    });
  }

  filterButtons.forEach(button => {
    button.addEventListener('click', function() {
      const filter = this.getAttribute('data-filter');

      // Update active button
      filterButtons.forEach(btn => btn.classList.remove('active'));
      this.classList.add('active');

      updateVisibility(filter);
    });
  });
});
