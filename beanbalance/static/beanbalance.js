function createTable() {
    var tbody = document.getElementById('table-body');

    // Create 5 rows
    for (var i = 1; i < 6; i++) {
        var row = document.createElement('tr');
        var idCell = document.createElement('td');
        idCell.textContent = 'Coworker ' + i; // Display the ID

        var balanceCell = document.createElement('td');
        balanceCell.textContent = 'balance'

        var textFieldCell = document.createElement('td');
        var textField = document.createElement('input');
        textField.type = 'decimal';
        textField.id = 'text' + i; // Text field with unique ID
        textField.name = 'text' + i;

        textFieldCell.appendChild(textField);
        row.appendChild(idCell);
        row.appendChild(balanceCell)
        row.appendChild(textFieldCell);
        tbody.appendChild(row);
    }
};

function validateForm() {
    var bobInput = document.getElementById('textBob').value;
    var jeremyInput = document.getElementById('textJeremy').value;
    var c1Input= document.getElementById('text1').value;
    var c2Input= document.getElementById('text2').value;
    var c3Input= document.getElementById('text3').value;
    var c4Input= document.getElementById('text4').value;
    var c5Input= document.getElementById('text5').value;

    if (!isValidDecimal(bobInput) || !isValidDecimal(jeremyInput) || !isValidDecimal(c1Input)
        || !isValidDecimal(c2Input) || !isValidDecimal(c3Input) || !isValidDecimal(c4Input)
        || !isValidDecimal(c5Input)) {
        alert('Please enter valid decimal values.');
        return false;  // Prevent form submission
    }
    return true;  // Allow form submission
};

function isValidDecimal(input) {
    // Regular expression to match a decimal number
    var decimalPattern = /^\d+(\.\d+)?$/;
    return decimalPattern.test(input);
};