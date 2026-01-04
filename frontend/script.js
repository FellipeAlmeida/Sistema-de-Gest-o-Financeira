const btnNovaTransacao = document.querySelector('.button-header')
const modal = document.querySelector('.sectionModal')
const modalCategoria = document.querySelector('#categorias')
const btnfecharModal = document.querySelectorAll('.close-btn')
const btnCancelarModal = document.querySelectorAll('.cancel')

function abrirModal() {
    modal.style.display = 'flex'
}
btnNovaTransacao.addEventListener('click', abrirModal)

function fecharModal() {
    modal.style.display = 'none'
}

btnfecharModal.forEach(btn => {
    btn.addEventListener('click', fecharModal)
})

btnCancelarModal.forEach(btn => {
    btn.addEventListener('click', fecharModal)
})

/* ------------------------------------ */

// Botões
const btnReceita = document.getElementById("btn-receita");
const btnDespesa = document.getElementById("btn-despesa");
const categoriaSelect = document.getElementById("categoria-select");

// Listas
const categoriasGasto = ["Alimentação", "Transporte", "Saúde"];
const categoriasReceita = ["Salário", "Investimentos", "Freelance"];

// Receita
function colocaCategoriaReceita() {
    btnReceita.classList.add("active");
    btnDespesa.classList.remove("active");

// limpa e coloca categorias de receita
categoriaSelect.innerHTML = "";
for (let i = 0; i < categoriasReceita.length; i++) {
    const op = document.createElement("option");
    op.textContent = categoriasReceita[i];
    categoriaSelect.appendChild(op);
    }
};
btnReceita.addEventListener('click', colocaCategoriaReceita)

// Despesa
function colocaCategoriaDespesa() {
btnDespesa.classList.add("active");
btnReceita.classList.remove("active");

categoriaSelect.innerHTML = "";
for (let i = 0; i < categoriasGasto.length; i++) {
    const op = document.createElement("option");
    op.textContent = categoriasGasto[i];
    categoriaSelect.appendChild(op);
    }
};
btnDespesa.addEventListener('click', colocaCategoriaDespesa)

// ABAS
const tab1 = document.querySelector('[data-tab="transacao"]');
const tab2 = document.querySelector('[data-tab="categorias"]');

const content1 = document.getElementById("transacao");
const content2 = document.getElementById("categorias");

function fecharCategorias() {
    tab1.classList.add("active");
    tab2.classList.remove("active");

    content1.classList.add("active");
    content2.classList.remove("active");
};
tab1.addEventListener('click', fecharCategorias)

function abrirCategorias() {
    tab2.classList.add("active");
    tab1.classList.remove("active");

    content2.classList.add("active");
    content1.classList.remove("active");
};
tab2.addEventListener('click', abrirCategorias)

/* ------------------------------------ */
const chart = document.querySelector('.graficoDespesas').getContext('2d')
const chart2 = document.querySelector('.graficoDespesasvsReceitas').getContext('2d')

// grafico despesas por categoria
const data = {
    labels: ['Vermelho', 'Amarelo', 'Azul'],
    datasets: [{
        label: 'Meu conjunto de dados',
        data: [10,20,30],
        backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(255, 159, 64, 0.2)',
            'rgba(54, 162, 235, 0.2)'
        ],
        borderColor: [
            'rgb(255, 99, 132)',
            'rgb(255, 159, 64)',
            'rgb(54, 162, 235)'
        ],
        borderWidth: 1
    }]
}

const grafico = new Chart(chart, {
    type: 'pie',
    data: data
})

// grafico despesas vs receitas
const data2 = {
    labels: ['Vermelho', 'Amarelo', 'Azul'],
    datasets: [{
        label: 'Meu conjunto de dados',
        data: [10,20,30],
        backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(255, 159, 64, 0.2)',
            'rgba(54, 162, 235, 0.2)'
        ],
        borderColor: [
            'rgb(255, 99, 132)',
            'rgb(255, 159, 64)',
            'rgb(54, 162, 235)'
        ],
        borderWidth: 1
    }]
}

const grafico2 = new Chart(chart2, {
    type: 'bar',
    data: data
})

/* ---------------- INTEGRAÇÃO ---------------- */

const btnSalvarCategoria = document.querySelector('#salvar-categoria')

async function salvarCategoria(){
    const tipo = document.querySelector('#tipo_categoria_escolha').value
    const nome = document.querySelector('#nome_categoria').value
    const mensagem = document.querySelector('.tipo-gasto-added')

    let url = ""

    if (tipo === 'gasto'){
        url = 'http://localhost:8000/tipo_gasto'
    } else {
        url = 'http://localhost:8000/tipo_receita'
    }

    const body = {nome: nome}

    const response = await fetch(url, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(body)
    })

    const data = await response.json()
    console.log('Criado: ', data)
    mensagem.style.display = 'flex'

    setTimeout(() => {
        mensagem.style.display = 'none'
    }, 2000)
}
btnSalvarCategoria.addEventListener('click', salvarCategoria)