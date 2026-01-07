import { buscarCategoriasGastos, buscarGastoPorIdCat } from "./integracao.js";
import { gerarCor } from "./utils.js";

let graficoDespesas = null;
let graficoReceitas = null;

export async function iniciarGraficos() {
  /* --------- DESPESAS POR CATEGORIA --------- */

  const categorias = await buscarCategoriasGastos();

  const valores = await Promise.all(
    categorias.map(async cat => {
      const gasto = await buscarGastoPorIdCat(cat.id);

      // garantia de número
        if (gasto && typeof gasto.valor === "number"){
            return gasto.valor
        } else {
            return 0
        }
    })
  );

  const labels = categorias.map(cat => cat.nome);

  const cores = valores.map(() => gerarCor());

  const backgroundColor = cores.map(c => c.bg);
  const borderColor = cores.map(c => c.border);

  const ctxDespesas = document.querySelector(".graficoDespesas").getContext("2d");

  if (graficoDespesas) {
    graficoDespesas.data.labels = labels;
    graficoDespesas.data.datasets[0].data = valores;
    graficoDespesas.update();
  } else {
    graficoDespesas = new Chart(ctxDespesas, {
      type: "pie",
      data: {
        labels,
        datasets: [
          {
            label: "Despesas por categoria",
            data: valores,
            backgroundColor,
            borderColor,
            borderWidth: 1
          }
        ]
      }
    });
  }

  /* --------- RECEITAS VS DESPESAS (EXEMPLO) --------- */

  const ctxResumo = document.querySelector(".graficoDespesasvsReceitas").getContext("2d");

  if (!graficoReceitas) {
    graficoReceitas = new Chart(ctxResumo, {
      type: "bar",
      data: {
        labels: ["Receitas", "Despesas"],
        datasets: [
          {
            label: "Resumo financeiro",
            data: [3000, valores.reduce((a, b) => a + b, 0)]
          }
        ]
      }
    });
  }
}
