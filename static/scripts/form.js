$(document).ready(function() {
    $('#btn-next, #btn-prev').hide();

    // TROCAR RADIO BUTTON POR BOTAO
    $('input.form-check').each(function() {
        let id = $(this).prop('id');

        $('#curso-btns').append(`<button class="btn btn-light btn-curso" id="btn-${id}">${$(`label[for="${id}"]`).text()}</button>`);
        $(this).parent().hide();
    });
});

$(document).on('click', '.btn-curso', function(e) {
    e.preventDefault();
    let id = $(this).prop('id').replace('btn-', '');
    let radio = $('#' + id);

    $('.btn-curso').removeClass('btn-curso-ativo');
    $(this).addClass('btn-curso-ativo');

    radio.prop('checked', true);
});

$(document).on('click', '#btn-prev, #btn-next', function(e) {
    let tipoAluno = $('.btn-inscricao.selected-btn').data('tipo');
    let numEtapas = tipoAluno == 'calouro' ? $('.form-section').length - 1 : $('.form-section').length;

    let sectionAtual = $('.section-atual');

    if ($(this).prop('id') == 'btn-next') {
        let nextSection = sectionAtual.next();

        sectionAtual.removeClass('section-atual').css('left', '-100%');
        nextSection.addClass('section-atual').css('left', '0');

        $('#btn-prev').removeClass('disabled');
        if ($('.form-section.section-atual').index() == numEtapas - 1) $(this).addClass('disabled');
    } else {
        let prevSection = sectionAtual.prev();
        sectionAtual.removeClass('section-atual').css('left', '100%');
        prevSection.addClass('section-atual').css('left', '0');

        $('#btn-next').removeClass('disabled');
        if (prevSection.is('.form-section:first-child')) $(this).addClass('disabled');
    }

    let etapaAtual = $('.section-atual').index();
    $('#form-progress-bar .progress').css({'width': (etapaAtual / (numEtapas - 1) * $('#form-progress-bar').width()) + 'px'});
    $('.step-icon').slice(0, etapaAtual + 1).css({'background-color': '#641290', 'color': '#fff'})
    $('.step-icon').slice(etapaAtual + 1).css({'background-color': '#fff', 'color': '#641290'})
});

$(document).on('click', '.btn-inscricao', function(e) {
    e.preventDefault();
    $('.btn-inscricao').removeClass('selected-btn');
    $(this).addClass('selected-btn');

    let tipoAluno = $(this).data('tipo');
    let numEtapas = tipoAluno == 'calouro' ? $('.form-section').length - 1 : $('.form-section').length;

    if ($('#form-progress-bar').css('opacity') == 1) {
        $('#form-progress-bar .step-icon').animate({opacity: 0}, 100);
        setTimeout(() => {
            $('#form-progress-bar .step-icon').remove();
            
            for (let i = 0; i < numEtapas; i++) $('#form-progress-bar').append(`<span class="step-icon">${i + 1}</i>`);
            $('#form-progress-bar .step-icon').css({'opacity': 0});
            $('#form-progress-bar .step-icon').animate({opacity: 1}, 100);
            $('.step-icon').first().css({'background-color': '#641290', 'color': '#fff'});
        }, 100);
    } else {
        for (let i = 0; i < numEtapas; i++) $('#form-progress-bar').append(`<span class="step-icon">${i + 1}</i>`);
        $('#form-progress-bar .step-icon').css({'opacity': 0});
        $('#form-progress-bar').animate({opacity: 1}, 100);
        $('#form-progress-bar .step-icon').animate({opacity: 1}, 100);
        $('.step-icon').first().css({'background-color': '#641290', 'color': '#fff'})
    }

    if ($('#btn-next').is(':hidden')) setTimeout(() => $('#btn-next').click(), 600);
    $('#btn-next, #btn-prev').prop('hidden', false);
    $('#btn-next, #btn-prev').fadeIn(100);

});

// FORMATAR TELEFONE
// Aplica a formatação conforme a quantidade de caracteres
$(document).on('input', '.telefone-input', function() {
    var value = $(this).val().replace(/\D/g, '');
        
    if (value.length <= 2) {
        $(this).val(`(${value}`);
    } else if (value.length <= 6) {
        $(this).val(`(${value.slice(0, 2)}) ${value.slice(2, 3)} ${value.slice(3, 7)}`);
    } else {
        $(this).val(`(${value.slice(0, 2)}) ${value.slice(2, 3)} ${value.slice(3, 7)}-${value.slice(7, 11)}`);
    }
});

// Permite apagar os caracteres nao numericos
$(document).on('keydown', '.telefone-input', function() {
    var value = $(this).val().replace(/\D/g, '');

    $(this).val(value);
});