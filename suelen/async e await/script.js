const url = "https://667c68333c30891b865c9009.mockapi.io/api/historia/historia";

async function carregarHistorias() {
    const resposta = await fetch(url)
    const dados = await resposta.json()
    colocarHTML(dados)
}

async function criarHistoria(){
    const inputDescricao = document.querySelector('#descricao')
    let descricaoDigitada = inputDescricao.value
    const historiaInformada = {
        "descricao" : descricaoDigitada, /*json aceita apenas "aspas duplas"*/
        "likes": 0
    }
    const resposta = await fetch(url,{
        method: 'POST',
        headers:{ 'Content-type': 'application/json'},
        body: JSON.stringify(historiaInformada)
    })
    alert('sua história foi criada com sucesso')
    carregarHistorias()
}

function colocarHTML(historias) {
    const tabelaHistorias = document.querySelector('#lista-historias')
    tabelaHistorias.innerHTML = ''

    historias.forEach(historia => {
        const tr = document.createElement('tr')
        tr.innerHTML = `<td>${historia.id}</td>
            <td>${historia.descricao}</td>
            <td>${historia.likes}</td>`

        tabelaHistorias.appendChild(tr)

    });
}

const formularioCadastrarHistoria = document.querySelector('#form-adicionar')
formularioCadastrarHistoria.addEventListener('submit', evento =>{
    evento.preventDefault()
    criarHistoria()

})

carregarHistorias()