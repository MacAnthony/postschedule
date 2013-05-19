$(function(){
	$('.collapse').collapse();
	$('a[rel="tooltip"]').tooltip();
	$('.dateinput').datepicker({
		format: 'yyyy-mm-dd'
	});
	$('.timeinput').timepicker({
		template: 'dropdown'
	});
});