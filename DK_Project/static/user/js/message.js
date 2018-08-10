function sendmessage(){
    $.get('/loan/user_code/',{'user_tel':$('#user_tel').val()},function(msg){
    });
    return false;

}