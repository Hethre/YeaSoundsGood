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
	var $player = $("#playback-panel");
	$player.find("audio").html("<source src='/soundfile/" + clipName + "' type='audio/" + clipType + "'>");
	$player.play();
});

var toggleLoginOrCreateAccount = function () {
	$('#login').toggle();
	$('.create-account').toggle();
}