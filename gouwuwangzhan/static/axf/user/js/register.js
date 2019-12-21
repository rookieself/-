// $(function () {
//
//     var $username = $("#username_input");
//
//     $username.change(function () {
//         var username = $username.val().trim();
//
//         if (username.length) {
//
//             //    将用户名发送给服务器进行预校验
//             $.getJSON('/axf/checkuser/', {'username': username}, function (data) {
//
//                 console.log(data);
//
//                 var $username_info = $("#username_info");
//
//                 if (data['status'] === 200){
//                     $username_info.html("用户名可用").css("color", 'green');
//                 }else  if(data['status'] ===901){
//                     $username_info.html("用户已存在").css('color', 'red');
//                 }
//
//             })
//
//         }
//
//     })
//
//
// })

$(function () {

    var $username = $("#username_input");

    $username.blur(function () {
        var username = $username.val().trim();
        var $username_info = $('#username_info');
        $.getJSON('/App/checkname', {'username': username}, function (data) {

            if (data.status == 'fail') {
                $username_info.text('用户名不可用').css('color', 'red')
            } else {
                $username_info.text('用户可用').css('color', 'green')
            }
        });

    });


});


function check() {
    var $username = $("#username_input");

    var username = $username.val().trim();

    if (!username) {
        return false
    }

    var info_color = $("#username_info").css('color');

    console.log(info_color);

    if (info_color == 'rgb(255, 0, 0)') {
        return false
    }

    var $password_input = $("#password_input");

    var password = $password_input.val().trim();

    $password_input.val(md5(password));

    return true
}
