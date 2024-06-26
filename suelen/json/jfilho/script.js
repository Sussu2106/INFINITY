const livro ={
    nome:'Orgulho & Preconceito'
    , escritora: 'Jane Austen'
    , ano:1813
}
console.log(JSON.stringify(livro))
console.log(JSON.parse(JSON.stringify(livro)))