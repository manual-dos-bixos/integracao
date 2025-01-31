
$(document).ready(function() {
    // TROCAR RADIO BUTTON POR BOTAO
    $('input.form-check').each(function() {
        let id = $(this).prop('id');

        $('#curso-btns').append(`<button class="btn btn-light btn-curso" id="btn-${id}">${$(`label[for="${id}"]`).text()}</button>`);
        $(this).parent().hide();
    })
});

$(document).on('click', '.btn-curso', function(e) {
    e.preventDefault();
    let id = $(this).prop('id').replace('btn-', '');
    let radio = $('#' + id);

    $('.btn-curso').removeClass('btn-curso-ativo');
    $(this).addClass('btn-curso-ativo');

    radio.prop('checked', true);
});

$(document).on('click', '#btn-next', function(e) {
    let sectionAtual = $('.section-atual');
    let nextSection = sectionAtual.next();

    sectionAtual.removeClass('section-atual').css('left', '-100%');
    nextSection.addClass('section-atual').css('left', '0');

    $('#btn-prev').removeClass('disabled');
    if (nextSection.is('.form-section:last-child')) $(this).addClass('disabled');
});

$(document).on('click', '#btn-prev', function(e) {
    let sectionAtual = $('.section-atual');
    let prevSection = sectionAtual.prev();

    sectionAtual.removeClass('section-atual').css('left', '100%');
    prevSection.addClass('section-atual').css('left', '0');

    $('#btn-next').removeClass('disabled');
    if (prevSection.is('.form-section:first-child')) $(this).addClass('disabled');
});

$(document).on('click', '.btn-inscricao', function(e) {
    e.preventDefault();

    let tipoAluno = $(this).data('tipo');
    console.log(tipoAluno);
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