$(document).ready(function(){

	var form = $('#chat_forms');

	function get_message(){
		var url_id = $('.hidden_input').val();
		var url = 'get_messages/' + url_id + '/';
		var data = {}
		$.get(url, function(data) {
			  $('.result').html(data);
			  alert('Загрузка завершена.');
			});
	};

	form.on('submit', function(e){
		e.preventDefault();
		console.log('Good')
		get_message()
		
	})

});