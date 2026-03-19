# ===============================
# Coleta de dados de API clima
# ===============================

library(httr)
library(jsonlite)

latitude <- "-23.6000"
longitude <- "-46.7203"

# Montar URL da API
url <- paste0(
  "https://api.open-meteo.com/v1/forecast?",
  "latitude=", latitude,
  "&longitude=", longitude,
  "&current_weather=true",
  "&hourly=temperature_2m,relative_humidity_2m,precipitation,windspeed_10m,winddirection_10m,pressure_msl,cloudcover,visibility",
  "&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,sunrise,sunset"
)

# Consultar API
resposta <- GET(url)

# Transformar resposta em texto
conteudo <- content(resposta, "text", encoding = "UTF-8")

# Ler JSON
json <- fromJSON(conteudo)

# ===============================
# DATA FRAMES
# ===============================

# Clima atual
df_atual <- data.frame(
  temperatura = json$current_weather$temperature,
  vento = json$current_weather$windspeed,
  dirvento = json$current_weather$winddirection,
  tipclim = json$current_weather$weathercode,
  dianoi = json$current_weather$is_day,
  horario = json$current_weather$time,
  latitude = json$latitude,
  longitude = json$longitude,
  timezone = json$timezone,
  elevacao = json$elevation,
  stringsAsFactors = FALSE
)

# Previsão por hora
df_horario <- data.frame(
  horario = json$hourly$time,
  temperatura = json$hourly$temperature_2m,
  umidade = json$hourly$relative_humidity_2m,
  precipitacao = json$hourly$precipitation,
  vento = json$hourly$windspeed_10m,
  dirvento = json$hourly$winddirection_10m,
  pressao = json$hourly$pressure_msl,
  nuvens = json$hourly$cloudcover,
  visibilidade = json$hourly$visibility,
  stringsAsFactors = FALSE
)

# Previsão diária
df_diario <- data.frame(
  data = json$daily$time,
  temp_max = json$daily$temperature_2m_max,
  temp_min = json$daily$temperature_2m_min,
  precipitacao_total = json$daily$precipitation_sum,
  nascer_sol = json$daily$sunrise,
  por_sol = json$daily$sunset,
  stringsAsFactors = FALSE
)

# ===============================
# VARIÁVEIS SIMPLES
# ===============================

temperatura <- json$current_weather$temperature
vento <- json$current_weather$windspeed
dirvento <- json$current_weather$winddirection
tipclim <- json$current_weather$weathercode
dianoi <- json$current_weather$is_day
horario <- json$current_weather$time

latitude <- json$latitude
longitude <- json$longitude
timezone <- json$timezone
elevacao <- json$elevation
geracaotempo <- json$generationtime_ms
fuso <- json$utc_offset_seconds

temp_hora <- json$hourly$temperature_2m
umidade <- json$hourly$relative_humidity_2m
chuva <- json$hourly$precipitation
vento10m <- json$hourly$windspeed_10m
dirvento10m <- json$hourly$winddirection_10m
pressao <- json$hourly$pressure_msl
nuvens <- json$hourly$cloudcover
visibilidade <- json$hourly$visibility
hora <- json$hourly$time

cat("\n==============================\n")
cat("     🌤️ CLIMA ATUAL\n")
cat("==============================\n")

cat(sprintf("%-30s: %s °C\n", "Temperatura", temperatura))
cat(sprintf("%-30s: %s km/h\n", "Velocidade do vento", vento))
cat(sprintf("%-30s: %s°\n", "Direção do vento", dirvento))
cat(sprintf("%-30s: %s\n", "Código do clima", tipclim))
cat(sprintf("%-30s: %s (%s)\n", "Período", dianoi, ifelse(dianoi == 1, "Dia", "Noite")))
cat(sprintf("%-30s: %s\n", "Horário da medição", horario))

cat("\n==============================\n")
cat("     📍 LOCALIZAÇÃO\n")
cat("==============================\n")

cat(sprintf("%-30s: %s\n", "Latitude", latitude))
cat(sprintf("%-30s: %s\n", "Longitude", longitude))
cat(sprintf("%-30s: %s\n", "Timezone", timezone))
cat(sprintf("%-30s: %s m\n", "Elevação", elevacao))

cat("\n==============================\n")
cat("     ⏱️ INFORMAÇÕES TÉCNICAS\n")
cat("==============================\n")

cat(sprintf("%-30s: %s ms\n", "Tempo de geração", geracaotempo))
cat(sprintf("%-30s: %s s\n", "Fuso UTC", fuso))

cat("\n==============================\n")
cat("     📊 DADOS HORÁRIOS (PRIMEIROS)\n")
cat("==============================\n")

for (i in 1:5) {
  cat(sprintf("\n[%s]\n", hora[i]))
  cat(sprintf("  %-25s: %s °C\n", "Temperatura", temp_hora[i]))
  cat(sprintf("  %-25s: %s %%\n", "Umidade", umidade[i]))
  cat(sprintf("  %-25s: %s mm\n", "Precipitação", chuva[i]))
  cat(sprintf("  %-25s: %s km/h\n", "Vento", vento10m[i]))
  cat(sprintf("  %-25s: %s°\n", "Direção do vento", dirvento10m[i]))
  cat(sprintf("  %-25s: %s hPa\n", "Pressão", pressao[i]))
  cat(sprintf("  %-25s: %s %%\n", "Nuvens", nuvens[i]))
  cat(sprintf("  %-25s: %s m\n", "Visibilidade", visibilidade[i]))
}

cat("\n==============================\n")
cat("     📅 PREVISÃO DIÁRIA\n")
cat("==============================\n")

for (i in 1:nrow(df_diario)) {
  cat(sprintf("\n[%s]\n", df_diario$data[i]))
  cat(sprintf("  %-25s: %s °C\n", "Temp. Máxima", df_diario$temp_max[i]))
  cat(sprintf("  %-25s: %s °C\n", "Temp. Mínima", df_diario$temp_min[i]))
  cat(sprintf("  %-25s: %s mm\n", "Chuva total", df_diario$precipitacao_total[i]))
  cat(sprintf("  %-25s: %s\n", "Nascer do sol", df_diario$nascer_sol[i]))
  cat(sprintf("  %-25s: %s\n", "Pôr do sol", df_diario$por_sol[i]))
}

cat("\n==============================\n")
cat("         ✅ FIM\n")
cat("==============================\n\n")