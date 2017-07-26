/**
 * Created by root on 17-1-24.
 */


// text()   无法获取到标签内部的标签，只能获取标签的内容
//html()    可以获取标签内的标签和内容

$(document).ready(function () {
    $('#btn1').click(function () {
        var vas = $('#itext').val();
        $('#p1').text(vas);
    });
});