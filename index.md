<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="UTF-8" />
    <title>Afsan Sarwer | Academic Portfolio</title>
    <link rel="stylesheet" href="style.css" />
    <!-- Fontawesome CDN Link -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  </head>
  <body>
    <!-- Navigation Bar -->
    <nav>
      <div class="navbar">
        <div class="logo"><a href="#">Afsan Sarwer</a></div>
        <ul class="menu">
          <li><a href="#home">Home</a></li>
          <li><a href="#summary">Summary</a></li>
          <li><a href="#contact">Contact Information</a></li>
          <li><a href="#education">Education</a></li>
          <li><a href="#R_interests">Research Interests</a></li>
          <li><a href="#R_experience">Research Experience</a></li>
          <li><a href="#A_experience">Additional Experience</a></li>
          <li><a href="#skills">Technical Skills</a></li>
          <li><a href="#conference">Conference Presentations</a></li>
          <li><a href="#A_courses">Additional Courses</a></li>
        </ul>
      </div>
    </nav>

    <!-- Page Content -->
    <section id="home" class="section">
      <h2>Home</h2>
      <p>Welcome to my academic portfolio. Here you can find all my academic work and experience.</p>
    </section>

    <section id="summary" class="section">
      <h2>Summary</h2>
      <p>Afsan Sarwer is a Doctor of Veterinary Medicine (DVM) and an MS fellow in Microbiology at Bangladesh Agricultural University. Specializing in bioinformatics and whole genome sequencing (WGS), he applies machine learning and deep learning models to advance research.</p>
    </section>

    <section id="contact" class="section">
      <h2>Contact Information</h2>
      <p>Email: <a href="mailto:afsansarwer.bd@gmail.com">afsansarwer.bd@gmail.com</a></p>
      <p>
        <a href="https://www.linkedin.com/in/afsansarwer/" target="_blank">
          <img src="assets/img/linkedin.png" width="50" height="auto" />
        </a>
        <a href="https://www.researchgate.net/profile/Afsan-Sarwer?ev=hdr_xprf" target="_blank">
          <img src="assets/img/researchgate.png" width="50" height="auto" />
        </a>
      </p>
    </section>

    <section id="education" class="section">
      <h2>Education</h2>
      <p>Doctor of Veterinary Medicine (DVM), Bangladesh Agricultural University (Graduating in 2025)</p>
    </section>

    <section id="R_interests" class="section">
      <h2>Research Interests</h2>
      <p>Whole Genome Sequence (WGS), Antimicrobial Resistance (AMR), Bioinformatics, Deep Learning for Medical Diagnostics, Microscopic Image Analysis, Computer Vision in Life Science.</p>
    </section>

    <section id="R_experience" class="section">
      <h2>Research Experience</h2>
      <p>Ongoing Research Project: Whole-Genome-Based Global Phylogeny and Resistome Profiling of ESBL-Producing *Escherichia coli* from Seafish (April 2025 - Present)</p>
    </section>

    <section id="A_experience" class="section">
      <h2>Additional Experience</h2>
      <ul>
        <li>Intern Student, 21st DVM Internship Program 2024 – Faculty of Veterinary Science, Bangladesh Agricultural University (Sept 2024 - Feb 2025)</li>
        <li>Student Member, Veterinary Information Network (VIN) (June 2020 - March 2025)</li>
        <li>Founding Member, Team Utshob – Cultural Innovation and Collaboration (Feb 2020 - Present)</li>
        <li>BYLC Graduate, BYLC Graduate Network (June 2020 - Present)</li>
      </ul>
    </section>

    <section id="skills" class="section">
      <h2>Technical Skills</h2>
      <p>Programming: Python, LaTeX, Data Analysis (NumPy, Pandas, Matplotlib, Seaborn), TensorFlow for Neural Networks</p>
    </section>

    <section id="conference" class="section">
      <h2>Conference Presentations</h2>
      <p>23rd SCAC Conference – Fourth Industrial Revolution and Future Society (National Science & Technology Complex, Dhaka, December 2024)</p>
    </section>

    <section id="A_courses" class="section">
      <h2>Additional Courses</h2>
      <ul>
        <li>IBM (through Coursera): “Data Analysis with Python”</li>
        <li>Wellcome Connecting Science (FutureLearn): “Bacterial Genomes: From DNA to Protein Function using Bioinformatics”</li>
        <li>Bangladesh Youth Leadership Center (BYLC): “CareerX 18”</li>
      </ul>
    </section>

    <!-- Back to Top Button -->
    <div class="button">
      <a href="#home"><i class="fa-solid fa-arrow-up"></i></a>
    </div>

    <script>
      // Smooth Scroll for navigation links
      document.querySelectorAll('.navbar a').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
          e.preventDefault();
          
          document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
          });
        });
      });
    </script>
  </body>
</html>

