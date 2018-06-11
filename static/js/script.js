$(document).ready(function(){
	var form = $('#chat_forms');

	form.on('submit', function(e){
 		e.preventDefault();

 	var url_id = $('.hidden_input').val();
	var url = '/get_messages/' + url_id + '/';
	var data = {'name': 'name'}
	var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
	data['csrfmiddlewaretoken'] = csrf_token;
 	console.log(url)
	$.post({
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