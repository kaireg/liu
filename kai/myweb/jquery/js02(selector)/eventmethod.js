/**
 * Created by root on 17-1-22.
 */


$(document).ready(function () {
    $('#pid1').click(function () {
        $('#pid1').text("click");
    });
    $('#pid2').dblclick(function () {
        $('#pid2').text("dblclick");
    });
    $('#pid3').mousedown(function () {
        $('#pid3').text("mousedown");
    });
    $('#pid4').mouseenter(function () {
        $('#pid4').text("mouseenter");
    });
     $('#pid5').mouseout(function () {
        $('#pid5').text("mouseout");
    });
      $('#pid6').mouseleave(function () {
        $('#pid6').text("mouseleave");
    });
       $('#pid7').mouseover(function () {
        $('#pid7').text("mouseover");
    });

    //

    $('#btn').on('click',mydemo);    //绑定事件
    $('#btn').off('click',mydemo);      //解除事件
    $('#btn').bind('click',mydemo);       //在这里bind  和on一样 都是绑定事件  建议使用on
    $('#btn').unbind('click',mydemo);
    function mydemo() {
        $('#onp').text('world!');
    }
});