

function search_info(){
    var loan_id = $('#loan_id').val();
    var user_name = $('#user_name').val();
    var user_card = $('#user_card').val()
    var pri_date = $('#pri_date').val()
    var do_ = $('#do_').val()
    var way = $('#way').val()
    $.get('/admin/search_info/?loan_id='+ loan_id + '&user_name='+ user_name + '&user_card='+ user_card +'&pri_date='+ pri_date +'&do_=' + do_ + '&way='+ way , function(msg){
        if(msg.code==200){
            var tr_html = '<tr>\n' +
                '    <th>申请编号</th>\n' +
                '    <th>客户名称</th>\n' +
                '    <th>联系方式</th>\n' +
                '    <th>身份证号码</th>\n' +
                '    <th>办理日期</th>\n' +
                '    <th>处理人</th>\n' +
                '    <th>处理状态</th>\n' +
                '    <th>处理时间</th>\n' +
                '    <th>操作</th>\n' +
                '   </tr>'
             tr_html += template('tr_list',{users:msg.data_info})
        $('#test').html(tr_html)

        }
    })
}