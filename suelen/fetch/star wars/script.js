const botao = document.querySelector('button')

botao.addEventListener('click', () =>{
    const url = 'https://swapi.dev/api/'
    fetch(url)
    .then(resposta =>{
        return resposta.json()
    })
    .then(dados => {
        
    })
})