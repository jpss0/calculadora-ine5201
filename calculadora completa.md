" Document calculator usage and tests"

AuthorDate: Sat Nov 14 21:51:47 2026 -0300
Commit:     jpss0 <jpsigarans@gmail.com>
CommitDate: Sat Nov 14 21:51:47 2026 -0300

    Document calculator usage and tests

 README.md | 48 ++++++++++++++++++++++++++++++++++++++++++++++--
 1 file changed, 46 insertions(+), 2 deletions(-)
diff --git a/README.md b/README.md
index f0f9a33..1bd652d 100644
--- a/README.md
+++ b/README.md
@@ -1,2 +1,46 @@
-# ligue-4-ine5201
-trabalho 1:jogo ligue 4
+# Calculadora
+
+Calculadora gráfica de desktop feita em Python e Tkinter. Ela realiza as
+quatro operações básicas, aceita números decimais, mostra mensagens para
+entradas inválidas e divisão por zero e mantém os 10 cálculos mais recentes.
+
+## Requisitos
+
+- Python 3.10 ou superior
+- Tkinter (incluido nas instalacoes oficiais do Python para Windows)
+
+Nao ha dependencias externas.
+
+## Como executar
+
+Na raiz do repositorio:
+
+```powershell
+python -m calculadora.main
+```
+
+O teclado também pode ser usado: digite números e operadores, use `Enter` para
+calcular, `Backspace` para apagar e `Escape` para limpar o display e o histórico.
+O botão `C` limpa o display e todo o histórico; `←` apaga o último dígito.
+
+## Testes
+
+```powershell
+python -m unittest discover -s tests -v
+```
+
+## Interface e comportamento
+
+- Teclado organizado como uma calculadora fisica, com display e operacoes.
+- Operações com `Decimal` para preservar a precisão decimal usual.
+- Mensagem de erro quando uma divisão por zero é tentada ou quando a sequência
+  de entrada está incompleta/inválida.
+- Histórico na ordem mais recente primeiro, limitado a 10 cálculos.
+
+## GitHub e GitHub Copilot
+
+Este projeto é mantido no repositório público
+[jpss0/calculadora-ine5201](https://github.com/jpss0/calculadora-ine5201).
+O GitHub Copilot foi usado como assistente para estruturar a interface,
+implementar o tratamento das operações e preparar testes. O código e os
+resultados dos testes foram revisados; o Copilot não substitui essa verificação.
