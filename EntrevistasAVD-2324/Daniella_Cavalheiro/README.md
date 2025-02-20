## README do Projeto "UM Sombra" - Entrevista com o Professor Mário Farelo

Este é o README específico para a entrevista realizada com o Professor Mário Farelo, como parte do projeto "UM Sombra". Abaixo, estão os detalhes sobre a entrevista, os desafios enfrentados durante a transcrição e extração dos metadados, bem como informações sobre a organização do conteúdo.

# Entrevista
A entrevista foi conduzida e transcrita por Daniella Cavalheiro. Você pode acessar a primeira transcrição com o áudio da entrevista no seguinte link:
https://app.meetgeek.ai/meeting/f10dd912-ccf4-48ba-afe5-00d92237f5b8
Também incluí no diretório o arquivo txt da primeira transcrição (1a_Transcrição_Entrevista _Prof_Mario_Farelo_MeetGeek.txt) com o MeetGeek.ai. Houve uma taxa de acerto de cerca de 90% com utlização dessa AI.

# Desafios Enfrentados

Durante o processo de transcrição e extração dos metadados, foram enfrentados os seguintes desafios:

Em um trecho da transcrição não era possível compreender o que o entrevistado dizia (minuto 9:30). O meet Geek identificou como 'téocientes de saber'. Enviei email para o entrevistado que não respondeu sobre a palavra em questão, mas 'editou' a resposta sem comentar a palavra. Então tentei usar outra AI para verificar a acurácia da transcrição (Transcrição_Entrevista_Prof_Mario_Farelo_TurboScribe.txt) e ela identificou 'até os centros de saber', mas errou em alguns outros trechos, tendo a mesma taxa de acerto de cerca de 90%.
Quando da extração dos metadados os códigos extrtaiam quase que a totalidade das etiquetas solicitadas, mas algumas delas foram incluídas ao final, por exemplo 'Minho', quando não fazia parte da 'Universidade do Minho'.
Para criação dos codes utilizei basicamente duas intligências artificiais para me auxiliar (chatGPT e CoPilot).

Estrutura e funcionalidade geral dos códigos utilizados: O primeiro código utilizado (Extract_Meta_Interview_Prof_Farelo_Data.py) é mais simples, focado na extração básica de informações da entrevista e salvamento em Markdown, o mesmo código que utilizei para extrair metadados do UMDicas. Já o segundo código (Extract_Meta_Interview_Prof_Farelo_Data.py) é mais complexo, realizando tarefas adicionais como etiquetagem de entidades e categorização de perguntas e respostas. Reutilizei boa parte do primeiro código e adicionei a função extract_interview_content no segundo código porque estava mal definida.

Manipulação de exceções: O segundo código possui uma estrutura mais robusta para manipular exceções, utilizando um bloco try-except para lidar com erros durante a leitura do arquivo.

Nomenclatura e organização: O segundo código utiliza nomes de variáveis mais descritivos e uma função main() para melhorar a organização e compreensão do código.

Funcionalidades adicionais: O segundo código adiciona funcionalidades como etiquetagem de entidades e categorização de perguntas e respostas, não presentes no primeiro código.

# Processo de Organização
O processo de organização do conteúdo da entrevista incluiu as seguintes etapas:

Transcrição Bruta: Inicialmente, foi realizada a transcrição completa da entrevista.

Edição e Refinamento: A transcrição foi editada para remover partes desnecessárias, inserir pontuação e criar parágrafos.
    Oralidade Escrita e Tags de Metadados: Adaptação da oralidade para a escrita e identificação apropriada das tags de metadados.
    Edição: Necessidade de editar a transcrição para melhorar a legibilidade e organização do texto.
    Criação de Parágrafos: Estruturação do texto em parágrafos perguntas e respostas.
    Inserção de Pontuação: Adição de pontuação para melhorar a fluidez do texto.
    Melhoria da Legibilidade: Foram feitos ajustes para tornar a transcrição mais fácil de ler e compreender.
    Inclusão de Títulos de Seção: Quando apropriado, foram adicionados títulos de seção para organizar o conteúdo (perguntas e repostas).
    
Editoração: Fiz a editoração da entrevista no Canva.com 

Finalização: A transcrição final foi preparada para inclusão no projeto "UM Sombra" e para criação de um livro no Issuu a ser entregue ao entrevistado.


# Link para áudio da Entrevista e 1a transcrição
https://app.meetgeek.ai/meeting/f10dd912-ccf4-48ba-afe5-00d92237f5b8 (Link da 1a transcrição - Meet Geek)


# Link para a Entrevista editorada
https://www.canva.com/design/DAGB0eHJjRY/hOMaeJoUVIZEamYpPA_3jA/view?utm_content=DAGB0eHJjRY&utm_campaign=designshare&utm_medium=link&utm_source=editor


# Link para o livro com a publicação da entrevista
https://issuu.com/danimcav/docs/entrevista_professor_mario_farelo_f_7be33718c95ddd

# Arquivos adicionados ao diretório

Perguntas Entrevista Professor Mário Farelo por Daniella Monteiro Cavalheiro.pdf (Preparação das perguntas para entrevista)


1a_Transcrição_Entrevista _Prof_Mario_Farelo_MeetGeek.txt (1a transcrição por AI)


Transcrição_Entrevista_Prof_Mario_Farelo_TurboScribe.txt (2a transcrição por AI)


Entrevista Professor Mario Farelo_Final_copy_and_paste.txt (1a limpeza)


Entrevista_Professor_Mario_Farelo_por_Daniella_Monteiro_Cavalheiro_Editado.txt (Arquivo editado para ser editorado em formato revista)

Entrevista Professor Mario Farelo_FINAL_VERSION (arquivo em pdf da entrevista editorada para ser transformada em livro)


Extract_Meta_Interview_Prof_Farelo.py (1a tentativa de extrtação de Metadados)

Interview_Prof_Farelo.md (escuta do code acima)


Extract_Meta_Interview_Prof_Farelo_Data.py (extração dos metadados)

Entrevista_Professor_Mario_Farelo_Metadata.md (escuta do code acima)


Entrevista_Professor_Mario_Farelo_Metadata.md (escuta do code Extract_Meta_Interview_Prof_Farelo_Data.py)

Entrevista_Professor_Mario_Farelo_Metadata_Final.md (adição manual de etiquetas que o code não leu. Arquivo md final)


Mais informações e atualizações sobre o progresso do projeto serão adicionadas conforme necessário.

