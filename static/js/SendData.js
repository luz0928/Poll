$(function(){
	$('#btnSendData').click(function(){

		$.ajax({
			url: '/sendData',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){

				console.log(response);
				console.log("1");
			},
			error: function(error){
				console.log(error);
				console.log("2");
			}
		});
	});
});
