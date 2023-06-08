window.onload = function () {
    var btn = $('#login-button') != null ? $('#login-button') : $('#logout-button');
    var modal = document.getElementById('loginModal');
    var menuLinks = document.querySelectorAll('nav a');
    var isLoggedIn = $('#login-button') != null ? false : true;

    // fetch('./login_status')
    // .then(response => response.json())
    // .then(data => {
    //     var isLoggedIn = data.login_status;

    //     menuLinks.forEach(function(link) {
    //         link.onclick = function(e) {
    //             e.preventDefault();
    //             if (!isLoggedIn) {
    //                 modal.style.display = 'block';
    //             }
    //         }
    //     });

    //     if(isLoggedIn){
    //         btn.onclick = function(e) {
    //             e.preventDefault();
    //             window.location.href = "/logout";
    //         }
    //     }
    // });



    // When the user clicks on the button, open the modal 

    menuLinks.forEach(function(link) {
        link.onclick = function(e) {
            if (!isLoggedIn) {
                e.preventDefault();
                modal.style.display = 'block';
                    // Close modal when 'x' is clicked
                var span = document.getElementsByClassName("close")[0];
                span.onclick = function() {
                modal.style.display = "none";
                }

                // Close modal when clicked outside
                window.onclick = function(event) {
                if (event.target == modal) {
                    modal.style.display = "none";
                }
                }
            }else if (link.hash !== '' && location.pathname == '/mypage') {
                e.preventDefault();
                scrollToSection(link.hash);
            }
        }})

    if(isLoggedIn){
        btn.onclick = function() {
            window.location.href = "/logout";
        }
    }
}

function nextStep(id) {
    switch(id) {
        case 'continueYoutube':
            // Continue with Youtube account
            // Add your Youtube authentication process here
            break;
        case 'continueGoogle':
            // Continue with Google account
            // Add your Google authentication process here
            break;
        case 'emailLogin':
            // Login with email
            window.location.href = "/login";
            break;
        case 'emailRegistration':
            // Register now
            window.location.href = "/register";
            break;
    }
}


function $(selector){
    return document.querySelector(selector);
}

function scrollToSection(sectionId) {
    var section = document.querySelector(sectionId);
    if (section) {
        section.scrollIntoView({ behavior: 'smooth' });
    }
}



