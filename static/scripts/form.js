$(document).ready(function() {
    $('#btn-next, #btn-prev').hide();
    $('.step-icon').first().css({'background-color': '#641290', 'color': '#fff'})

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
    let numEtapas = $('.form-section').length;
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

$(document).on('click', '.btn-tipo-aluno-inscricao', function(e) {
    e.preventDefault();
    $('.btn-tipo-aluno-inscricao').removeClass('selected-btn');
    $(this).addClass('selected-btn');

    if ($('#btn-next').is(':hidden')) setTimeout(() => $('#btn-next').click(), 600);
    $('#btn-next, #btn-prev').prop('hidden', false);
    $('#btn-next, #btn-prev').fadeIn(100);

    if ($(this).data('tipo') == 'calouro') {
        $('#semestre_atual').parent().hide();
        $('#semestre_atual').val('1');
    } else {
        $('#semestre_atual').parent().show();
        $('#semestre_atual').val('');
    }
});

// FORMATAR TELEFONE
// Aplica a formatação conforme a quantidade de caracteres
$(document).on('input', '.telefone-input', function() {
    var value = $(this).val().replace(/\D/g, '');
        
    if (value.length <= 2) {
        $(this).val(`(${value}`);
    } else if (value.length <= 6) {
        $(this).val(`(${value.slice(0, 2)}) ${value.slice(2, 6)}`);
    } else if (value.length <= 10) {
        $(this).val(`(${value.slice(0, 2)}) ${value.slice(2, 6)}-${value.slice(6, 12)}`);
    } else {
        $(this).val(`(${value.slice(0, 2)}) ${value.slice(2, 3)} ${value.slice(3, 7)}-${value.slice(7, 11)}`);
    }
});

// Permite apagar os caracteres nao numericos
$(document).on('keydown', '.telefone-input', function(e) {
    var value = $(this).val().replace(/\D/g, '');

    if (e.keyCode === 8) $(this).val(value);
});

$(document).on('click', '.interesse', function(e) {
    $(this).toggleClass('interesse-selecionado');
});

$(document).on('keydown', '#novo-interesse', function(e) {
    if (e.key === 'Enter') {        
        $('#lista-temas-novos').append(`<span class="interesse-adicionado">${$(this).val()}<i class="bi bi-x-lg ms-2"></i></span>`);
        $(this).val('');
        $(this).focus();
    }
});

$(document).on('click', '.interesse-adicionado .bi-x-lg', function(e) {
    $(this).parent().remove();
});
