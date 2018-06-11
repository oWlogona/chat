$(document).ready(function(){
	var form = $('#chat_forms');

	form.on('submit', function(e){
 	e.preventDefault();

 	var url_id = $('.hidden_input').val();
	var url = 'get_messages/' + url_id + '/';
	var data = {}
 	console.log('Try')

	$.ajax({
			url: url,
			type: 'POST',
			data: data,
			cache: true,
			success: function(data){
				console.log('OK');
			},
			error: function(){
				console.log('error');
			}
		})
 });

});