document.getElementById('calc').addEventListener('click', updater);

function updater () {
    var cost = 25;
    var quantity = document.getElementById('quantity').value;
    var totalcost = (cost * quantity);

    document.getElementById('total').innerText = totalcost;
}
