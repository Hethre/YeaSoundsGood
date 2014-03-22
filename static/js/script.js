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

$('.sound-byte i').click(function() {
	var clipName = $(this).parent().parent().find('p').html();
	var clipTitle = clipName.substr(0, clipName.indexOf("."));
	var clipType = $(this).data('type');
	var $playerPanel = $("#playback-panel");

	var audio = "<audio id='" + clipTitle + "' controls autoplay>";
	audio += "<source src='/soundfile/" + clipName + "' type='audio/" + clipType + "'>";
	audio += "</audio>";
	$playerPanel.append(audio);

	$("#" + clipTitle).bind('ended', function(){
	    $(this).remove();
	});
});

var toggleLoginOrCreateAccount = function () {
	$('#login').toggle();
	$('.create-account').toggle();
}