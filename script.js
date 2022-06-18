/*
Ao clicar no botão X, vai fazer um fetch() para o backend (http://127.0.0.1:5000/todos)
vai fazer um loop (iterar sobre os dados retornados) e vai criar um
elemento <td> pra cada dado retornado
*/
const tabela = document.querySelector('#tabela-alunos');


fetch('http://127.0.0.1:5000/todos')
.then(function(resposta) {
    return resposta.json()
})
.then(function(listaAlunos) {
    const tamanhoLista = ListaAlunos.lenght;

 for(let index = 0; index ,tamanhoLista;index++) {
    const linha = document.createElement('tr');

    const id = document.createElement('td');
    const aluno = document.createElement('td');
    const etnia = document.createElement('td');
    const idade = document.createElement('td');
    const aprovados = document.createElement('td');
    const concluiram =document.createElement('td');
    const sexo = document.createElement('td');
    const familiares = document.createElement('td');
    const filhos = document.createElement('td');

    id.innerHTML = listaAlunos[index][0];
    aluno.innerHTML = listaAlunos[index][1];
    etnia.innerHTML = listaAlunos[index][2];
    idade.innerHTML = listaAlunos[index][3];
    aprovados.innerHTML = listaAlunos[index][4];
    concluiram.innerHTML = listaAlunos[index][5];
    sexo.innerHTML = listaAlunos[index][6];
    familiares.innerHTML = listaAlunos[index][7];
    filhos.innerHTML = listaAlunos[index][8];

    linha.appendChild(id);
    linha.appendChild(aluno);
    linha.appendChild(etnia);
    linha.appendChild(idade);
    linha.appendChild(aprovados);
    linha.appendChild(concluiram);
    linha.appendChild(sexo);
    linha.appendChild(familiares);
    linha.appendChild(filhos);
 }
})
