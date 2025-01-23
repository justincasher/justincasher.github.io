# Gemfile
#
# This Gemfile is designed for a GitHub Pages–compatible environment.
# By using the 'github-pages' gem, you're locking in the same Jekyll
# version and associated dependencies that GitHub Pages uses.
# 
# IMPORTANT: If you previously had `gem "jekyll", "~> 4.0.0"` in this file,
# remove or comment out that line. GitHub Pages bundles its own (older) Jekyll
# version. Combining both leads to dependency conflicts.

source "https://rubygems.org"

# ─────────────────────────────────────────────────────────────────────────────
# GitHub Pages Gem
# ─────────────────────────────────────────────────────────────────────────────
# This gem provides a pinned version of Jekyll (3.x) plus all the plugins
# GitHub Pages supports out-of-the-box. Installing it ensures your local
# environment matches GitHub Pages' production environment.
gem "github-pages", group: :jekyll_plugins


# ─────────────────────────────────────────────────────────────────────────────
# Jekyll Plugins
# ─────────────────────────────────────────────────────────────────────────────
# If you want additional plugins that GitHub Pages *does* support, add them
# here. (Check GitHub Pages docs for the supported plugin list.)
group :jekyll_plugins do
  # Official feed generator for Jekyll: creates an Atom feed at /feed.xml
  gem "jekyll-feed", "~> 0.12"

  # Cleans up and minifies HTML/CSS output (if GitHub Pages allows it).
  # Check https://github.com/JohnAlbin/jekyll-tidy for compatibility info.
  gem "jekyll-tidy"
end

# Some other typical Jekyll plugins or libraries you might use:
gem "jekyll-sitemap"        # Generates a sitemap.xml for your site
gem "kramdown-math-katex"   # Renders math with KaTeX for Jekyll

# webrick is often required by Jekyll 3.x on newer Rubies
gem "webrick", "~> 1.7"


# ─────────────────────────────────────────────────────────────────────────────
# Default Gems Removed in Ruby 3.4
# ─────────────────────────────────────────────────────────────────────────────
# In Ruby 3.4 and later, certain libraries (csv, base64, logger, bigdecimal, etc.)
# are no longer included as default gems. If older plugins or parts of Jekyll
# assume they're available, you need to explicitly install them:
gem "csv"
gem "base64"
gem "logger"
gem "bigdecimal"


# ─────────────────────────────────────────────────────────────────────────────
# Platform-Specific Gems
# ─────────────────────────────────────────────────────────────────────────────
# Windows (and JRuby) doesn't bundle certain time-zone data, so these help:
install_if -> { RUBY_PLATFORM =~ %r!mingw|mswin|java! } do
  gem "tzinfo", "~> 1.2"
  gem "tzinfo-data"
end

# On Windows, wdm can improve file-watching performance (jekyll serve --watch):
gem "wdm", "~> 0.1.1", install_if: Gem.win_platform?
