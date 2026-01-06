/* ---------------- FUNÇÕES UTÉIS ---------------- */

// verifica tipo de transação
export function verificaTipoTransacao(btnReceita){
    return btnReceita.classList.contains('active')
        ? 'receita'
        : 'despesa'
}