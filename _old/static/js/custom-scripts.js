$('.dropdown-trigger').dropdown();


$(".alert").delay(4000).fadeOut(300, function() {
    $(this).alert('close');
});


$(document).ready(function() {
    $('.sidenav').sidenav();

    $('select').formSelect();

    $('#selectArea').formSelect();

    $('.counter').counterUp({
        delay: 10,
        time: 400
    });
});



