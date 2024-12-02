---
layout: Post
permalink: /about
feedformat: card
title: "About Me"
---

<style>
:root {
  --primary-color: #212121;
  --background-color: #111;
  --font: sans-serif;
}

* {
  margin: 0;
  padding: 0;
}

body {
  background: var(--background-color);
  font-family: var(--font);
  display: flex;
  justify-content: center;
}

/* Timeline Container */
.timeline {
  background: var(--primary-color);
  margin: 20px auto;
  padding: 20px;
}

/* Outer container for timeline */
.outer {
  position: relative;
  padding: 20px 0;
}

/* Card container */
.card {
  position: relative;
  max-width: 400px;
  margin: 20px 0;
}

/* Setting padding based on even or odd */
.card:nth-child(odd) {
  padding: 30px 0 30px 30px;
  align-self: flex-start;
}
.card:nth-child(even) {
  padding: 30px 30px 30px 0;
  align-self: flex-end;
}

/* Global ::before */
.card::before {
  content: "";
  position: absolute;
  top: 20px;
  width: 50px;
  height: 2px;
  background: orangered;
}

/* Connecting lines */
.card:nth-child(odd)::before {
  left: -50px;
}
.card:nth-child(even)::before {
  right: -50px;
}

/* Information about the timeline */
.info {
  display: flex;
  flex-direction: column;
  background: #333;
  color: gray;
  border-radius: 10px;
  padding: 20px;
  position: relative;
  width: 100%;
}

/* Title of the card */
.title {
  color: orangered;
  position: relative;
  margin-bottom: 10px;
}

/* Timeline dot */
.title::before {
  content: "";
  position: absolute;
  top: 10px;
  width: 10px;
  height: 10px;
  background: white;
  border-radius: 50%;
  border: 3px solid orangered;
}

/* Aligning titles and dots */
.card:nth-child(odd) .title::before {
  left: -25px;
}
.card:nth-child(even) .title::before {
  right: -25px;
}

/* Text alignment */
.card:nth-child(even) .info .title {
  text-align: right;
}
.card:nth-child(odd) .info .title {
  text-align: left;
}
</style>

<div class="timeline">
  <div class="outer">
    <div class="card">
      <div class="info">
        <h3 class="title">Title 1</h3>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
      </div>
    </div>
    <div class="card">
      <div class="info">
        <h3 class="title">Title 2</h3>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
      </div>
    </div>
    <div class="card">
      <div class="info">
        <h3 class="title">Title 3</h3>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
      </div>
    </div>
    <div class="card">
      <div class="info">
        <h3 class="title">Title 4</h3>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
      </div>
    </div>
    <div class="card">
      <div class="info">
        <h3 class="title">Title 5</h3>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
      </div>
    </div>
  </div>
</div>
