
/**
 * Converts the bulk_expenses textarea content into seperated expense
 * entries.
 */
function convert() {
  var bulk_expenses = document.getElementById("bulk_expenses").value.trim();
  var who = document.getElementById("who").value.trim();
  var expenses_lines = bulk_expenses.split("\n");
  var split_container = document.getElementById("split_container");
  split_container.innerHTML = "";
  expenses_lines.forEach(expense_line => {
    var split_expense = expense_line.trim().split("|");
    var expense_div = genExpenseDiv(who, split_expense);
    split_container.appendChild(expense_div);
  });
}

function genExpenseDiv(who, expense_parts) {
  var div = document.createElement("div");
  var input = document.createElement("input");
  input.type = "text";
  input.name = "expense";
  input.id = "expense";
  input.value = who + "|" + expense_parts.join("|");
  div.appendChild(input);
  return div;
}