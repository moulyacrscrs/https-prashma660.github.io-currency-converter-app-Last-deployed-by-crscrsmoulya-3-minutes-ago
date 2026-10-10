async function convert() {
    let amount = document.getElementById("amount").value;
    let from = document.getElementById("from").value;
    let to = document.getElementById("to").value;

    let url = `https://api.exchangerate-api.com/v4/latest/${from}`;

    let response = await fetch(url);
    let data = await response.json();

    let rate = data.rates[to];
    let result = amount * rate;

    document.getElementById("result").innerText =
        `${amount} ${from} = ${result.toFixed(2)} ${to}`;
}