arrlist = [];
year = null;


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





