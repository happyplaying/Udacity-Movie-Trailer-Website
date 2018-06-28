// Pause the video when the modal is closed
$(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
    // Remove the src so the player itself gets removed, as this is the only
    // reliable way to ensure the video stops playing in IE
    $(".youtube-wrapper").empty();
});
// Start playing the video whenever the trailer modal is opened
$(document).on('click', '.movie-modal', function (event) {
    var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
    var modalId = $(this).attr('data-modal-id')
    var sourceUrl = 'https://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
    $("#trailer-video-container-" + modalId).empty().append($("<iframe></iframe>", {
        'class': 'video',
        'type': 'text-html',
        'src': sourceUrl,
        'frameborder': 0
    }));
});
// back to top
$(document).ready(function() {
    $(window).scroll(function() {
        if ($(this).scrollTop() > 50) {
            $("#back-to-top").fadeIn();
        } else {
            $("#back-to-top").fadeOut();
        }
    });
    // scroll body to 0px on click
    $("#back-to-top").click(function() {
        $("#back-to-top").tooltip("hide");
        $("body,html").animate(
            {
                scrollTop: 0
            },
            800
        );
        return false;
    });
});