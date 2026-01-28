import {verificaTipoTransacao} from './utils.js'

/* ---------------- INTEGRAÇÃO SALVAR CATEGORIAS ---------------- */

export async function salvarCategoria(){
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

/* ---------------- INTEGRAÇÃO SALVAR TRANSAÇÃO ---------------- */

export async function salvarTransacao(){
    const btnReceita = document.getElementById("btn-receita");
    const tipo = verificaTipoTransacao(btnReceita)
    const nome = document.querySelector('#nome_transacao').value
    const categoria = document.querySelector('#categoria-select').value
    const valor = document.querySelector('#valor').value
    const dataDaTransacao = document.querySelector('#data').value
    const eh_fixo = document.querySelector('#eh_fixo').checked
    const descricao = document.querySelector('#descricao').value
    const mensagem = document.querySelector('.tipo-gasto-added')

    let url = ""

    if (tipo === 'receita'){
        url = 'http://localhost:8000/receita'
    } else {
        url = 'http://localhost:8000/Gasto'
    }

    let body = {}

    if (tipo === 'receita'){
        body = {
            nome: nome,
            valor: valor,
            data: dataDaTransacao,
            eh_fixo: eh_fixo,
            descricao: descricao,
            tipo_receita_id: categoria
        }
    } else {
        body = {
            nome: nome,
            valor: valor,
            data: dataDaTransacao,
            eh_fixo: eh_fixo,
            descricao: descricao,
            tipo_gasto_id: categoria
        }
    }

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
    console.log(tipo)
}

/* -------------------------------- */


/* LIST TIPOS_GASTOS PARA MOSTRAR EM CATEGORIAS */
export async function buscarCategoriasReceitas(){
    const response = await fetch('http://localhost:8000/tipo_receita/list')
    return response.json()
}

export async function buscarCategoriasGastos(){
    const response = await fetch('http://localhost:8000/tipo_gasto/list')
    return response.json()
}

/* -------------------------------- */

export async function buscarGastoPorIdCat(categoria){
    const response = await fetch(`http://localhost:8000/Gasto/${categoria}`)
    return response.json()
}

/* --------------- LISTAR RECEITAS ----------------- */

export async function buscarReceitas(){
    const response = await fetch(`http://localhost:8000/receita/list`)
    return response.json()
}

/* --------------- LISTAR DESPESAS ----------------- */

export async function buscarGastos(){
    const response = await fetch(`http://localhost:8000/Gasto/list`)
    return response.json()
}

