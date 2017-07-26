/**
 * Created by root on 17-1-25.
 */

$(document).ready(function () {
    $('#btn').click(function () {
        $('#p').append('biubiubiu');
        $('#p').prepend('dedede');
    });
     $('#btn1').click(function () {
        $('#p1').after('biubiubiu');
        $('#p1').before('dedede');
    });
    $('#btn2').click(function () {
        $('#p').remove();
    });
    $('#btn4').click(function () {
        $('#p1').empty();
    });
});