$(document).ready(function() {
    $('#form-email').animate({height: 'toggle'}, 200);
});

$(document).on('click', '#btn-calouro', function() {
    // $('#main').animate({opacity: 'toggle'}, 200);
    // $('#form-email').animate({opacity: 'toggle'}, 200);

    $('#form-email').animate({height: 'toggle'}, 200);
});

$(document).on('click', '#btn-enviar', function() {
    hasFilledForm($('#email').val());
});

function hasFilledForm(email) {
    const url = 'https://docs.google.com/spreadsheets/d/14HkIJpVn2TV9gcAjpiXDE0uu0kEBzevZn2L1ErgsKFY/export?format=csv&id=14HkIJpVn2TV9gcAjpiXDE0uu0kEBzevZn2L1ErgsKFY&gid=934437593';
    
    fetch(url)
    .then(data => data.text())
    .then(data => {
        let calouros = csvToJson(data);
        
        calouros.forEach(calouro => {
            if (calouro.email == email) console.log(1);
            else console.log(0);
        })
    })
    .catch(error => function() {
        console.error(error);
    });
}

function csvToJson(csv) {
    const lines = csv.split('\n');

    const headers = lines[0].split(',');

    const resultado = lines.slice(1).map(line => {
        const columns = line.split(',')
        const obj = {};

        headers.forEach((header, index) => {
            header = header.replace('\r', '');
            obj[header] = columns[index].replace(/&#44;/g, ",");
        });
        return obj;
    });

    return resultado;
}