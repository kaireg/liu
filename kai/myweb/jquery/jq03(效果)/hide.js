/**
 * Created by root on 17-1-22.
 */

$(document).ready(function () {
    for (var i=0; i<6 ;i++){
    $("<div>").appendTo(document.body);
}
$('div').click(function () {
    $(this).hide(1000,function () {
        $(this).remove();
    });
});
});
