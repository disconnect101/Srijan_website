$('#comment-button').on('click', function () {

    var comment = {
        article_id: $('#article-id').val(),
        firstname: $('#fname').val(),
        lastname: $('#lname').val(),
        comment: $('#message').val(),
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
    };

    console.log(comment);

   $.ajax({
       type: 'POST',
       url: '/article/comment/',
       data: comment,
       success: function (data) {
            if (data){
                console.log("data received ",data);
                $('.comment-box').append("<div class=\"comment-post\"><div class='row'>" +

                    "<div class=\"col col-lg-8\"><h1>" + data.firstname + " " + data.lastname + "</h1></div><small class=\"col col-lg-4\" style='text-align: right;margin: auto'>" + " posted: just now" + "</small>" +
                    "</div><p>" + data.comment +  "</p>" +

                    "</div>");
            }
       }
   });
});