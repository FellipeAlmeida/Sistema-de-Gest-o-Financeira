import {
    buscarCategoriasGastos,
    buscarCategoriasReceitas,
    salvarCategoria,
    salvarTransacao
} from './integracao.js'

import {data, data2} from "./chart.js";

/* ---------------- LÓGICA PRA ABRIR E FECHAR MODAL -------------------- */

const btnNovaTransacao = document.querySelector('.button-header')
const modal = document.querySelector('.sectionModal')
const btnfecharModal = document.querySelectorAll('.close-btn')
const btnCancelarModal = document.querySelectorAll('.cancel')

function abrirModal() {
    modal.style.display = 'flex'
}
btnNovaTransacao.addEventListener('click', abrirModal)

function fecharModal() {
    modal.style.display = 'none'
}

/* ------------------------------------ */

btnfecharModal.forEach(btn => {
    btn.addEventListener('click', fecharModal)
})

// forEachs pra pegar cada botão "x" e "cancelar" e aplicar a mesma função

btnCancelarModal.forEach(btn => {
    btn.addEventListener('click', fecharModal)
})

/* ------------------------------------ */

const btnReceita = document.getElementById("btn-receita");
const btnDespesa = document.getElementById("btn-despesa");
const categoriaSelect = document.getElementById("categoria-select");

// preenche o select com as categorias fornecidas
function preencherSelectCat(categorias){
    categoriaSelect.innerHTML = "";

    categorias.forEach(cat => {
        const option = document.createElement('option')
        option.value = cat.id
        option.textContent = cat.nome
        categoriaSelect.appendChild(option)
    })
}

/* ------------------ CHAMA A ROTA LIST E PREENCHE AS CATEGORIAS ------------------ */

// Receita
async function colocaCategoriaReceita() {
    btnReceita.classList.add("active");
    btnDespesa.classList.remove("active");

// limpa e coloca categorias de receita com as que estão no banco de dados
    categoriaSelect.innerHTML = "";
    const categorias = await buscarCategoriasReceitas()
    preencherSelectCat(categorias)
};
btnReceita.addEventListener('click', colocaCategoriaReceita)

// Despesa
async function colocaCategoriaDespesa() {
    btnDespesa.classList.add("active");
    btnReceita.classList.remove("active");

    categoriaSelect.innerHTML = "";
    const categorias = await buscarCategoriasGastos()
    preencherSelectCat(categorias)
};
btnDespesa.addEventListener('click', colocaCategoriaDespesa)

/* ------------------------------------ */

/* ------------------ LÓGICA PARA A TROCA DE ABAS "TRANSAÇÃO" E "CATEGORIAS" DO MODAL ------------------ */

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

/* ---------------- INTEGRAÇÃO SALVAR CATEGORIAS ---------------- */

const btnSalvarCategoria = document.querySelector('#salvar-categoria')
btnSalvarCategoria.addEventListener('click', salvarCategoria)


const btnSalvarTransacao = document.querySelector('#add-transacao')
btnSalvarTransacao.addEventListener('click', salvarTransacao)

/* ---------------- MOSTRA GRAFICOS ---------------- */

const chart = document.querySelector('.graficoDespesas').getContext('2d')
const chart2 = document.querySelector('.graficoDespesasvsReceitas').getContext('2d')

const grafico = new Chart(chart, {
    type: 'pie',
    data: data
})

const grafico2 = new Chart(chart2, {
    type: 'bar',
    data: data2
})