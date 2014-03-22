$('#already-have-account').click(function() {
	toggleLoginOrCreateAccount();
	$(this).hide();
	$('#create-an-account').show();
});

$('#create-an-account').click(function() {
	toggleLoginOrCreateAccount();
	$(this).hide();
	$('#already-have-account').show();
});

$('.sound-byte').click(function() {
	var clipName = $(this).find('p').html();
	var clipType = clipName.substr(clipName.indexOf(".") + 1);
	// $("#playback-panel audio").html("<source src='../../data/uploads/" + clipName + "' type='audio/" + clipType + "'>");
});

var toggleLoginOrCreateAccount = function () {
	$('#login').toggle();
	$('.create-account').toggle();
}