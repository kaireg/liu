/**
 * Created by root on 17-1-22.
 */


$(document).ready(function () {
   $('#div1').click(function () {
       $('#div4').slideDown(1000);
   });
    $('#div2').click(function () {
       $('#div4').slideUp(1000);
   });
    $('#div3').click(function () {
       $('#div4').slideToggle(1000);
   });
});