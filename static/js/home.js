// ---------Responsive-navbar-active-animation-----------
function test(){
	var tabsNewAnim = $('#navbarSupportedContent');
	var selectorNewAnim = $('#navbarSupportedContent').find('li').length;
	var activeItemNewAnim = tabsNewAnim.find('.active');
	var activeWidthNewAnimHeight = activeItemNewAnim.innerHeight();
	var activeWidthNewAnimWidth = activeItemNewAnim.innerWidth();
	var itemPosNewAnimTop = activeItemNewAnim.position();
	var itemPosNewAnimLeft = activeItemNewAnim.position();
	$(".hori-selector").css({
		"top":itemPosNewAnimTop.top + "px", 
		"left":itemPosNewAnimLeft.left + "px",
		"height": activeWidthNewAnimHeight + "px",
		"width": activeWidthNewAnimWidth + "px"
	});
	$("#navbarSupportedContent").on("click","li",function(e){
		$('#navbarSupportedContent ul li').removeClass("active");
		$(this).addClass('active');
		var activeWidthNewAnimHeight = $(this).innerHeight();
		var activeWidthNewAnimWidth = $(this).innerWidth();
		var itemPosNewAnimTop = $(this).position();
		var itemPosNewAnimLeft = $(this).position();
		$(".hori-selector").css({
			"top":itemPosNewAnimTop.top + "px", 
			"left":itemPosNewAnimLeft.left + "px",
			"height": activeWidthNewAnimHeight + "px",
			"width": activeWidthNewAnimWidth + "px"
		});
	});
}
$(document).ready(function(){
	setTimeout(function(){ test(); });
});
$(window).on('resize', function(){
	setTimeout(function(){ test(); }, 500);
});
$(".navbar-toggler").click(function(){
	$(".navbar-collapse").slideToggle(300);
	setTimeout(function(){ test(); });
});



// --------------add active class-on another-page move----------
jQuery(document).ready(function($){
	// Get current path and find target link
	var path = window.location.pathname.split("/").pop();

	// Account for home page with empty path
	if ( path == '' ) {
		path = 'index.html';
	}

	var target = $('#navbarSupportedContent ul li a[href="'+path+'"]');
	// Add active class to target link
	target.parent().addClass('active');
});




// Add active class on another page linked
// ==========================================
// $(window).on('load',function () {
//     var current = location.pathname;
//     console.log(current);
//     $('#navbarSupportedContent ul li a').each(function(){
//         var $this = $(this);
//         // if the current path is like this link, make it active
//         if($this.attr('href').indexOf(current) !== -1){
//             $this.parent().addClass('active');
//             $this.parents('.menu-submenu').addClass('show-dropdown');
//             $this.parents('.menu-submenu').parent().addClass('active');
//         }else{
//             $this.parent().removeClass('active');
//         }
//     })
// });

// LOGIN
// const loginText = document.querySelector(".title-text .login");
// const loginForm = document.querySelector("form.login");
// const loginBtn = document.querySelector("label.login");
// const signupBtn = document.querySelector("label.signup");
// const signupLink = document.querySelector("form .signup-link a");
// signupBtn.onclick = (()=>{
//   loginForm.style.marginLeft = "-50%";
//   loginText.style.marginLeft = "-50%";
// });
// loginBtn.onclick = (()=>{
//   loginForm.style.marginLeft = "0%";
//   loginText.style.marginLeft = "0%";
// });
// signupLink.onclick = (()=>{
//   signupBtn.click();
//   return false;
// });




// Smooth Scroll on anchor links
(function() {

	'use strict';

   // Feature Test
   if ( 'querySelector' in document && 'addEventListener' in window && Array.prototype.forEach ) {

	   // Function to animate the scroll
	   var smoothScroll = function (anchor, duration) {

		   // Calculate how far and how fast to scroll
		   var startLocation = window.pageYOffset;
		   var endLocation = anchor.offsetTop;
		   var distance = endLocation - startLocation;
		   var increments = distance/(duration/16);
		   var stopAnimation;

		   // Scroll the page by an increment, and check if it's time to stop
		   var animateScroll = function () {
			   window.scrollBy(0, increments);
			   stopAnimation();
		   };

		   // If scrolling down
		   if ( increments >= 0 ) {
			   // Stop animation when you reach the anchor OR the bottom of the page
			   stopAnimation = function () {
				   var travelled = window.pageYOffset;
				   if ( (travelled >= (endLocation - increments)) || ((window.innerHeight + travelled) >= document.body.offsetHeight) ) {
					   clearInterval(runAnimation);
				   }
			   };
		   }
		   // If scrolling up
		   else {
			   // Stop animation when you reach the anchor OR the top of the page
			   stopAnimation = function () {
				   var travelled = window.pageYOffset;
				   if ( travelled <= (endLocation || 0) ) {
					   clearInterval(runAnimation);
				   }
			   };
		   }

		   // Loop the animation function
		   var runAnimation = setInterval(animateScroll, 16);
	  
	   };

	   // Define smooth scroll links
	   var scrollToggle = document.querySelectorAll('.scroll');

	   // For each smooth scroll link
	   [].forEach.call(scrollToggle, function (toggle) {

		   // When the smooth scroll link is clicked
		   toggle.addEventListener('click', function(e) {

			   // Prevent the default link behavior
			   e.preventDefault();

			   // Get anchor link and calculate distance from the top
			   var dataID = toggle.getAttribute('href');
			   var dataTarget = document.querySelector(dataID);
			   var dataSpeed = toggle.getAttribute('data-speed');

			   // If the anchor exists
			   if (dataTarget) {
				   // Scroll to the anchor
				   smoothScroll(dataTarget, dataSpeed || 500);
			   }

		   }, false);

	   });

   }

})();

//Smooth Scroll
SmoothScroll({
   // Scrolling Core
   animationTime    : 400, // [ms]
   stepSize         : 100, // [px]

   // Acceleration
   accelerationDelta : 50,  // 50
   accelerationMax   : 3,   // 3

   // Keyboard Settings
   keyboardSupport   : true,  // option
   arrowScroll       : 50,    // [px]

   // Pulse (less tweakable)
   // ratio of "tail" to "acceleration"
   pulseAlgorithm   : true,
   pulseScale       : 4,
   pulseNormalize   : 1,

   // Other
   touchpadSupport   : false, // ignore touchpad by default
   fixedBackground   : true, 
   excluded          : ''    
});

// Google Maps
var myCenter = new google.maps.LatLng(9.9150603, 122.8321918);

function initialize() {
 var mapProp = {
   center: myCenter,
   zoom: 12,
   scrollwheel: false,
   draggable: false,
   mapTypeId: google.maps.MapTypeId.ROADMAP
 };

 var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);

 var marker = new google.maps.Marker({
   position: myCenter,
 });

 marker.setMap(map);
}

google.maps.event.addDomListener(window, 'load', initialize);

// Modal Image Gallery
function onClick(element) {
 document.getElementById("img01").src = element.src;
 document.getElementById("modal01").style.display = "block";
}

// Change style of navbar on scroll
window.onscroll = function() {
 myFunction()
};

function myFunction() {
 var navbar = document.getElementById("myNavbar");
 if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
   navbar.className = "w3-navbar" + " w3-card-2" + " w3-animate-top" + " w3-white";
 } else {
   navbar.className = navbar.className.replace(" w3-card-2 w3-animate-top w3-white", "");
 }
}