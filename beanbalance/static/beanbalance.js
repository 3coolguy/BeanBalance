function createTable() {
    var tbody = document.getElementById('table-body');

    // Create 5 rows
    for (var i = 1; i < 6; i++) {
        var row = document.createElement('tr');
        var idCell = document.createElement('td');
        idCell.textContent = 'Coworker ' + i; // Display the ID

        var textFieldCell = document.createElement('td');
        var textField = document.createElement('input');
        textField.type = 'decimal';
        textField.id = 'text' + i; // Text field with unique ID
        textField.name = 'text' + i;

        textFieldCell.appendChild(textField);
        row.appendChild(idCell);
        row.appendChild(textFieldCell);
        tbody.appendChild(row);
    }
};

function decidePayment(){

    return
};