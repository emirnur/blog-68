function myCalc(d) {
    let myVar = d.getAttribute('data-id');
    console.log(myVar);
    a = document.getElementById('A').value;
    b = document.getElementById('B').value;

    $.ajax({
        url: "http://localhost:8000/" + myVar + '/',
        method: 'post',
        dataType: "json",
        contentType: "application/json",
        data: JSON.stringify({'A': a, 'B': b}),
        success: function(response) {
            const result = $('#result');
            const result_div = $('#result-div');
            result.text('Ответ: ' + response.answer);
            result_div.css('backgroundColor', 'green');
            },
        error: function(response) {
            const result = $('#result');
            const result_div = $('#result-div');
            result.text('Ответ: ' + response.responseJSON.mistake);
            result_div.css('backgroundColor', 'red');
            console.log(response)
        },
    });
}


