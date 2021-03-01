$(document).ready(function() {
    $('.modal').modal();
    $('.parallax').parallax();

    $(".dropdown-trigger").dropdown({ hover: false });
    $(".slider").slider({ full_width: true })
    $('.parallax').parallax();


})

function toggleModal() {
    var instance = M.Modal.getInstance($('#modal3'));
    instance.open();
}


$(document).ready(function() {
    $('.fixed-action-btn').floatingActionButton();
});


$('.carousel.carousel-slider').carousel({
    fullWidth: true
});