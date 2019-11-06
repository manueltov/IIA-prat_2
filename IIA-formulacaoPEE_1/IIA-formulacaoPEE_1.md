<div tabindex="-1" id="notebook" class="border-box-sizing">

<div class="container" id="notebook-container">

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

# Introdução à Inteligência Artificial - PEE / 1 - Formulação[¶](#Introdução-à-Inteligência-Artificial---PEE-/-1---Formulação)

# Guião Laboratorial[¶](#Guião-Laboratorial)

(30/Set:04/Out-2019)

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

## Introdução[¶](#Introdução)

Vamos ver como poderemos, usando a linguagem Python, resolver problemas formulados de acordo com o paradigma do espaço de estados (PEE). Para isso, há que completar dois passos:

1.  Definir o problema;
2.  Utilizar um algoritmo de procura para o resolver.

Nesta aula vamos tratar apenas da formulação, i.e., da definição do problema.

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Recordando, para formularmos um problema de acordo com esta metododologia, precisamos de:

*   **Estados**: Idealizar uma representação para o que vamos considerar um estado. Notem que o estado deve ser mínimo, apenas deve conter a informação que muda com as acções;
*   **Estado Inicial**: Identificar o estado inicial;
*   **Objectivo**: Verificar se um estado satisfaz o objectivo, sendo assim, um dos estados finais;
*   **Acções**: Para cada estado, caracterizar rigorosamente as acções de mudança de estado, de que modo incrementam os custos dos caminhos, e quais os estados resultantes.

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

## Recursos necessários[¶](#Recursos-necessários)

*   Para executar as experiências que se seguem, copie o módulo [searchPlus.py](searchPlus.py) para a directoria de trabalho.
*   Copie para o mesmo local os outros módulos auxiliares necessários: [utils.py](utils.py)
*   Crie um novo modulo **pee1.py** para ir realizando as experiências sugeridas.

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

## Módulo _searchPlus.py_ - breve explicação[¶](#Módulo-searchPlus.py---breve-explicação)

