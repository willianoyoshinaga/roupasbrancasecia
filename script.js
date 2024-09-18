function salvarClienteNoLog(cliente) {
    fetch('https://roupasbrancasecia.herokuapp.com/log', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(cliente)
    }).then(response => {
        if (!response.ok) {
            response.json().then(data => {
                console.error('Erro ao salvar cliente no log:', data.message);
            });
        } else {
            console.log('Cliente salvo no log com sucesso.');
        }
    }).catch(error => console.error('Erro ao salvar cliente no log:', error));
}
