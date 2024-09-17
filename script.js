function salvarClienteNoLog(cliente) {
    fetch('https://roupasbrancasecia.herokuapp.com/log', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(cliente)
    }).then(response => {
        if (!response.ok) {
            console.error('Erro ao salvar cliente no log.');
        }
    }).catch(error => console.error('Erro ao salvar cliente no log:', error));
}
