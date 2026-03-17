# ==================================================================
# FarmTech Solutions — Analise Estatistica dos Talhoes
# Fase 1, Letra G: Estatisticas basicas em R
# FIAP IA 2026 — Grupo 44 / Equipe 7
#
# Uso: Rscript r/analise_estatistica.R  (a partir da raiz do projeto)
# ==================================================================

# --- Leitura dos dados exportados pelo sistema Python ---
dados <- read.csv("data/talhoes.csv",
                   fileEncoding = "UTF-8",
                   stringsAsFactors = FALSE)

# Verifica se ha dados no arquivo
if (nrow(dados) == 0) {
  stop("Arquivo talhoes.csv vazio. Execute o sistema Python e cadastre talhoes primeiro.")
}

cat("\n")
cat("================================================================\n")
cat("       FARMTECH SOLUTIONS — ANALISE ESTATISTICA\n")
cat("================================================================\n")

# --- Exibe os dados carregados ---
cat("\n--- DADOS CARREGADOS ---\n\n")
print(dados)
cat(sprintf("\nTotal de talhoes: %d\n", nrow(dados)))
cat(sprintf("Culturas encontradas: %s\n",
            paste(unique(dados$Cultura), collapse = ", ")))

# --- Estatisticas gerais da area ---
cat("\n--- ESTATISTICAS GERAIS — AREA (ha) ---\n\n")
cat(sprintf("  N (talhoes):   %d\n",       nrow(dados)))
cat(sprintf("  Media:         %.4f ha\n",   mean(dados$Area)))
cat(sprintf("  Desvio padrao: %.4f ha\n",   sd(dados$Area)))
cat(sprintf("  Mediana:       %.4f ha\n",   median(dados$Area)))
cat(sprintf("  Minimo:        %.4f ha\n",   min(dados$Area)))
cat(sprintf("  Maximo:        %.4f ha\n",   max(dados$Area)))

# --- Estatisticas por cultura ---
cat("\n--- ESTATISTICAS POR CULTURA ---\n")

culturas <- unique(dados$Cultura)

for (cultura in culturas) {
  areas <- dados$Area[dados$Cultura == cultura]
  n <- length(areas)

  cat(sprintf("\n  [%s]\n", cultura))
  cat(sprintf("    N (talhoes):   %d\n",     n))
  cat(sprintf("    Media:         %.4f ha\n", mean(areas)))

  # Desvio padrao requer ao menos 2 observacoes
  if (n > 1) {
    cat(sprintf("    Desvio padrao: %.4f ha\n", sd(areas)))
  } else {
    cat("    Desvio padrao: N/A (apenas 1 observacao)\n")
  }

  cat(sprintf("    Minimo:        %.4f ha\n", min(areas)))
  cat(sprintf("    Maximo:        %.4f ha\n", max(areas)))
}

cat("\n================================================================\n")
cat("  Analise concluida.\n")
cat("================================================================\n\n")
