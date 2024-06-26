let botao = document.querySelector('button')
let logradouro = document.querySelector('#logradouro')
let bairro = document.querySelector('#bairro')
let localidade = document.querySelector('#localidade')
let uf = document.querySelector('#uf')

botao.addEventListener('click', (event) =>{
    event.preventDefault()
    let cep = document.querySelector('#cep').value
    let url = `https://viacep.com.br/ws/${cep}/json/`
    fetch(url)
    .then(resposta =>{
        return resposta.json()
    })
    .then(dados => {
        logradouro.value = dados.logradouro
        bairro.value = dados.bairro
        localidade.value = dados.localidade
        uf.value = dados.uf
    })
})