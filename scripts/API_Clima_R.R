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
print(json)
# -----------------------------
# 1. Data frame do clima atual
# -----------------------------
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

# -----------------------------
# 2. Data frame da previsão por hora
# -----------------------------
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

# -----------------------------
# 3. Data frame da previsão diária
# -----------------------------
df_diario <- data.frame(
  data = json$daily$time,
  temp_max = json$daily$temperature_2m_max,
  temp_min = json$daily$temperature_2m_min,
  precipitacao_total = json$daily$precipitation_sum,
  nascer_sol = json$daily$sunrise,
  por_sol = json$daily$sunset,
  stringsAsFactors = FALSE
)

# Mostrar resultados
print("=== CLIMA ATUAL ===")
print(df_atual)

print("=== PREVISAO HORARIA ===")
print(head(df_horario))

print("=== PREVISAO DIARIA ===")
print(df_diario)




#Dados antigos
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
uv <- json$hourly$uv_index
hora <- json$hourly$time

print(paste("Temperatura atual:", temperatura))
print(paste("Velocidade do vento:", vento))
print(paste("Direção do vento (graus):", dirvento))
print(paste("Código do tipo de clima:", tipclim))
print(paste("Dia(1) ou Noite (2):", dianoi))
print(paste("Horário da medição:", horario))



