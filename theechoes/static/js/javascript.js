$(document).ready(function() {
	$('.nav li').click(function() {
		$('.nav').find('.active').removeClass('active');
		$(this).addClass('active');
	});
});
