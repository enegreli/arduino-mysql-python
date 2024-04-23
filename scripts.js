function carregarDados(){
    fetch('http://localhost:3000/dados-climaticos')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('dadosClimaticos');
            container.innerHTML = '';
            data.forEach(dado => {
                const card = document.createElement('div');
                card.className = 'card';
                card.innerHTML = `
                <div class="container">
                    <h4><b>Data/Hora: ${dado.data_hora}</b></h4>
                    <p>Temperatura: ${dado.temperatura} °C</p>
                    <p>Umidade: ${dado.umidade} %</p>
                </div>    
                `;
                container.appendChild(card);
            });
        })
        .catch(error => console.error('Erro ao buscar dados:', error));
}

document.addEventListener('DOMContentLoaded',carregarDados);