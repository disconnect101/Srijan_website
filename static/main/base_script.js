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

