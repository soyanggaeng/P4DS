var h1 = "Welcome to YAMP!";
var h3 = "The Ultimate Youtube Ad Matching Platform";

commit test remote

window.addEventListener('load', function () {

    var header = `<div class="header-overlay"></div>
        <div class="header-content">
            <div class="logo-container">
                <a href="/">
                    <img src="static/img/YAMP_logo.png" alt="YAMP Logo" id="logo" />
                </a>
            </div>
            <div class="header-text">
                <h1>${h1}</h1>
                <h3>${h3}</h3>
            </div>
        </div>`;

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

    
    var nav = `<ul>
    <li><a href="#">Channel Analysis</a>
        <ul>
            <li><a href="/overview">Channel Overview</a></li>
            <li><a href="#">Video & Comment Analysis</a></li>
            <li><a href="/keyword">Keyword Analysis</a></li>
            <li class="advertiser-only"><a href="#">Channel Controversy Check</a></li>
        </ul>
    </li>
    <li><a href="#">Advertisement Analysis</a>
        <ul>
            <li><a href="#">Ad View Estimation</a></li>
            <li><a href="#">Channel's Existing Ad Analysis</a></li>
            <li><a href="#">Advertiser's Ad Request Status</a></li>
            <li class="youtuber-only"><a href="#">Advertiser Overview</a></li>
            <li class="youtuber-only"><a href="#">Advertiser Controversy Check</a></li>
        </ul>
    </li>
    <li><a href="#">Advertisement Proposal</a>
        <ul>
            <li><a href="/proposal">To YouTuber</a></li>
            <li><a href="#">To Advertiser</a></li>
        </ul>
    </li>
    <li><a href="/mypage">My Page</a>
        <ul>
            <li><a href="/mypage#member-information">Member Information</a></li>
            <li><a href="/mypage#analysis-history">Recent Analysis History</a></li>
            <li><a href="/mypage#purchased-service">My Purchased Service</a></li>
            <li><a href="/feedback">Feedback</a></li>
        </ul>
    </li>
</ul>`;

    var footer = `<div class="footer-content">
        <a href="sotube">About SoTube</a>
        <p>&copy; 2023 YAMP. All rights reserved.</p>
    </div>`

    document.querySelector('header').innerHTML = header;
    document.querySelector('footer').innerHTML = footer;
    document.querySelector('nav').innerHTML = nav + document.querySelector('nav').innerHTML;
});

function $(selector){
    return document.querySelector(selector);
}