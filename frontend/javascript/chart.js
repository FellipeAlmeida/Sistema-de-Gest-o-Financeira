import { buscarCategoriasGastos, buscarGastoPorIdCat } from "./integracao.js";
import { gerarCor } from "./utils.js";

let graficoDespesas = null;
let graficoReceitas = null;

export async function iniciarGraficos() {
  /* --------- DESPESAS POR CATEGORIA --------- */

  const categorias = await buscarCategoriasGastos();

  const valores = await Promise.all(
      // para cada categoria ele busca um gasto com base no id da categoria e soma
    categorias.map(async (cat) => {
      const gastos = await buscarGastoPorIdCat(cat.id);

      // soma apenas os gastos das categorias correspondentes
      const totalCategoria = gastos.reduce((total, gasto) => {
        if (gasto.tipo_gasto_id === cat.id) { // verifica se o tipo_gasto_id do objeto gasto é igual ao id da categoria
          return total + Number(gasto.valor || 0);
        }
        return total;
      }, 0);

      return totalCategoria;
    })
  );

  // atributos do gráfico
  const labels = categorias.map(cat => cat.nome);
  const cores = valores.map(() => gerarCor());
  const backgroundColor = cores.map(c => c.bg);
  const borderColor = cores.map(c => c.border);

  const canvasDespesas = document.querySelector(".graficoDespesas").getContext('2d')

  if (graficoDespesas) { // se ja existir, so atualiza, se não, cria
    graficoDespesas.data.labels = labels;
    graficoDespesas.data.datasets[0].data = valores;
    graficoDespesas.update();
  } else {
    graficoDespesas = new Chart(canvasDespesas, {
      type: "pie",
      data: {
        labels,
        datasets: [{
          label: "Despesas por categoria",
          data: valores,
          backgroundColor,
          borderColor,
          borderWidth: 1
        }]
      }
    });
  }

  /* --------- RECEITAS VS DESPESAS --------- */

  const canvasResumo = document.querySelector(".graficoDespesasvsReceitas");
  if (!canvasResumo) return;

  const ctxResumo = canvasResumo.getContext("2d");

  const totalDespesas = valores.reduce((a, b) => a + b, 0);

  if (graficoReceitas) {
    graficoReceitas.data.datasets[0].data = [3000, totalDespesas];
    graficoReceitas.update();
  } else {
    graficoReceitas = new Chart(ctxResumo, {
      type: "bar",
      data: {
        labels: ["Receitas", "Despesas"],
        datasets: [{
          label: "Resumo financeiro",
          data: [3000, totalDespesas]
        }]
      }
    });
  }
}
