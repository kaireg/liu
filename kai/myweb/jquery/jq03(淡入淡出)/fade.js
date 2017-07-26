/**
 * Created by root on 17-1-22.
 */

$(document).ready(function () {
    $('#in').on('click',function () {
        $('#div1').fadeIn(1000);
        $('#div2').fadeIn(1500);
        $('#div3').fadeIn(2000);
    });
    $('#out').on('click',function () {
        $('#div1').fadeOut(1000);
        $('#div2').fadeOut(1500);
        $('#div3').fadeOut(2000);
    });
    $('#toggle').on('click',function () {
        $('#div1').fadeToggle(1000);
        $('#div2').fadeToggle(1500);
        $('#div3').fadeToggle(2000);
    });
    $('#to').on('click',function () {
        $('#div1').fadeTo(1000,1);
        $('#div2').fadeTo(1000,0.5);
        $('#div3').fadeTo(1000,0);
    });

});