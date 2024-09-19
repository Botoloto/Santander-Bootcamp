<h2>Web Scraping VivaReal 🌇</h2>

<p>Esse código é responsável por extrair as informações de venda de imóveis do site <a href="https://www.vivareal.com.br" target="_blank">VivaReal</a>.</p>

<p>Esse projeto não objetivo de venda, mas sim um estudo de bibliotecas de webscrapping e testes para treinamentos de IA.</p>

<h3>Bibliotecas Utilizadas 📖</h3>
<ul>
  <li>os</li>
  <li>cloudscraper</li>
  <li>BeautifulSoup (bs4)</li>
  <li>time</li>
  <li>pandas</li>
</ul>

<h3>Sobre o desenvolvimento 💻</h3>

<p>Fazendo uma breve filtragem dentro do próprio site, sua URL fica fixa com os filtros aplicados (podendo ser por cidade, tipo de imóvel, preço) e o código percorre as páginas alterando apenas o número presente no link.</p>
<p>O código coleta todas as informações de cada card do imóvel salvando desde a localização até o preço do condomínio:</p>
<ul>
    <li>Rua</li>
    <li>Bairro</li>
    <li>Estado</li>
    <li>Tipo</li>
    <li>Preço</li>
    <li>Metragem</li>
    <li>Quartos</li>
    <li>Banheiros</li>
    <li>Vagas</li>
    <li>Condomínio</li>
</ul>


<h3>Modo de uso ⛏️</h3>
<ol>
  <li>Com o <a href="https://www.python.org/downloads/" target="_blank">Python</a> já instalado, instale as bibliotecas necessárias utilizando o arquivo <strong> requirements.txt </strong> com o seguinte trecho de código: <code>pip install -r requirements.txt</code>.</li>
  <li>Escolha o link inicial para inicializar a extração, nessa parte comentada anteriormente é possivel aplicar filtros prévios para extrair apenas de uma cidade especifica ou algo do tipo.</li>
  <li>Também é necessário escolher quantas páginas devem ser extraídas, o site contém algumas limitações para grandes quantidade (valor recomendado 150 ~ 200)</li>
</ol>

<h3>Resultado 🥇</h3>
<p>Será criado um arquivo CSV chamado <strong>VivaRealData.xlsx</strong> no mesmo diretório do arquivo contendo todos os dados dos imóveis</p>
![vivarealdata](https://github.com/user-attachments/assets/238c5d15-1460-437f-ae99-944b481f8591)
