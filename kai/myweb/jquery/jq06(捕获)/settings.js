/**
 * Created by root on 17-1-24.
 */

$(document).ready(function () {
    $('#btn1').click(function () {
        $('#mp').html('<a href="http://www.baidu.com">百度</a>');
    });
    $('#btn2').click(function () {
        $('#bp').attr({
            'title': '网易',
            'href': 'http://www.163.com'
        });
    });
    $('#btn3').click(function () {
        $('#pid').text(function (i,ot) {
            return 'old:' + ot + 'new:' + (i);
        });
    });

});