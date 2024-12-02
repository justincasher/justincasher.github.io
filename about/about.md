---
layout: About
permalink: /about
feedformat: card
title: "About Me"
---
<br/>

<!-- Include AOS Stylesheet -->
<link href="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.css" rel="stylesheet">
<script src="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.js"></script>
<script>
    document.addEventListener('DOMContentLoaded', function () {
        AOS.init();
    });
</script>

<style>
/* Timeline Container Styles */
.timeline {
    margin: 20px auto;
    padding: 0;
    max-width: 800px;
    position: relative;
}

.timeline-item {
    background: #f9f9f9;
    margin: 20px 0;
    padding: 15px 25px;
    border-left: 3px solid #0078d4;
    border-radius: 8px;
    position: relative;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.timeline-item h3, .timeline-item h4 {
    margin: 0 0 10px;
    font-family: Arial, sans-serif;
}

.timeline-item p {
    margin: 5px 0 10px;
    font-family: Arial, sans-serif;
    font-size: 14px;
    color: #333;
}

.timeline-item ul {
    margin: 0;
    padding: 0 0 0 20px;
    list-style-type: disc;
}

.timeline-item ul li {
    margin-bottom: 8px;
    font-size: 14px;
    color: #555;
}
</style>

<div class="timeline">

    <!-- Timeline Item 1 -->
    <div class="timeline-item" data-aos="fade-left">
        <h3>2024 - Present</h3>
        <h4>Current Role</h4>
        <p><strong>[Company Name]</strong> - [Location]</p>
        <ul>
            <li>Leading strategic initiatives to drive business growth.</li>
            <li>Mentored a team of 15 developers and delivered key projects on time.</li>
        </ul>
    </div>

    <!-- Timeline Item 2 -->
    <div class="timeline-item" data-aos="fade-left">
        <h3>2020 - 2024</h3>
        <h4>Previous Role</h4>
        <p><strong>[Company Name]</strong> - [Location]</p>
        <ul>
            <li>Managed cross-functional teams to implement agile workflows.</li>
            <li>Increased operational efficiency by 25% through process optimization.</li>
        </ul>
    </div>

    <!-- Timeline Item 3 -->
    <div class="timeline-item" data-aos="fade-left">
        <h3>2017 - 2020</h3>
        <h4>Earlier Role</h4>
        <p><strong>[Company Name]</strong> - [Location]</p>
        <ul>
            <li>Developed and launched three high-impact applications.</li>
            <li>Key contributor to the company’s flagship product.</li>
        </ul>
    </div>

    <!-- Timeline Item 4 (Education) -->
    <div class="timeline-item" data-aos="fade-left">
        <h3>2013 - 2017</h3>
        <h4>Education</h4>
        <p><strong>[University Name]</strong> - [Location]</p>
        <ul>
            <li>Bachelor's Degree in Computer Science.</li>
            <li>Graduated with honors and received the Dean’s Award for Excellence.</li>
        </ul>
    </div>

</div>
