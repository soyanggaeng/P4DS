var isLoggedIn = false;

window.onload = function () {
    var btn = document.getElementById('login-button');
    var modal = document.getElementById('loginModal');
    var menuLinks = document.querySelectorAll('nav a');

    // When the user clicks on the button, open the modal 
    btn.onclick = function() {
        modal.style.display = 'block';
    }

    // If a user tries to access any menu without login, open the login modal
    menuLinks.forEach(function(link) {
        link.onclick = function(e) {
            e.preventDefault();
            if (!isLoggedIn) {
                modal.style.display = 'block';
            }
        }
    });

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