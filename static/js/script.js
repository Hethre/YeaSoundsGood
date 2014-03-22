$('#alreadyHaveAccount').click(function() {
	toggleLoginOrCreateAccount();
	$(this).hide();
	$('#createAnAccount').show();
});

$('#createAnAccount').click(function() {
	toggleLoginOrCreateAccount();
	$(this).hide();
	$('#alreadyHaveAccount').show();
});

var toggleLoginOrCreateAccount = function () {
	$('#login').toggle();
	$('.create-account').toggle();
}