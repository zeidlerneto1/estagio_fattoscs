document.addEventListener('DOMContentLoaded', function() {
    var tarefasListaDetalhes = document.getElementById('tarefas-lista-detalhes');
    var salvarOrdemUrl = document.getElementById('salvar-ordem-url').getAttribute('data-url');
    var csrfToken = document.getElementById('csrf-token').getAttribute('data-csrf');

    if (tarefasListaDetalhes) {
        new Sortable(tarefasListaDetalhes, {
            animation: 150,
            onEnd: function(evt) {
                var order = [];
                var items = tarefasListaDetalhes.getElementsByTagName('tr');
                for (var i = 0; i < items.length; i++) {
                    order.push(items[i].getAttribute('data-id')); 
                }

                fetch(salvarOrdemUrl, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrfToken
                    },
                    body: JSON.stringify({ ordem: order })  
                })
                .then(response => response.json())
                .then(data => {
                    if (data.status === 'success') {
                        alert('Ordem salva com sucesso!' + "\nCarregue Novamente a Pagina para ver as alterações");
                    } else {
                        alert('Erro ao salvar a ordem:', data.message);
                    }
                })
                .catch(error => console.error('Erro:', error));
            }
        });
    }
});
