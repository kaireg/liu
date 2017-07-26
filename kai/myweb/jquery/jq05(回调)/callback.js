/**
 * Created by root on 17-1-24.
 */



//回调

$(document).ready(function () {
    $('#btn').click(function () {
        $('p').hide(1000,function () {
            $('#btn').text('没的点了');
        })
    });
    $('#bt').click(function () {
        $('p').css('color','red').slideDown(1000).slideUp(1000);
    })
});