Este módulo é uma variante muito ligeira do search.py que está disponível no repositório [aima-python](https://github.com/aimacode/aima-python), que contém a implementação (em Python) da generalidade dos algoritmos descritos no livro da disciplina (Russell & Norvig). Muitas das definições deste módulo não serão utilizadas. Vamos apenas concentrar-nos em algumas das suas classes e funções. No essencial, é disponiblizado o seguinte:

*   A classe **Problem**, que vamos utilizar para definir os problemas;
*   A classe **Node**, que representa um **_nó de procura_**, utilizada pelos algoritmos de procura implementados;
*   A implementação de vários algoritmos de procura.

Para esta aula dedicada à formulação, apenas precisamos de usar a classe **Problem** do módulo, que tem de ser importado, mas não deverá alterá-lo.

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="kn">from</span> <span class="nn">searchPlus</span> <span class="k">import</span> <span class="o">*</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

## Exemplo base[¶](#Exemplo-base)

Para já, vamos ilustrar com um exemplo de problema que consiste num grafo de estados, com um estado inicial I e final F. Queremos encontrar uma sequência de acções que nos leve de I a F.

![Drawing](figura-ee-T-1.png)

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

### Representação de um estado[¶](#Representação-de-um-estado)

Não há qualquer restrição quanto ao tipo que o estado pode assumir (pode ser um inteiro, uma string, uma lista, um tuplo, etc, ou um tipo definido recorrendo a uma nova classe).

Neste exemplo do grafo abstracto, o estado é apenas uma etiqueta sem estrutura, Em python, vamos considerar que um estado é uma string de um caracter que corresponde aos nós do grafo. Vamos ter o seguinte conjunto de estados: {'I', 'A','B', 'C', 'D', 'F'}.

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

### A classe **Problem**[¶](#A-classe-Problem)

Esta classe funciona como uma classe _abstracta_. Para definir um problema concreto é necessário criar uma sua sub-classe. A classe **Problem** tem um construtor em que se passa o estado inicial e o estado final ou conjunto de estados finais e a função de teste do objectivo apenas verifica se um estado é igual ao estado final ou se pertence ao conjunto dos estados finais, respectivamente; tem também um método **_path_cost()_**, por defeito, que considera que todas as acções possuem custo 1, o que é o caso do nosso grafo em cima.

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="c1">## Apenas a definição da classe, ainda sem qualquer conteúdo</span>
<span class="k">class</span> <span class="nc">ProblemaGrafo</span><span class="p">(</span><span class="n">Problem</span><span class="p">)</span> <span class="p">:</span>
    <span class="k">pass</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Um problema é criado fornecendo a identificação do estado inicial e, opcionalmente, o objectivo. Veja-se a assinatura do construtor:

<div class="highlight">

<pre><span></span><span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">initial</span><span class="p">,</span> <span class="n">goal</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
    <span class="sd">"""The constructor specifies the initial state, and possibly a goal</span>
 <span class="sd">state, if there is a unique goal. Your subclass's constructor can add</span>
 <span class="sd">other arguments."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">initial</span> <span class="o">=</span> <span class="n">initial</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">goal</span> <span class="o">=</span> <span class="n">goal</span>
</pre>

</div>

Por exemplo, para criarmos o problema de encontrar um caminho entre **'I'** e **'F'** no espaço acima, poderíamos fazer:

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">problema_1</span> <span class="o">=</span> <span class="n">ProblemaGrafo</span><span class="p">(</span><span class="s1">'I'</span><span class="p">,</span><span class="s1">'F'</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Os atributos **initial** e **goal** guardam esta informação:

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">problema_1</span><span class="o">.</span><span class="n">initial</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">problema_1</span><span class="o">.</span><span class="n">goal</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

#### Definição do objectivo[¶](#Definição-do-objectivo)

Há duas formas de definir o teste de satisfação do objectivo:

1.  Indicando explicitamente o seu valor, utilizando o parâmetro **_goal_** do construtor; o parâmetro **_goal_** pode ser também uma lista de estados, nos casos em que existam vários estados finais.
2.  Redefinindo o método **goal_test()** na classe que define o nosso problema:

<div class="highlight">

<pre><span></span><span class="k">def</span> <span class="nf">goal_test</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
        <span class="sd">"""Return True if the state is a goal. The default method compares the</span>
 <span class="sd">state to self.goal or checks for state in self.goal if it is a</span>
 <span class="sd">list, as specified in the constructor. Override this method if</span>
 <span class="sd">checking against a single self.goal is not enough."""</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">goal</span><span class="p">,</span> <span class="nb">list</span><span class="p">):</span>
            <span class="k">return</span> <span class="n">state</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">goal</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">state</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">goal</span>
</pre>

</div>

Este método retornará `True` nos casos em que o estado fornecido (**state**) seja o estado final ou membro dos estados finais.

No exemplo acima, utilizámos a primeira opção, definindo como objectivo o estado **F**.

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

#### Operadores[¶](#Operadores)

A implementação dos operadores de mudança de estado é feita com base na definição de dois métodos:

*   `actions(self, state)` - Este método, dado um estado, devolve a lista de todas as acções possíveis nesse estado; a representação concreta do que é uma acção fica em aberto.
*   `result(self, state, action)` - Dados um estado e uma acção, este método devolve o estado resulante da execução da acção **_action_**, no estado **_state_**.

A definição destes dois métodos na classe que define o problema é **_obrigatória_**. Notem que a classe Problem tem os métodos **_actions()_** e **_result()_** por implementar.

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">problema_1</span><span class="o">.</span><span class="n">actions</span><span class="p">(</span><span class="n">problema_1</span><span class="o">.</span><span class="n">initial</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Continuando o mesmo exemplo, antes de definir estas funções, temos que representar o grafo que define o espaço de estados ilustrado acima.

Uma possiblidade é utilizar um dicionário:

<div class="highlight">

<pre><span></span><span class="n">grafo</span> <span class="o">=</span> <span class="p">{</span><span class="s1">'I'</span><span class="p">:[</span><span class="s1">'A'</span><span class="p">,</span><span class="s1">'B'</span><span class="p">],</span>
         <span class="s1">'A'</span><span class="p">:[</span><span class="s1">'C'</span><span class="p">,</span><span class="s1">'D'</span><span class="p">,</span><span class="s1">'I'</span><span class="p">],</span>
         <span class="s1">'B'</span><span class="p">:[</span><span class="s1">'D'</span><span class="p">,</span><span class="s1">'F'</span><span class="p">,</span><span class="s1">'I'</span><span class="p">],</span>
         <span class="s1">'C'</span><span class="p">:[],</span>
         <span class="s1">'D'</span><span class="p">:[</span><span class="s1">'C'</span><span class="p">,</span><span class="s1">'F'</span><span class="p">],</span>
         <span class="s1">'F'</span><span class="p">:[]}</span>
</pre>

</div>

Nesta representação de um grafo, a chave é um estado, sendo o valor correspondente a lista dos possíveis sucessores.

Como os custos dos arcos são homogéneos, não é necessário representá-los. A classe **Problem** atribui o custo 1 a cada acção por defeito, através do método **_path_cost()_**. Mas o método recebe como parâmetro o custo que vai do estado inicial até state1 e adiciona-lhe 1, que é o custo de ir de state1 para state2.

<div class="highlight">

<pre><span></span><span class="k">def</span> <span class="nf">path_cost</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">c</span><span class="p">,</span> <span class="n">state1</span><span class="p">,</span> <span class="n">action</span><span class="p">,</span> <span class="n">state2</span><span class="p">):</span>
        <span class="sd">"""Return the cost of a solution path that arrives at state2 from</span>
 <span class="sd">state1 via action, assuming cost c to get up to state1\. If the problem</span>
 <span class="sd">is such that the path doesn't matter, this function will only look at</span>
 <span class="sd">state2\.  If the path does matter, it will consider c and maybe state1</span>
 <span class="sd">and action. The default method costs 1 for every step in the path."""</span>
        <span class="k">return</span> <span class="n">c</span> <span class="o">+</span> <span class="mi">1</span>
</pre>

</div>

Não precisaremos de redefinir este método mas apenas o método **_actions()_** e o método **_result()_**. Vamos a isso.

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

##### Definindo o método **_actions()_**[¶](#Definindo-o-método-actions())

Neste exemplo abstracto, uma acção é simplesmente uma transição entre dois estados, X e Y, que poderemos representar pela string **"Ir de X para Y"**.

Assim, podemos ter a seguinte definição do método **_actions()_**:

<div class="highlight">

<pre><span></span><span class="k">def</span> <span class="nf">actions</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">estado</span><span class="p">)</span> <span class="p">:</span>
    <span class="n">sucessores</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">grafo</span><span class="p">[</span><span class="n">estado</span><span class="p">]</span>  <span class="c1"># obter lista dos sucessores</span>
    <span class="n">accoes</span> <span class="o">=</span> <span class="nb">map</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span> <span class="p">:</span> <span class="s2">"ir de {} para {}"</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">estado</span><span class="p">,</span><span class="n">x</span><span class="p">),</span><span class="n">sucessores</span><span class="p">)</span> <span class="c1"># compor as strings que representam cada uma das possíveis acções</span>
    <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="n">accoes</span><span class="p">)</span>
</pre>

</div>

Notem que a função **_map()_** aplica uma função a todos os elementos de uma lista. Neste caso, a função é uma função lambda ou anónima, criada e usada na hora.

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

##### Definindo o método **_result()_**[¶](#Definindo-o-método-result())

O método **_result()_** recebe como um dos parâmetros uma acção, que terá que ter o formato determinado pelo método **_actions()_**. Não tem de se preocupar com as pré-condições das acções porque é o método **_actions()_** que trata disso.

Como cada acção é uma cadeia de caracteres em que o último é o estado seguinte ou sucessor, destino da acção, o que queremos é obter a última palavra de uma _acção_. Vamos usar o método **_split()_** das strings para partir a frase numa lista de palavras e depois vamos buscar a última, usando o índice -1 de uma lista.

<div class="highlight">

<pre><span></span><span class="k">def</span> <span class="nf">result</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">estado</span><span class="p">,</span> <span class="n">accao</span><span class="p">)</span> <span class="p">:</span>
        <span class="sd">"""Assume-se que uma acção é da forma 'ir de X para Y'</span>
 <span class="sd">"""</span>
        <span class="k">return</span> <span class="n">accao</span><span class="o">.</span><span class="n">split</span><span class="p">()[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
</pre>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Vejamos então como fica a definição completa da classe:

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="k">class</span> <span class="nc">ProblemaGrafo</span><span class="p">(</span><span class="n">Problem</span><span class="p">)</span> <span class="p">:</span>
    <span class="n">grafo</span> <span class="o">=</span> <span class="p">{</span><span class="s1">'I'</span><span class="p">:[</span><span class="s1">'A'</span><span class="p">,</span><span class="s1">'B'</span><span class="p">],</span>
             <span class="s1">'A'</span><span class="p">:[</span><span class="s1">'C'</span><span class="p">,</span><span class="s1">'D'</span><span class="p">,</span><span class="s1">'I'</span><span class="p">],</span>
             <span class="s1">'B'</span><span class="p">:[</span><span class="s1">'D'</span><span class="p">,</span><span class="s1">'F'</span><span class="p">,</span><span class="s1">'I'</span><span class="p">],</span>
             <span class="s1">'C'</span><span class="p">:[],</span>
             <span class="s1">'D'</span><span class="p">:[</span><span class="s1">'C'</span><span class="p">,</span><span class="s1">'F'</span><span class="p">],</span>
             <span class="s1">'F'</span><span class="p">:[]}</span>

    <span class="k">def</span> <span class="nf">actions</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">estado</span><span class="p">)</span> <span class="p">:</span>
        <span class="n">sucessores</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">grafo</span><span class="p">[</span><span class="n">estado</span><span class="p">]</span>
        <span class="n">accoes</span> <span class="o">=</span> <span class="nb">map</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span> <span class="p">:</span> <span class="s2">"ir de</span> <span class="si">{}</span> <span class="s2">para</span> <span class="si">{}</span><span class="s2">"</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">estado</span><span class="p">,</span><span class="n">x</span><span class="p">),</span><span class="n">sucessores</span><span class="p">)</span>
        <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="n">accoes</span><span class="p">)</span>
        <span class="c1">#</span>
        <span class="c1"># alternativamente:</span>
        <span class="c1"># accoes = ["ir de {} para {}".format(estado,x) for x in sucessores]</span>
        <span class="c1"># return accoes</span>
        <span class="c1">#</span>
        <span class="c1"># alternaivamente:</span>
        <span class="c1"># accoes = list()</span>
        <span class="c1"># for x in sucessores :</span>
        <span class="c1">#     accoes.append("ir de {} para {}".format(estado,x))</span>
        <span class="c1"># return accoes</span>

    <span class="k">def</span> <span class="nf">result</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">estado</span><span class="p">,</span> <span class="n">accao</span><span class="p">)</span> <span class="p">:</span>
        <span class="sd">"""Assume-se que uma acção é da forma 'ir de X para Y'</span>
 <span class="sd">"""</span>
        <span class="k">return</span> <span class="n">accao</span><span class="o">.</span><span class="n">split</span><span class="p">()[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Podemos então redefinir o nosso problema e verificar se os métodos dão o resultado esperado:

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">p1</span> <span class="o">=</span> <span class="n">ProblemaGrafo</span><span class="p">(</span><span class="s1">'I'</span><span class="p">,</span><span class="s1">'F'</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Vamos listar todos os estados

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="nb">print</span><span class="p">(</span><span class="s2">"Estados:"</span><span class="p">)</span>
<span class="k">for</span> <span class="n">estado</span> <span class="ow">in</span> <span class="n">p1</span><span class="o">.</span><span class="n">grafo</span><span class="o">.</span><span class="n">keys</span><span class="p">():</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">estado</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Listemos todas as acções possíveis a partir do estado inicial do problema

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">p1</span><span class="o">.</span><span class="n">actions</span><span class="p">(</span><span class="n">p1</span><span class="o">.</span><span class="n">initial</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Vejemos qual o resultado de executar a acção 'ir de I para B' a partir de I

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">p1</span><span class="o">.</span><span class="n">result</span><span class="p">(</span><span class="s1">'I'</span><span class="p">,</span><span class="s1">'ir de I para B'</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Testemos se 'B' é o estado final

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">p1</span><span class="o">.</span><span class="n">goal_test</span><span class="p">(</span><span class="s1">'B'</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Vamos aplicar a primeira accão ao estado inicial e verifiquemos onde estamos

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">p1</span><span class="o">.</span><span class="n">result</span><span class="p">(</span><span class="n">p1</span><span class="o">.</span><span class="n">initial</span><span class="p">,</span><span class="n">p1</span><span class="o">.</span><span class="n">actions</span><span class="p">(</span><span class="n">p1</span><span class="o">.</span><span class="n">initial</span><span class="p">)[</span><span class="mi">0</span><span class="p">])</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Vamos testar a satisfação do objectivo e calcular os custo progressivamente à medida que vamos executando a primeira acção dado o estado inicial e a segunda dado o estado resultate.

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">custo</span><span class="o">=</span><span class="mi">0</span>
<span class="n">e0</span> <span class="o">=</span> <span class="n">p1</span><span class="o">.</span><span class="n">initial</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">'Em'</span><span class="p">,</span><span class="n">e0</span><span class="p">,</span><span class="s1">'com custo'</span><span class="p">,</span><span class="n">custo</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">'Cheguei ao objectivo?'</span><span class="p">,</span><span class="n">p1</span><span class="o">.</span><span class="n">goal_test</span><span class="p">(</span><span class="n">e0</span><span class="p">))</span>
<span class="n">a1</span> <span class="o">=</span> <span class="n">p1</span><span class="o">.</span><span class="n">actions</span><span class="p">(</span><span class="n">e0</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
<span class="n">e1</span> <span class="o">=</span> <span class="n">p1</span><span class="o">.</span><span class="n">result</span><span class="p">(</span><span class="n">e0</span><span class="p">,</span><span class="n">a1</span><span class="p">)</span>
<span class="n">custo</span> <span class="o">=</span> <span class="n">p1</span><span class="o">.</span><span class="n">path_cost</span><span class="p">(</span><span class="n">custo</span><span class="p">,</span><span class="n">e0</span><span class="p">,</span><span class="n">a1</span><span class="p">,</span><span class="n">e1</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">'Após executar a 1ª acção:'</span><span class="p">,</span> <span class="n">a1</span><span class="p">,</span> <span class="s1">'passei para '</span><span class="p">,</span><span class="n">e1</span><span class="p">,</span> <span class="s1">', com custo'</span><span class="p">,</span><span class="n">custo</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">'Cheguei ao objectivo?'</span><span class="p">,</span><span class="n">p1</span><span class="o">.</span><span class="n">goal_test</span><span class="p">(</span><span class="n">e1</span><span class="p">))</span>
<span class="n">a2</span> <span class="o">=</span> <span class="n">p1</span><span class="o">.</span><span class="n">actions</span><span class="p">(</span><span class="n">e1</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
<span class="n">e2</span> <span class="o">=</span> <span class="n">p1</span><span class="o">.</span><span class="n">result</span><span class="p">(</span><span class="n">e1</span><span class="p">,</span><span class="n">a2</span><span class="p">)</span>
<span class="n">custo</span> <span class="o">=</span> <span class="n">p1</span><span class="o">.</span><span class="n">path_cost</span><span class="p">(</span><span class="n">custo</span><span class="p">,</span><span class="n">e1</span><span class="p">,</span><span class="n">a2</span><span class="p">,</span><span class="n">e2</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">'Após executar a 2ª acção:'</span><span class="p">,</span> <span class="n">a2</span><span class="p">,</span> <span class="s1">'passei para '</span><span class="p">,</span><span class="n">e2</span><span class="p">,</span> <span class="s1">', com custo'</span><span class="p">,</span><span class="n">custo</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">'Cheguei ao objectivo?'</span><span class="p">,</span><span class="n">p1</span><span class="o">.</span><span class="n">goal_test</span><span class="p">(</span><span class="n">e1</span><span class="p">))</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

#### A função **_**eq()**_**[¶](#A-função-eq())

Quando existem vários estados finais que podemos enumerar, o método **_goal_test()_** verifica se um estado é membro de uma lista de estados usando "in". Neste caso, como os estados são strings o "in" funciona bem e não é preciso redefinir o teste de igualdade. De notar que se os estados fossem instâncias de uma classe e não strings, e como dois objectos diferentes mas com o mesmo conteúdo não são naturalmente iguais mas deveriam ser iguais, teríamos de redefinir o **_**eq()**_**.

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

#### Exercício 1[¶](#Exercício-1)

Crie um problema da classe **ProblemaGrafo** com o estado inicial 'A' e estados finais 'F' e 'E'

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

#### Exercício 2[¶](#Exercício-2)

Como poderá mudar o grafo da classe **ProblemaGrafo** de modo a poderem utilizar diferentes grafos e não apenas este? Ficam aqui duas sugestões e podem implementar as duas: (1) mudem o valor do atributo estático antes ou depois de criarem uma instância da classe; (2) Refaçam a classe de modo a que o grafo seja passado como parâmetro no construtor, sendo um atributo dinâmico e privado de cada objecto do tipo **ProblemaGrafo**.

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

## Grafo abstracto com custos[¶](#Grafo-abstracto-com-custos)

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Vamos primeiro representar este grafo com custos num dicionário em que cada chave é um estado e em que o valor é um novo dicionário, sendo a chave o estado sucessor e o valor o custo do arco. O grafo será guardado no atributo grafo da nova classe

<div class="highlight">

<pre><span></span><span class="n">grafo</span> <span class="o">=</span> <span class="p">{</span><span class="s1">'I'</span><span class="p">:{</span><span class="s1">'A'</span><span class="p">:</span><span class="mi">2</span><span class="p">,</span><span class="s1">'B'</span><span class="p">:</span><span class="mi">5</span><span class="p">},</span>
             <span class="s1">'A'</span><span class="p">:{</span><span class="s1">'C'</span><span class="p">:</span><span class="mi">2</span><span class="p">,</span><span class="s1">'D'</span><span class="p">:</span><span class="mi">4</span><span class="p">,</span><span class="s1">'I'</span><span class="p">:</span><span class="mi">2</span><span class="p">},</span>
             <span class="s1">'B'</span><span class="p">:{</span><span class="s1">'D'</span><span class="p">:</span><span class="mi">1</span><span class="p">,</span><span class="s1">'F'</span><span class="p">:</span><span class="mi">5</span><span class="p">,</span><span class="s1">'I'</span><span class="p">:</span><span class="mi">5</span><span class="p">},</span>
             <span class="s1">'C'</span><span class="p">:{},</span>
             <span class="s1">'D'</span><span class="p">:{</span><span class="s1">'C'</span><span class="p">:</span><span class="mi">3</span><span class="p">,</span><span class="s1">'F'</span><span class="p">:</span><span class="mi">2</span><span class="p">},</span>
             <span class="s1">'F'</span><span class="p">:{}}</span>
</pre>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Olhemos agora para um grafo em que os custos não são homogéneos. Por exemplo este:

![Drawing](figura-ee-T-2.png)

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Para além disso, precisamos de criar um método **_path_cost()_** que se vai sobrepor ao método da super-classe **Problem**. Lembram-se que este último devolve sempre 1 como custo. Este método recebe o custo actual do caminho (c) desde o estado inicial até ao estado **_state1_**, calculado pelo algoritmo de procura. A acção (**_action_**) provoca uma transição entre **_state1_** e **_state2_** e o custo da acção é adicionado a **_c_**. Para sabermos qual o custo da acção que leva do **_state1_** ao **_state2_** teremos de ir ler no grafo.

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

<div class="highlight">

<pre><span></span><span class="k">def</span> <span class="nf">path_cost</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">c</span><span class="p">,</span> <span class="n">state1</span><span class="p">,</span> <span class="n">action</span><span class="p">,</span> <span class="n">state2</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">c</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">grafo</span><span class="p">[</span><span class="n">state1</span><span class="p">][</span><span class="n">state2</span><span class="p">]</span>
</pre>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Vejamos então a definição completa da nova classe:

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="k">class</span> <span class="nc">ProblemaGrafoCustos</span><span class="p">(</span><span class="n">Problem</span><span class="p">)</span> <span class="p">:</span>
    <span class="n">grafo</span> <span class="o">=</span> <span class="p">{</span><span class="s1">'I'</span><span class="p">:{</span><span class="s1">'A'</span><span class="p">:</span><span class="mi">2</span><span class="p">,</span><span class="s1">'B'</span><span class="p">:</span><span class="mi">5</span><span class="p">},</span>
             <span class="s1">'A'</span><span class="p">:{</span><span class="s1">'C'</span><span class="p">:</span><span class="mi">2</span><span class="p">,</span><span class="s1">'D'</span><span class="p">:</span><span class="mi">4</span><span class="p">,</span><span class="s1">'I'</span><span class="p">:</span><span class="mi">2</span><span class="p">},</span>
             <span class="s1">'B'</span><span class="p">:{</span><span class="s1">'D'</span><span class="p">:</span><span class="mi">1</span><span class="p">,</span><span class="s1">'F'</span><span class="p">:</span><span class="mi">5</span><span class="p">,</span><span class="s1">'I'</span><span class="p">:</span><span class="mi">5</span><span class="p">},</span>
             <span class="s1">'C'</span><span class="p">:{},</span>
             <span class="s1">'D'</span><span class="p">:{</span><span class="s1">'C'</span><span class="p">:</span><span class="mi">3</span><span class="p">,</span><span class="s1">'F'</span><span class="p">:</span><span class="mi">2</span><span class="p">},</span>
             <span class="s1">'F'</span><span class="p">:{}}</span>

    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">initial</span> <span class="o">=</span> <span class="s1">'I'</span><span class="p">,</span> <span class="n">final</span> <span class="o">=</span> <span class="s1">'F'</span><span class="p">)</span> <span class="p">:</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">initial</span><span class="p">,</span><span class="n">final</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">actions</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">estado</span><span class="p">)</span> <span class="p">:</span>
        <span class="n">sucessores</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">grafo</span><span class="p">[</span><span class="n">estado</span><span class="p">]</span><span class="o">.</span><span class="n">keys</span><span class="p">()</span>  <span class="c1"># métodos keys() devolve a lista das chaves do dicionário</span>
        <span class="n">accoes</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="nb">map</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span> <span class="p">:</span> <span class="s2">"ir de</span> <span class="si">{}</span> <span class="s2">para</span> <span class="si">{}</span><span class="s2">"</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">estado</span><span class="p">,</span><span class="n">x</span><span class="p">),</span><span class="n">sucessores</span><span class="p">))</span>
        <span class="k">return</span> <span class="n">accoes</span>

    <span class="k">def</span> <span class="nf">result</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">estado</span><span class="p">,</span> <span class="n">accao</span><span class="p">)</span> <span class="p">:</span>
        <span class="sd">"""Assume-se que uma acção é da forma 'ir de X para Y'</span>
 <span class="sd">"""</span>
        <span class="k">return</span> <span class="n">accao</span><span class="o">.</span><span class="n">split</span><span class="p">()[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">path_cost</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">c</span><span class="p">,</span> <span class="n">state1</span><span class="p">,</span> <span class="n">action</span><span class="p">,</span> <span class="n">state2</span><span class="p">):</span>
        <span class="sd">"""Assume-se que action é da forma 'ir de <state1> para <state2>'</span>
 <span class="sd">"""</span>
        <span class="k">return</span> <span class="n">c</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">grafo</span><span class="p">[</span><span class="n">state1</span><span class="p">][</span><span class="n">state2</span><span class="p">]</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Vamos criar um problema e executar algumas operações.

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">p</span> <span class="o">=</span> <span class="n">ProblemaGrafoCustos</span><span class="p">()</span>
<span class="n">custo</span> <span class="o">=</span> <span class="mi">0</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Estado inicial:"</span><span class="p">,</span><span class="n">p</span><span class="o">.</span><span class="n">initial</span><span class="p">,</span> <span class="s1">'com custo'</span><span class="p">,</span><span class="n">custo</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Estado final:"</span><span class="p">,</span><span class="n">p</span><span class="o">.</span><span class="n">goal</span><span class="p">)</span>
<span class="n">actions</span> <span class="o">=</span> <span class="n">p</span><span class="o">.</span><span class="n">actions</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">initial</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">'Cheguei ao objectivo?'</span><span class="p">,</span><span class="n">p1</span><span class="o">.</span><span class="n">goal_test</span><span class="p">(</span><span class="n">e0</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"As acções do estado inicial:"</span><span class="p">,</span><span class="nb">str</span><span class="p">(</span><span class="n">actions</span><span class="p">))</span>
<span class="n">e1</span> <span class="o">=</span> <span class="n">p</span><span class="o">.</span><span class="n">result</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">initial</span><span class="p">,</span><span class="n">actions</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Partindo de"</span><span class="p">,</span> <span class="n">p</span><span class="o">.</span><span class="n">initial</span><span class="p">,</span><span class="s2">"executo a acção de "</span> <span class="o">+</span> <span class="n">actions</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">+</span><span class="s2">" e vou parar em :"</span><span class="p">,</span><span class="n">e1</span><span class="p">)</span>
<span class="n">custo</span> <span class="o">=</span> <span class="n">p</span><span class="o">.</span><span class="n">path_cost</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="n">p</span><span class="o">.</span><span class="n">initial</span><span class="p">,</span><span class="n">actions</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span><span class="n">e1</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"O custo desde o início é:"</span><span class="p">,</span><span class="n">custo</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">'Cheguei ao objectivo?'</span><span class="p">,</span><span class="n">p1</span><span class="o">.</span><span class="n">goal_test</span><span class="p">(</span><span class="n">e1</span><span class="p">))</span>
<span class="n">e2</span> <span class="o">=</span> <span class="n">p</span><span class="o">.</span><span class="n">result</span><span class="p">(</span><span class="n">e1</span><span class="p">,</span><span class="n">p1</span><span class="o">.</span><span class="n">actions</span><span class="p">(</span><span class="n">e1</span><span class="p">)[</span><span class="mi">1</span><span class="p">])</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Partindo de"</span><span class="p">,</span> <span class="n">e1</span><span class="p">,</span><span class="s2">"executo a acção de "</span> <span class="o">+</span> <span class="n">p1</span><span class="o">.</span><span class="n">actions</span><span class="p">(</span><span class="n">e1</span><span class="p">)[</span><span class="mi">1</span><span class="p">]</span><span class="o">+</span><span class="s2">" e vou parar em :"</span><span class="p">,</span><span class="n">e2</span><span class="p">)</span>
<span class="n">custo</span> <span class="o">=</span> <span class="n">p</span><span class="o">.</span><span class="n">path_cost</span><span class="p">(</span><span class="n">custo</span><span class="p">,</span><span class="n">e1</span><span class="p">,</span><span class="n">actions</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span><span class="n">e2</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"O custo desde o início é:"</span><span class="p">,</span><span class="n">custo</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">'Cheguei ao objectivo?'</span><span class="p">,</span><span class="n">p1</span><span class="o">.</span><span class="n">goal_test</span><span class="p">(</span><span class="n">e2</span><span class="p">))</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

## O Problema da inversão das setas[¶](#O-Problema-da-inversão-das-setas)

![Drawing](6arrows.PNG) Nesta aula vamos ver como poderemos, usando a linguagem Python, formular o problema da inversão das setas

Recordando o enunciado: Imagine que temos seis setas dispostas de cima para baixo, em que as primeiras 3 estão orientadas para a esquerda e as 3 últimas para a direita e que queremos obter seis setas com orientação alternadas, quando o único movimento possível é inverter a orientação de duas setas adjacentes.

Se partirmos da situação inicial e aplicarmos a inversão das duas primeiras setas, obteremos todas orientadas para a direita, excepto a terceira.

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

### Representação dos estados[¶](#Representação-dos-estados)

Podemos representar os estados deste problema como sendo objectos com um atributo que é uma lista de comprimento 6 em que da esquerda para a direita representamos a orientação das setas de cima para baixo, em que "d" indica que uma seta aponta para a direita e "e" representa o sentido da seta para a esquerda. A situação inicial é dada pela lista: [e,e,e,d,d,d]

Vamos ter um atributo **_setas_** onde guardamos a lista.

Precisamos de um método que inverta uma seta: de "e" para "d" e viceversa.

E precisamos de um método que permita inverter um par de setas adjacentes indicando o primeiro índice: 1 para inverter a primeira e a segunda, ..., 5 para inverter a quinta e sexta setas.

Finalmente, precisamos de imprimir as setas de um modo mais ou menos "pretty".

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="k">class</span> <span class="nc">EstadoSetas</span> <span class="p">:</span>

    <span class="sd">"""Um estado do problema da inversao das setas</span>
 <span class="sd">Uma lista de 6 setas (e's ou d's), indicando para cada seta se está orientada</span>
 <span class="sd">para a esquerda para para a direita</span>
 <span class="sd">A ordem da esquerda para a direita corresponde às setas de cima para baixo</span>
 <span class="sd">"""</span>
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">setas</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"e"</span><span class="p">,</span><span class="s2">"e"</span><span class="p">,</span><span class="s2">"e"</span><span class="p">,</span><span class="s2">"d"</span><span class="p">,</span><span class="s2">"d"</span><span class="p">,</span><span class="s2">"d"</span><span class="p">])</span> <span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">setas</span> <span class="o">=</span> <span class="n">setas</span>

    <span class="k">def</span> <span class="nf">flip</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">seta</span><span class="p">)</span> <span class="p">:</span>
        <span class="sd">""" Inversão do sentido de uma seta: de e para d e de d para e"""</span>
        <span class="k">if</span> <span class="n">seta</span><span class="o">==</span><span class="s2">"e"</span><span class="p">:</span>
            <span class="k">return</span> <span class="s2">"d"</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="s2">"e"</span>

    <span class="k">def</span> <span class="nf">inverte</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">n</span><span class="p">)</span> <span class="p">:</span>
        <span class="sd">""" Inverte duas setas, na posição n e n+1\. A primeira seta está na posição 0</span>
 <span class="sd">e para inverter a primeira e a segunda, de cima para baixo, implica n = 0.</span>
 <span class="sd">Gera uma nova lista.</span>
 <span class="sd">"""</span>
        <span class="n">copye</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">setas</span><span class="p">))</span> <span class="p">:</span>
            <span class="k">if</span> <span class="n">i</span> <span class="o">==</span> <span class="n">n</span><span class="o">-</span><span class="mi">1</span> <span class="ow">or</span> <span class="n">i</span> <span class="o">==</span> <span class="n">n</span> <span class="p">:</span>
                <span class="n">copye</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">flip</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">setas</span><span class="p">[</span><span class="n">i</span><span class="p">]))</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">copye</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">setas</span><span class="p">[</span><span class="n">i</span><span class="p">])</span>
        <span class="k">return</span> <span class="n">EstadoSetas</span><span class="p">(</span><span class="n">copye</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="p">:</span>
        <span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="s2">"-"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">setas</span><span class="p">))</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Podemos criar uma instância de um estado, por exemplo, o caso inicial do problema, desta maneira, sem passar quaisquer argumentos:

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">x</span> <span class="o">=</span> <span class="n">EstadoSetas</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">x</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Se quisermos criar uma nova instância, com outra combinação de orientações teremos de "pisar" o valor por omissão.

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">x</span> <span class="o">=</span> <span class="n">EstadoSetas</span><span class="p">([</span><span class="s2">"d"</span><span class="p">,</span><span class="s2">"e"</span><span class="p">,</span><span class="s2">"d"</span><span class="p">,</span><span class="s2">"d"</span><span class="p">,</span><span class="s2">"d"</span><span class="p">,</span><span class="s2">"e"</span><span class="p">])</span>
<span class="nb">print</span><span class="p">(</span><span class="n">x</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Se quisermos inverter a segunda e terceira seta de x, faremos:

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="nb">print</span><span class="p">(</span><span class="s2">"Começamos com:"</span><span class="p">,</span><span class="n">x</span><span class="p">)</span>
<span class="n">y</span> <span class="o">=</span> <span class="n">x</span><span class="o">.</span><span class="n">inverte</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">'Dado'</span><span class="p">,</span><span class="n">x</span><span class="p">,</span><span class="s2">"inverte a primeira e a segunda:"</span><span class="p">,</span><span class="n">y</span><span class="p">)</span>
<span class="n">z</span> <span class="o">=</span> <span class="n">y</span><span class="o">.</span><span class="n">inverte</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">'Dado'</span><span class="p">,</span><span class="n">y</span><span class="p">,</span><span class="s2">"inverte a segunda e terceira setas:"</span><span class="p">,</span><span class="n">z</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Podemos agora inverter de novo a 1ª e 2ª setas , depois de inverter a 2ª e 3ª, regressando à configuração inicial.

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">f</span> <span class="o">=</span> <span class="n">z</span><span class="o">.</span><span class="n">inverte</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span><span class="o">.</span><span class="n">inverte</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Iguais?"</span><span class="p">,</span><span class="n">f</span> <span class="o">==</span> <span class="n">x</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"f ="</span><span class="p">,</span><span class="n">f</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"x ="</span><span class="p">,</span><span class="n">x</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Como pudemos ver, os dois estados não são considerados iguais embora os seus atributos _setas_ sejam iguais. São duas instâncias diferentes. Assim, a função de teste **_goal_test()_** herdada de Problem não irá funcionar porque para verificar se um objecto é membro de uma lista é preciso que esse objecto seja membro da lista, i.e., igual a algum elemento da lista.

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">EstadoSetas</span><span class="p">([</span><span class="s1">'d'</span><span class="p">,</span><span class="s1">'e'</span><span class="p">,</span><span class="s1">'d'</span><span class="p">,</span><span class="s1">'e'</span><span class="p">,</span><span class="s1">'d'</span><span class="p">,</span><span class="s1">'e'</span><span class="p">])</span> <span class="ow">in</span> <span class="p">[</span><span class="n">EstadoSetas</span><span class="p">([</span><span class="s1">'d'</span><span class="p">,</span><span class="s1">'e'</span><span class="p">,</span><span class="s1">'d'</span><span class="p">,</span><span class="s1">'e'</span><span class="p">,</span><span class="s1">'d'</span><span class="p">,</span><span class="s1">'e'</span><span class="p">]),</span><span class="n">EstadoSetas</span><span class="p">([</span><span class="s1">'e'</span><span class="p">,</span><span class="s1">'d'</span><span class="p">,</span><span class="s1">'e'</span><span class="p">,</span><span class="s1">'d'</span><span class="p">,</span><span class="s1">'e'</span><span class="p">,</span><span class="s1">'d'</span><span class="p">])]</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">EstadoSetas</span><span class="p">([</span><span class="s1">'d'</span><span class="p">,</span><span class="s1">'e'</span><span class="p">,</span><span class="s1">'d'</span><span class="p">,</span><span class="s1">'e'</span><span class="p">,</span><span class="s1">'d'</span><span class="p">,</span><span class="s1">'e'</span><span class="p">])</span> <span class="o">==</span> <span class="n">EstadoSetas</span><span class="p">([</span><span class="s1">'d'</span><span class="p">,</span><span class="s1">'e'</span><span class="p">,</span><span class="s1">'d'</span><span class="p">,</span><span class="s1">'e'</span><span class="p">,</span><span class="s1">'d'</span><span class="p">,</span><span class="s1">'e'</span><span class="p">])</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Vamos definir o método **eq** de modo a que os estados sejam considerados iguais quando as **_setas_** forem iguais.

<div class="highlight">

<pre><span></span><span class="k">def</span> <span class="fm">__eq__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">estado</span><span class="p">)</span> <span class="p">:</span>
        <span class="sd">"""Definir em que circunstância os dois estados são considerados iguais.</span>
 <span class="sd">Necessário para os algoritmos de procura em grafo.</span>
 <span class="sd">"""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">setas</span> <span class="o">==</span> <span class="n">estado</span><span class="o">.</span><span class="n">setas</span>
</pre>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Vejemos a redefinição da classe **Setas()**

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="k">class</span> <span class="nc">EstadoSetas</span> <span class="p">:</span>

    <span class="sd">"""Um estado do problema da inversao das setas</span>
 <span class="sd">Uma lista de 6 setas (e's ou d's), indicando para cada seta se está orientada</span>
 <span class="sd">para a esquerda para para a direita</span>
 <span class="sd">A ordem da esquerda para a direita corresponde às setas de cima para baixo</span>
 <span class="sd">"""</span>
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">setas</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"e"</span><span class="p">,</span><span class="s2">"e"</span><span class="p">,</span><span class="s2">"e"</span><span class="p">,</span><span class="s2">"d"</span><span class="p">,</span><span class="s2">"d"</span><span class="p">,</span><span class="s2">"d"</span><span class="p">])</span> <span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">setas</span> <span class="o">=</span> <span class="n">setas</span>

    <span class="k">def</span> <span class="nf">flip</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">seta</span><span class="p">)</span> <span class="p">:</span>
        <span class="sd">""" Inversão do sentido de uma seta: de e para d e de d para e"""</span>
        <span class="k">if</span> <span class="n">seta</span><span class="o">==</span><span class="s2">"e"</span><span class="p">:</span>
            <span class="k">return</span> <span class="s2">"d"</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="s2">"e"</span>

    <span class="k">def</span> <span class="nf">inverte</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">n</span><span class="p">)</span> <span class="p">:</span>
        <span class="sd">""" Inverte duas setas, na posição n e n+1\. A primeira seta está na posição 0</span>
 <span class="sd">e para inverter a primeira e a segunda, de cima para baixo, implica n = 0.</span>
 <span class="sd">Gera uma nova lista.</span>
 <span class="sd">"""</span>
        <span class="n">copye</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">setas</span><span class="p">))</span> <span class="p">:</span>
            <span class="k">if</span> <span class="n">i</span> <span class="o">==</span> <span class="n">n</span><span class="o">-</span><span class="mi">1</span> <span class="ow">or</span> <span class="n">i</span> <span class="o">==</span> <span class="n">n</span> <span class="p">:</span>
                <span class="n">copye</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">flip</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">setas</span><span class="p">[</span><span class="n">i</span><span class="p">]))</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">copye</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">setas</span><span class="p">[</span><span class="n">i</span><span class="p">])</span>
        <span class="k">return</span> <span class="n">EstadoSetas</span><span class="p">(</span><span class="n">copye</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">__eq__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">estado</span><span class="p">)</span> <span class="p">:</span>
        <span class="sd">"""Definir em que circunstância os dois estados são considerados iguais.</span>
 <span class="sd">Necessário para os algoritmos de procura em grafo.</span>
 <span class="sd">"""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">setas</span> <span class="o">==</span> <span class="n">estado</span><span class="o">.</span><span class="n">setas</span>

    <span class="k">def</span> <span class="nf">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="p">:</span>
        <span class="sd">"""setas (d ou e) separadas por "-"s</span>
 <span class="sd">"""</span>
        <span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="s2">"-"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">setas</span><span class="p">))</span>

</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Voltemos a repetir as acções que fizemos lá trás.

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">x</span> <span class="o">=</span> <span class="n">EstadoSetas</span><span class="p">([</span><span class="s2">"d"</span><span class="p">,</span><span class="s2">"e"</span><span class="p">,</span><span class="s2">"d"</span><span class="p">,</span><span class="s2">"d"</span><span class="p">,</span><span class="s2">"d"</span><span class="p">,</span><span class="s2">"e"</span><span class="p">])</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Começamos com:"</span><span class="p">,</span><span class="n">x</span><span class="p">)</span>
<span class="n">y</span> <span class="o">=</span> <span class="n">x</span><span class="o">.</span><span class="n">inverte</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Agora, inverte a primeira e a segunda:"</span><span class="p">,</span><span class="n">y</span><span class="p">)</span>
<span class="n">z</span> <span class="o">=</span> <span class="n">y</span><span class="o">.</span><span class="n">inverte</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"E inverte a segunda e terceira setas:"</span><span class="p">,</span><span class="n">z</span><span class="p">)</span>
<span class="n">f</span> <span class="o">=</span> <span class="n">z</span><span class="o">.</span><span class="n">inverte</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span><span class="o">.</span><span class="n">inverte</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Façamos o inverso das duas inversões:"</span><span class="p">,</span><span class="n">f</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Os dois estados (o original e este que resulta de 4 acções) serão iguais?"</span><span class="p">,</span><span class="n">f</span><span class="o">==</span><span class="n">x</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Confirmemos mais uma vez que dois objectos diferentes com setas iguais, são iguais

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">EstadoSetas</span><span class="p">([</span><span class="s2">"d"</span><span class="p">,</span><span class="s2">"e"</span><span class="p">,</span><span class="s2">"d"</span><span class="p">,</span><span class="s2">"d"</span><span class="p">,</span><span class="s2">"d"</span><span class="p">,</span><span class="s2">"e"</span><span class="p">])</span> <span class="o">==</span> <span class="n">EstadoSetas</span><span class="p">([</span><span class="s2">"d"</span><span class="p">,</span><span class="s2">"e"</span><span class="p">,</span><span class="s2">"d"</span><span class="p">,</span><span class="s2">"d"</span><span class="p">,</span><span class="s2">"d"</span><span class="p">,</span><span class="s2">"e"</span><span class="p">])</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Vamos agora definir a classe do Problema que vai ser uma subclasse da classe **Problem**. Notem que não é preciso **_goal_test()_** nem **_path_cost()_**. Não precisamos do **_goal_test()_** porque apenas queremos verificar se um estado está na lista de estados finais, que o **_goal_test()_** herdado de **Problem** faz. Não precisamos do **_path_cost()_** porque cada acção custa mais 1.

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="kn">from</span> <span class="nn">searchPlus</span> <span class="k">import</span> <span class="o">*</span>

<span class="k">class</span> <span class="nc">ProblemaSetas</span><span class="p">(</span><span class="n">Problem</span><span class="p">)</span> <span class="p">:</span>

    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">initial</span> <span class="o">=</span> <span class="n">EstadoSetas</span><span class="p">([</span><span class="s2">"e"</span><span class="p">,</span><span class="s2">"e"</span><span class="p">,</span><span class="s2">"e"</span><span class="p">,</span><span class="s2">"d"</span><span class="p">,</span><span class="s2">"d"</span><span class="p">,</span><span class="s2">"d"</span><span class="p">]),</span><span class="n">goal</span><span class="o">=</span><span class="p">[</span><span class="n">EstadoSetas</span><span class="p">([</span><span class="s2">"e"</span><span class="p">,</span><span class="s2">"d"</span><span class="p">,</span><span class="s2">"e"</span><span class="p">,</span><span class="s2">"d"</span><span class="p">,</span><span class="s2">"e"</span><span class="p">,</span><span class="s2">"d"</span><span class="p">]),</span><span class="n">EstadoSetas</span><span class="p">([</span><span class="s2">"d"</span><span class="p">,</span><span class="s2">"e"</span><span class="p">,</span><span class="s2">"d"</span><span class="p">,</span><span class="s2">"e"</span><span class="p">,</span><span class="s2">"d"</span><span class="p">,</span><span class="s2">"e"</span><span class="p">])])</span> <span class="p">:</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">initial</span><span class="p">,</span><span class="n">goal</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">actions</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">estado</span><span class="p">)</span> <span class="p">:</span>
        <span class="sd">""" A acção 0 corresponde a inverter as setas de índices 0 e 1 da lista</span>
 <span class="sd">A acção 4 coorresponde a inverter as setas de índices 4 e 5, as últimas duas """</span>
        <span class="n">accoes</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">4</span><span class="p">,</span><span class="mi">5</span><span class="p">]</span>

        <span class="k">return</span> <span class="n">accoes</span>

    <span class="k">def</span> <span class="nf">result</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">estado</span><span class="p">,</span><span class="n">acao</span><span class="p">)</span> <span class="p">:</span>
        <span class="k">if</span> <span class="n">acao</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">actions</span><span class="p">(</span><span class="n">estado</span><span class="p">)</span> <span class="p">:</span>
          <span class="n">resultante</span> <span class="o">=</span> <span class="n">estado</span><span class="o">.</span><span class="n">inverte</span><span class="p">(</span><span class="n">acao</span><span class="p">)</span>
        <span class="k">else</span> <span class="p">:</span>
            <span class="k">raise</span> <span class="s2">"Há aqui qualquer coisa mal>> acao não reconhecida"</span>

        <span class="k">return</span> <span class="n">resultante</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">p</span> <span class="o">=</span> <span class="n">ProblemaSetas</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">initial</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Confirmemos que o **_goal_test()_** herdado esta a funcionar bem.

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">x</span> <span class="o">=</span> <span class="n">EstadoSetas</span><span class="p">([</span><span class="s1">'d'</span><span class="p">,</span><span class="s1">'e'</span><span class="p">,</span><span class="s1">'d'</span><span class="p">,</span><span class="s1">'e'</span><span class="p">,</span><span class="s1">'d'</span><span class="p">,</span><span class="s1">'e'</span><span class="p">])</span>
<span class="nb">print</span><span class="p">(</span><span class="n">x</span><span class="p">,</span><span class="s2">"satisfaz o objectivo?"</span><span class="p">,</span><span class="n">p</span><span class="o">.</span><span class="n">goal_test</span><span class="p">(</span><span class="n">x</span><span class="p">))</span>
<span class="n">y</span> <span class="o">=</span> <span class="n">EstadoSetas</span><span class="p">([</span><span class="s1">'d'</span><span class="p">,</span><span class="s1">'d'</span><span class="p">,</span><span class="s1">'d'</span><span class="p">,</span><span class="s1">'e'</span><span class="p">,</span><span class="s1">'d'</span><span class="p">,</span><span class="s1">'e'</span><span class="p">])</span>
<span class="nb">print</span><span class="p">(</span><span class="n">y</span><span class="p">,</span><span class="s2">"satisfaz o objectivo?"</span><span class="p">,</span><span class="n">p</span><span class="o">.</span><span class="n">goal_test</span><span class="p">(</span><span class="n">y</span><span class="p">))</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Quais as acções aplicáveis ao estado inicial?

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">p</span><span class="o">.</span><span class="n">actions</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">initial</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Apliquemos a acção 1 ao estado inicial

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">s1</span> <span class="o">=</span> <span class="n">p</span><span class="o">.</span><span class="n">result</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">initial</span><span class="p">,</span><span class="mi">1</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">s1</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Confirmemos que se voltarmos a aplicar a mesma acção regressamos ao estado inicial

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">s2</span> <span class="o">=</span> <span class="n">p</span><span class="o">.</span><span class="n">result</span><span class="p">(</span><span class="n">s1</span><span class="p">,</span><span class="mi">1</span><span class="p">)</span>
<span class="n">s2</span> <span class="o">==</span> <span class="n">p</span><span class="o">.</span><span class="n">initial</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Vamos agora aplicar as acções 1, 2, 3 e 4 sobre o estado inicial e verifiquemos se o estado resultante é final. Podemos começar logo com s2 que resulta da aplicação da inversão da primeira e segunda setas (1).

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">s3</span> <span class="o">=</span> <span class="n">p</span><span class="o">.</span><span class="n">result</span><span class="p">(</span><span class="n">s2</span><span class="p">,</span><span class="mi">2</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">s3</span><span class="p">)</span>
<span class="n">s4</span> <span class="o">=</span> <span class="n">p</span><span class="o">.</span><span class="n">result</span><span class="p">(</span><span class="n">s3</span><span class="p">,</span><span class="mi">3</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">s4</span><span class="p">)</span>
<span class="n">s5</span> <span class="o">=</span> <span class="n">p</span><span class="o">.</span><span class="n">result</span><span class="p">(</span><span class="n">s4</span><span class="p">,</span><span class="mi">4</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">s5</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Final?"</span><span class="p">,</span><span class="n">p</span><span class="o">.</span><span class="n">goal_test</span><span class="p">(</span><span class="n">s5</span><span class="p">))</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

#### Exercício 3[¶](#Exercício-3)

Extra: adapte o problema para qualquer número de setas.

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

#### Exercício 4[¶](#Exercício-4)

Supõe que tens um número arbitrário de moedas de 50, 20, 10, 5, 2 e 1 cêntimos, e que pretendes dar o troco no valor de N cêntimos, utilizando o menor número de moedas. Formula o problema em Python, seguindo o paradigma do Espaço de Estados e a plataforma aimas-python, de modo a poder resolver o problema de saber quais as moedas a utilizar para formar qualquer troco desejado.

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

#### Exercício 5[¶](#Exercício-5)

Resolva o problema da ordenação das panquecas. Dada uma pilha de panquecas de vários tamanhos, podem ordená-las de modo descrescente, com a maior em baixo e a mais pequena no topo? Vocês possuem uma espátula com a qual podem inverter as i panquecas do topo, sendo i maior do que 1 e menor ou igual ao número de panquecas. Podemos inverter as duas de topo, ou as 3 de topo, ..., ou todas. A figura em baixo ilustra o problema com uma espátula com i=3; no topo a espátula agarra 3 panquecas e no fundo aparecem invertidas:

![Drawing](https://upload.wikimedia.org/wikipedia/commons/0/0f/Pancake_sort_operation.png)

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

#### Exercício 6[¶](#Exercício-6)

Formule o problema das rãs e sapos saltitantes. Neste puzzle, o qual também pode ser um jogo para dois jogadores, temos uma linha formada por quadrados, com N quadrados à esquerda preenchidos com rãs azuis e N quadrados à direita preenchidos com sapos vermelhos, e um quadrado livre no meio. Os sapos só podem saltar para a esquerda e as rãs para a direita. As rãs podem deslocar-se para a direita para uma casa livre ou saltar sobre uma rã ou sapo, para uma casa livre à sua direita. Os sapos movem-se de forma análoga, mas para a esquerda. O objectivo é inverter a configuração inicial, tendo os sapos à esquerda, a casa livre e as rãs todas à direita. Na figura seguinte, N é igual a 2.

![](https://upload.wikimedia.org/wikipedia/commons/2/2f/ToadsAndFrogs.png)

</div>

</div>

</div>

</div>

</div>
