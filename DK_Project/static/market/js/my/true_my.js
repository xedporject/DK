$(document).ready(function () {
   $.get('/userinfo/have_IDcard/', function (msg) {

   })
});


$('#true_info').submit(function (e) {
    e.preventDefault();
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    $(this).ajaxSubmit({
        type: 'post',
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        url: '/userinfo/true_info/',
        error: function (msg) {
            console.log(msg);
        },

        success: function (msg) {
            console.log(msg);
            $('#my_avatar').attr('src', msg.true_avatar_url)
        }
    })
});