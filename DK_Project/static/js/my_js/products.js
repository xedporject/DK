  $(document).ready(function(){
$.get('/admin/products/',function(msg){
    console.log(msg.product_info)
    if(msg.code == 200){
       // var pro_html = '<tr><td><img src="'+ msg.product_image+'" class="thumbnail center"/></td><td class="center">'+ msg.product_name + '</td><td class="center">'+msg.product_months+'期</td>\n' +
       //      '      <td class="center">\n' +
       //      '          <i>￥</i>\n' +
       //      '        <em>'+msg.month_pay+'</em>\n' +
       //      '      </td>\n' +
       //      '      <td class="center">\n' +
       //      '       <span>\n' +
       //      '        <i>￥</i>\n' +
       //      '        <em>'+msg.surplus_pay+'</em>\n' +
       //      '       </span>\n' +
       //      '      </td>\n' +
       //      '     </tr>'
        var pro_html = template('tr_list_msg',{products:msg.product_info})
        $('.list-style').append(pro_html)
    }
})

});
