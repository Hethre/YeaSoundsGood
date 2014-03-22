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
	var clipName = $(this).data('name');
	var clipTitle = clipName.substr(0, clipName.indexOf("."));
	var clipType = $(this).data('type');
	var clipDesc = $(this).data('desc');
	var clipCreated = $(this).data("created");
	var $playerPanel = $("#playback-panel");

	var audio = "<audio id='" + clipTitle + "' controls autoplay>";
	audio += "<source src='/soundfile/" + clipName + "' type='audio/" + clipType + "'><br/>";
	audio += "<div class='clip-title'>" + clipName + " - ";
	audio += "<span class='clip-created'>" + clipCreated + "</span></div>";
	audio += "<div class='clip-desc'>" + clipDesc + "</div><hr></audio>";
	$playerPanel.append(audio);

	$("#" + clipTitle).bind('ended', function(){
	    $(this).remove();
	});
});

var toggleLoginOrCreateAccount = function () {
	$('#login').toggle();
	$('.create-account').toggle();
}