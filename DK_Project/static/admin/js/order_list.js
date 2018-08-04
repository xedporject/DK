$(document).ready(function () {
    $.get('/admin/get_order_info/',function (data) {
        var tr_html = template('tr_list',{users:data.user_list})
        $('#test').append(tr_html)
    })
});