---
layout: About
permalink: /about
feedformat: card
title: "About me"
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

/* Timeline Item Styles */
.timeline-item {
    background: #f9f9f9;
    margin: 20px 0;
    padding: 20px 25px;
    border-left: 3px solid #0078d4;
    border-radius: 8px;
    position: relative;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

/* Header Section for Title and Date */
.timeline-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    flex-wrap: wrap;
}

/* Event Title Styles */
.timeline-title {
    max-width: 70%;
}

.timeline-title h4 {
    margin: 0;
    font-family: Arial, sans-serif;
    font-size: 1.2em; /* Increased font size for better visibility */
    font-weight: bold;
    color: #000000;
}

/* Date Subtitle Styles */
.timeline-date {
    margin-top: 5px;
    font-family: Arial, sans-serif;
    font-size: 1em; /* Adjust as needed */
    color: #555;
}

/* Company and Location Styles */
.timeline-company {
    text-align: right;
    max-width: 25%;
}

.timeline-company p {
    margin: 0;
    font-family: Arial, sans-serif;
    font-size: 0.95em; /* Slightly larger than original */
    color: #333;
}

/* Bullet Points Styles */
.timeline-item ul {
    margin: 15px 0 0 20px;
    padding: 0;
    list-style-type: disc;
    font-size: 1em; /* Increased font size */
    color: #555;
}

.timeline-item ul li {
    margin-bottom: 5px; /* Reduced space between bullet points */
    line-height: 1.5; /* Improved readability */
}

/* Responsive Adjustments */
@media (max-width: 600px) {
    .timeline-header {
        flex-direction: column;
    }
    
    .timeline-title, .timeline-company {
        max-width: 100%;
        text-align: left;
    }
    
    .timeline-company {
        margin-top: 10px;
    }
}
</style>

<div class="timeline">

    <!-- Timeline Item 1 -->
    <div class="timeline-item" data-aos="fade-left">
        <div class="timeline-header">
            <div class="timeline-title">
                <h4>Building Mathematics Superintelligence</h4>
                <div class="timeline-date">Nov. 2024 - Present</div>
            </div>
            <div class="timeline-company">
                <p><strong>Independent Project</strong> - Palo Alto, CA</p>
            </div>
        </div>
        <ul>
            <li>Developing an AI capable of solving and verifying mathematical problems with near 100% accuracy.</li>
            <li>Leveraging techniques like PyTorch, fine-tuning/QLoRA, and vector databases.</li>
        </ul>
    </div>

    <!-- Timeline Item 2 -->
    <div class="timeline-item" data-aos="fade-left">
        <div class="timeline-header">
            <div class="timeline-title">
                <h4>Deep Learning Research Assistant</h4>
                <div class="timeline-date">Sep. 2024 - Nov. 2024</div>
            </div>
            <div class="timeline-company">
                <p><strong>Purdue University, Laboratory of Data Science</strong> - Fort Wayne, IN</p>
            </div>
        </div>
        <ul>
            <li>Managed cross-functional teams to implement agile workflows.</li>
            <li>Optimized processes to enhance research efficiency in machine learning projects.</li>
        </ul>
    </div>

    <!-- Timeline Item 3 -->
    <div class="timeline-item" data-aos="fade-left">
        <div class="timeline-header">
            <div class="timeline-title">
                <h4>Associate Instructor</h4>
                <div class="timeline-date">Aug. 2022 - May 2024</div>
            </div>
            <div class="timeline-company">
                <p><strong>Indiana University</strong> - Bloomington, IN</p>
            </div>
        </div>
        <ul>
            <li>Conducted seminars on pure mathematics, focusing on advanced topics and Fields Medal discussions.</li>
            <li>Taught undergraduate-level mathematics courses, developing new curricula for abstract algebra.</li>
        </ul>
    </div>

    <!-- Timeline Item 4 -->
    <div class="timeline-item" data-aos="fade-left">
        <div class="timeline-header">
            <div class="timeline-title">
                <h4>Brain Age Researcher</h4>
                <div class="timeline-date">2019 - 2020</div>
            </div>
            <div class="timeline-company">
                <p><strong>Indiana University</strong> - Bloomington, IN</p>
            </div>
        </div>
        <ul>
            <li>Collaborated on predicting brain aging through statistical analysis and machine learning.</li>
            <li>Published findings on differential geometry-based algorithms in peer-reviewed journals.</li>
        </ul>
    </div>

    <!-- Timeline Item 5 (Education) -->
    <div class="timeline-item" data-aos="fade-left">
        <div class="timeline-header">
            <div class="timeline-title">
                <h4>Education</h4>
                <div class="timeline-date">2020 - 2024</div>
            </div>
            <div class="timeline-company">
                <p><strong>Indiana University</strong> - Bloomington, IN</p>
            </div>
        </div>
        <ul>
            <li>Master of Arts in Mathematics (2024), GPA: 3.89/4.00</li>
            <li>Bachelor of Science in Mathematics (2022), GPA: 3.86/4.00, graduated with honors.</li>
            <li>Recipient of the Dean’s Award for Excellence.</li>
        </ul>
    </div>

</div>
