const botao = document.querySelector('button')

const PrimeiroNome = document.querySelector('#name')
const sobrenome = document.querySelector('#sobrenome')
const pronome = document.querySelector('#pronome')


botao.addEventListener('click', () =>{
    const url = 'https://randomuser.me/api'
    fetch(url)
    .then(resposta =>{
        return resposta.json()
    })
    .then(dados => {
        let dadosNome = dados.results[0].name
        pronome.innerHTML = dadosNome.title
        PrimeiroNome.innerHTML = dadosNome.first
        sobrenome.innerHTML = dadosNome.last
    })
})