import { buscarReceitas, buscarGastos } from './integracao.js'

/* ---------------- FUNÇÕES UTÉIS ---------------- */

// verifica tipo de transação
export function verificaTipoTransacao(btnReceita){
    if (btnReceita.classList.contains('active')){
        return 'receita'
    } else {
        return 'despesa'
    }
}

export function nomeCategorias(categorias){
    categorias.forEach(cat => {
        return cat.nome
    })
}

/* ---------------- CHART.JS ---------------- */

export function gerarCor() {
  const r = Math.floor(Math.random() * 255)
  const g = Math.floor(Math.random() * 255)
  const b = Math.floor(Math.random() * 255)

  return {
    bg: `rgba(${r}, ${g}, ${b}, 0.5)`,
    border: `rgb(${r}, ${g}, ${b})`
  }
}

/* ---------------- PEGA VALOR DE RECEITAS E SOMA ---------------- */

export async function pegaValorReceitasESoma(){
    let receitas = await buscarReceitas()
    let receitaValor = 0

    for (let receita of receitas){
        receitaValor += receita.valor
    }

    return receitaValor
}

/* ---------------- PEGA VALOR DE GASTOS E SOMA ---------------- */

export async function pegaValorDespesasESoma(){
    let gastos = await buscarGastos()
    let gastoValor = 0

    for (let gasto of gastos){
        gastoValor += gasto.valor
    }

    return gastoValor
}

/* ---------------- PEGA VALOR DE GASTOS E RECEITAS E PEGA A DIFERENÇA ---------------- */

export async function pegaDiferencaDespesaEReceitas(){
    let diferenca = await pegaValorReceitasESoma() - await pegaValorDespesasESoma()
    return diferenca
}