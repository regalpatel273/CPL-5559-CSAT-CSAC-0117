$(document).ready(function(){
    $('.form-label').each(function(){
        $(this).next().next().addClass('form-control')
        let temp = $(this).html().toLowerCase()
        $(this).next().next().attr('placeholder','Enter ' + temp)
    });
    $('#id_phone_number_0').addClass('form-control');
    $('#id_phone_number_1').addClass('form-control mt-3');
    $('#id_phone_number_1').attr('placeholder','Enter phone number');
});