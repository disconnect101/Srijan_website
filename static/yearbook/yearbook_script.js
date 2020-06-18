arrlist = [];
year = null;
counter = 0;
fulllength = 0;

$(document).ready(function () {
    arrlist = $('.regno-list-item');
    fulllength = arrlist.length;
    console.log(arrlist[0].childNodes[0].innerText + " " + fulllength + " " + counter);

        $('#toggle-gallery').on('click', function () {
        $('#imagelist').css('display', 'block');
        $('#regnolist').css('display', 'none');
    });

    $('#toggle-regno').on('click', function () {
        $('#imagelist').css('display', 'none');
        $('#regnolist').css('display', 'block');
    });

});

$(window).scroll(function () {
    if(($(window).scrollTop() + $(window).height() == $(document).height()) && $('#imagelist').css('display')=='block'){
        for(var i=1 ; i<=6 && counter<fulllength ; i++, counter++)
            $('#imagelist').append('<div style="padding: 1em;margin: 1em auto; font-size: 15px; border: 5px solid lightgrey; height: 270px" class="col-lg-2 col-md-3 col-sm-4 col-xs-6 text-center custom-font-2"><img  style="width: 100%;max-height: 180px ; margin-bottom: 0.5em;" src="' + arrlist[counter].childNodes[1].innerText + '"><b>' + arrlist[counter].childNodes[2].innerText + '</b><br>' + arrlist[counter].childNodes[0].innerText + '</div>');
    }
});



