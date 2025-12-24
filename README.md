### About

This is the code behind my personal website. I am using GitHub pages since it is both dynamic and can render LaTeX (using a combination of KaTeX and MathJax). I am hoping this allows me to organize things more easily.

### Running Locally

Prerequisites:
- Install Ruby (check with `ruby -v`)
- Install Bundler: `gem install bundler`

To run the site:
```bash
# Install dependencies
bundle install

# Start the local server
bundle exec jekyll serve --livereload
```

The site will be available at `http://localhost:4000`.
