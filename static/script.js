document.addEventListener('DOMContentLoaded', function(){
    var input_lang = document.getElementById('input_lang');
    input_lang.onkeyup = function(){
        updateCreateButtonVisability();
    };

    var input_sex = document.getElementById('input_sex');
    input_sex.onkeyup = function(){
        updateCreateButtonVisability();
    };

    var input_text = document.getElementById('input_text');
    input_text.onkeyup = function(){
        updateCreateButtonVisability();
    };
    input_text.onkeydown = function(event){
        if(event.key == 'Enter' && isCreatingAllowed()){
            createCompliment();
        }
    };

    var input_submit = document.getElementById('input_submit');
    input_submit.onclick = function(){
        createCompliment();
    };

    updateDeleteButtonsListeners();
    updateCreateButtonVisability();
});

function updateDeleteButtonsListeners(){
    var input_delete = document.getElementsByClassName('compliment_delete');
    for(var i = 0; i < input_delete.length; i ++){
        (function(){
            var compliment_id = input_delete[i].id;
            input_delete[i].onclick = function(){
                deleteCompliment(compliment_id);
            };
        })();
    }
}

function isCreatingAllowed(){
    var input_lang = document.getElementById('input_lang');
    var input_sex = document.getElementById('input_sex');
    var input_text = document.getElementById('input_text');

    return input_lang.value.length > 0 && input_sex.value.length > 0 && input_text.value.length > 0;
}

function updateCreateButtonVisability(){
    var input_submit = document.getElementById('input_submit');
    input_submit.style = isCreatingAllowed() ? '' : 'display:none';
}

function createCompliment(){
    var input_lang = document.getElementById('input_lang');
    var input_sex = document.getElementById('input_sex');
    var input_text = document.getElementById('input_text');

    performRequest('POST', '/compliment', 'lang=' + input_lang.value + '&sex=' + input_sex.value + '&text=' + input_text.value, function(response){
        var table = document.getElementById('compliments_table');
        var row = table.insertRow(-1);
        row.id = response['id'];
        row.insertCell(-1).innerHTML = response['lang'];
        row.insertCell(-1).innerHTML = response['sex'];
        row.insertCell(-1).innerHTML = response['text'];
        row.insertCell(-1).innerHTML = '<input id="' + response['id'] + '" class="compliment_edit" type="submit" value="Edit">';
        row.insertCell(-1).innerHTML = '<input id="' + response['id'] + '" class="compliment_delete" type="submit" value="Delete">';

        updateDeleteButtonsListeners();
    });

    input_text.value = '';
    input_text.focus();
}

function deleteCompliment(compliment_id){
    performRequest('DELETE', '/compliment/' + compliment_id, undefined, function(){
        var table = document.getElementById('compliments_table');
        var rows = table.rows;
        for(var i = 0; i < rows.length; i ++){
            if(rows[i].id == compliment_id){
                table.deleteRow(i);
                break;
            }
        }
    });
}

function performRequest(method, path, params, callback){
    var request = new XMLHttpRequest();
    request.open(method, path, true);
    if(params){
        request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        request.setRequestHeader("Content-length", params.length);
    }
    request.setRequestHeader("Connection", "close");
    request.onreadystatechange = function(){
        if(callback && request.readyState == 4 && request.status == 200){
            var response = request.responseText.length > 0 ? JSON.parse(request.responseText) : undefined;
            callback(response);
        }
    }
    request.send(params);
}
