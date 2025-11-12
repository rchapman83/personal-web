// Read profile pic from DOM data attribute so this file remains static (no Jinja)
document.addEventListener('DOMContentLoaded', function() {
    const terminalBox = document.getElementById('terminal-box');
    const profilePic = terminalBox ? terminalBox.getAttribute('data-profile-pic') || '' : '';

    const terminalContents = {
        home: `
          <p>
            $ echo "Welcome to my digital lair!"<br>
            Welcome to my digital lair!<br><br>
            $ cat home_pg.txt &vert; less <span class="terminal-cursor"></span><br>
            ${ profilePic ? `<img src="${profilePic}" alt="Gravatar" class="rounded float-left mr-3"><br>` : '' }
            My friends call me Chappy, i'm a network engineer and cybersecurity enthusiast with a passion for building secure, reliable systems. 
            With years of experience navigating the complex landscape of IT, I specialize in designing networks that won't drop the ball—and certainly won't drop the packets either! 
            Whether it's crafting resilient network architectures or safeguarding data against the latest security threats, I enjoy solving problems and keeping systems running smoothly.
          </p>
          <p>
            If you're looking for someone who can fortify your infrastructure while keeping the digital gremlins at bay, you've come to the right place. Let's connect and create something secure, scalable, and future-proof.
          </p>
        `,
        blog: `
          <p>
            $ cat blog.txt<br>
            - "How to Secure Your Network"<br>
            - "Automating with Python"<br>
            - "Linux Tips &amp; Tricks"<br>
            <br>
            $ echo "More posts coming soon..."<span class="terminal-cursor"></span>
          </p>
        `,
        projects: `
          <p>
            $ ls projects/<br><br>
            <ul class="list-group list-group-flush">
              <li class="list-group-item"><a href="http://local-xp.guide" target="_blank">Mini city guide</a></li>
              <li class="list-group-item"><a href="https://github.com/rchapman83/python-admin-scripts" target="_blank">Admin scripts</a></li>
              <li class="list-group-item"><a href="http://www.doubles.cards" target="_blank">Doubles webapp</a></li>
              <li class="list-group-item"><a href="http://www.passwd.studio" target="_blank">Password generator</a></li>
            </ul>
            <br>
            $ echo "See my <a href='https://github.com/rchapman83' target='_blank'>Github</a> for more!"<span class="terminal-cursor"></span>
          </p>
        `,
        contact: `
          <p>
            $ whoami<br>
            Rowan Chapman<br><br>    
            $ echo "Let's connect!" &vert; mail -s "Hello Rowan" rowan@example.com <span class="terminal-cursor"></span><br><br>
          </p>
            <!-- Glyphs from feathericons.com -->
            <table class="table table-borderless">
            <tbody>
            <tr>
                <td>
                    <span class="align-middle"><a href="https://www.facebook.com/rnchapman" class="btn btn-hacker" target="_blank"><i data-feather="facebook" color="#007bff"></i> Facebook</a></span>  
                </td>
                <td>
                    <span class="align-middle"><a href="https://twitter.com/rchapman83" class="btn btn-hacker" target="_blank"><i data-feather="twitter" color="#007bff"></i> Twitter aka X</a></span>  
                </td>
            </tr>
            <tr>
                <td>
                    <span class="align-middle"><a href="https://www.instagram.com/chapmanrowan/" class="btn btn-hacker" target="_blank"><i data-feather="instagram" color="#007bff"></i> Instagram</a></span>  
                </td>
                <td>
                  <span class="align-middle"><a href="https://github.com/rchapman83" class="btn btn-hacker" target="_blank"><i data-feather="github" color="#007bff"></i> GitHub</a></span> 
                </td>
            </tr>
            <tr>
                <td>
                    <span class="align-middle"><a href="https://keybase.io/rnchapman" class="btn btn-hacker" target="_blank"><i data-feather="key" color="#007bff"></i> Keybase PGP (8BF1 B07D 75CB AB43)</a></span>  
                </td>
                <td>
                    <span class="align-middle"><a href="https://www.linkedin.com/in/rowan-chapman-b0686895" class="btn btn-hacker" target="_blank"><i data-feather="linkedin" color="#007bff"></i> LinkedIn</a></span>  
                </td>
            </tr>
            </tbody>
            </table> 
        `
    };

    // wire up nav links
    document.querySelectorAll('.nav-link[data-content]').forEach(function(link) {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
            this.classList.add('active');
            const key = this.getAttribute('data-content');
            const content = terminalContents[key] || '';
            const terminalContentEl = document.getElementById('terminal-content');
            if (terminalContentEl) terminalContentEl.innerHTML = content;
            // re-render feather icons in newly-inserted content
            if (window.feather && typeof feather.replace === 'function') {
                feather.replace();
            }
        });
    });

    // initial render of feather icons (for content already on page)
    if (window.feather && typeof feather.replace === 'function') {
        feather.replace();
    }
});