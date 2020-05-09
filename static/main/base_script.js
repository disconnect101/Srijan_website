$(document).ready(function () {

    $('.custom-card-toggle').click(function () {
        var imgsrc = $(this).find("img").attr("src");
        var title = $(this).find('.custom-list-item-title').text();
        var content = $(this).find('.custom-content-description').text();
        var href = $(this).find('input').val();


        
        $(this).parents('.custom-category').find('.card').children("img").attr("src", imgsrc);
        $(this).parents('.custom-category').find('.card').find('.custom-category-card-title').text(title);
        $(this).parents('.custom-category').find('.card').find('.custom-category-card-content').text(content);
        $(this).parents('.custom-category').find('.card').find("a").attr("href", href);
    });
});


/*$(document).ready(function(){
  $("p").click(function(){
    $(this).hide();
  });
});*/


/*.closest('.custom-category').children('#card').children("img").attr("src",)*/


/*
window.onscroll = function() {myFunction()};


var navbar = document.getElementById('navbar');

var sticky = navbar.offsetTop;

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
    console.log('scrolling');
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
}*/

var yourNavigation = $('#navbar');
    stickyDiv = "sticky";
    yourHeader = $('#header').height();



$(window).scroll(function() {
    //console.log($(this).scrollTop() + " " + yourHeader);
    yourHeader = $('#header').height();
var navtoggle = $('a.colorlib-nav-toggle');
    //initpos = navtoggle.css("position");
  if( $(this).scrollTop() > yourHeader ) {
    yourNavigation.addClass(stickyDiv);
    navtoggle.css("position", "fixed");
  } else {
    yourNavigation.removeClass(stickyDiv);
    navtoggle.css("position", "absolute");
  }
});