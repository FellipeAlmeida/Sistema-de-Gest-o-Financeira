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

