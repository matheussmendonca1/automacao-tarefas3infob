const btnEnviar = document.getElementById('salvar');
let nome = document.getElementById('idnome');
let nota = document.getElementById('idnota');
let id = 0;
let table = document.getElementById('tabela-notas');


const infoAlunos = {
    id: [],
    nome: [],
    nota: []
};

btnEnviar.addEventListener('click', (event) => {
    event.preventDefault();
    addAluno(id, nome.value, nota.value);
    criarElemento();
    limpaCampos();
    console.log(infoAlunos);
    id++;
});

function addAluno(id, nome, nota) {
    infoAlunos.id.push(id);
    infoAlunos.nome.push(nome);
    infoAlunos.nota.push(nota);
}

function criarElemento() {

    const tr = document.createElement("tr");
    const tdNome = document.createElement("td");
    const tdNota = document.createElement("td");

    let textoNome = (infoAlunos.nome[id]);
    let textoNota = (infoAlunos.nota[id]);


    tdNome.textContent = textoNome;
    tdNota.textContent = textoNota;

    table.appendChild(tr);
    tr.appendChild(tdNome);
    tr.appendChild(tdNota);

    if(infoAlunos.id[id] % 2 == 0) {
        tr.className = "linha";
    }
}

function limpaCampos() {
    nome.value = '';
    nota.value = '';
}

