
$(document).ready(function () {

    uploadImage();

});

// 加载图片，同时给图片添加 a 标签的 href 属性
function uploadImage() {
    $.get(' /market/goods/?good_id_gte=160&good_id_lte=169', function (data) {
        var a_list = $("#screenshots a");
        var imgs = $("#screenshots a div img");
        for (var i = 0; i += 1; i <= 9) {
            var src = data[i]["slider_imgs"][0];
            var good_id = data[i]["good_id"];
            a_list[i].href = '/market/goods/details/' + good_id + '/';
            imgs[i].src = src;
        }
    })
};