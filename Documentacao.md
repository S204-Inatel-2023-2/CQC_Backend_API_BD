\# Documentação da API

\## Visão Geral

A API foi desenvolvida para gerenciar cadastros de usuários e eventos no sistema EventNow.

\## Endpoints

\### 1. Página Inicial

- \*\*Descrição:\*\* Retorna uma mensagem para indicar que o servidor está funcionando corretamente.
- \*\*URL:\*\* `/`
- \*\*Método HTTP:\*\* GET

\#### Respostas

- \*\*Sucesso (200 - OK):\*\* Retorna uma mensagem de sucesso.

Exemplo de resposta:

\```json

{

"status": 200,

"message": "ok"

}

\```

\### 2. Login de Usuário

- \*\*Descrição:\*\* Autentica um usuário no sistema.
- \*\*URL:\*\* `/login`
- \*\*Método HTTP:\*\* POST

\#### Parâmetros da Solicitação

| Parâmetro | Tipo   | Descrição                   |

\|-----------|--------|-----------------------------|

| email     | string | Endereço de e-mail do usuário|

| senha     | string | Senha para a conta do usuário|

\#### Respostas

- \*\*Sucesso (200 - OK):\*\* Retorna uma mensagem de sucesso e o ID do usuário autenticado.

Exemplo de resposta:

\```json

{

"mensagem": "Login bem-sucedido",

"user\_id": "id\_do\_usuario"

}

\```

- \*\*Erro (401 - Não Autorizado):\*\* Retorna uma mensagem de credenciais inválidas se a autenticação falhar.

Exemplo de resposta:

\```json

{

"mensagem": "Credenciais inválidas",

"user\_id": null

}

\```

\### 3. Adicionar Usuário ao Evento

- \*\*Descrição:\*\* Adiciona um usuário a um evento específico.
- \*\*URL:\*\* `/add-user-event`
- \*\*Método HTTP:\*\* POST

\#### Parâmetros da Solicitação


| Chave    | Tipo   | Descrição           |

\|----------|--------|---------------------|

| usuario  | string | Nome do usuário     |

| evento   | string | Nome do evento      |

\#### Respostas

- \*\*Sucesso (200 - OK):\*\* Retorna uma mensagem de sucesso após adicionar o usuário ao evento.

Exemplo de resposta:

\```json

{

"mensagem": "Usuário inserido com sucesso no evento"

}

\```

- \*\*Erro (400 - Solicitação Inválida):\*\* Retorna uma mensagem de erro se o formato dos dados enviados for inválido.

Exemplo de resposta:

\```json

{

"mensagem": "Formato de dados inválido"

}

\```

\### 4. Deletar Usuário

- \*\*Descrição:\*\* Remove um usuário do sistema.
- \*\*URL:\*\* `/delete\_usuario/<string:nome>`
- \*\*Método HTTP:\*\* DELETE

\#### Respostas

- \*\*Sucesso (200 - OK):\*\* Retorna uma mensagem de sucesso após remover o usuário.

Exemplo de resposta:

\```json

{

"mensagem": "Usuário removido com sucesso"

}

\```

- \*\*Erro (500 - Erro Interno do Servidor):\*\* Retorna uma mensagem de erro se ocorrer um problema durante a remoção.

Exemplo de resposta:

\```json

{

"mensagem": "Erro ao processar solicitação",

"error": "Descrição do erro"

}

\```

\### 5. Deletar Evento

- \*\*Descrição:\*\* Remove um evento do sistema.
- \*\*URL:\*\* `/delete\_evento/<string:nome>`
- \*\*Método HTTP:\*\* DELETE

\#### Respostas

- \*\*Sucesso (200 - OK):\*\* Retorna uma mensagem de sucesso após remover o evento.

Exemplo de resposta:

\```json

{

"mensagem": "Evento removido com sucesso"

}

\```

- \*\*Erro (500 - Erro Interno do Servidor):\*\* Retorna uma mensagem de erro se ocorrer um problema durante a remoção.

Exemplo de resposta:

\```json

{

"mensagem": "Erro ao processar solicitação",

"error": "Descrição do erro"

}

\```

\### 6. Cadastro de Evento

- \*\*Descrição:\*\* Cadastra um novo evento no sistema.
- \*\*URL:\*\* `/cadastroevento`
- \*\*Método HTTP:\*\* POST

\#### Parâmetros da Solicitação


| Chave        | Tipo   | Descrição           |

\|--------------|--------|---------------------|

| nome         | string | Nome do evento      |

| local        | string | Local do evento     |

| administrador| string | Administrador do evento|

\#### Respostas

- \*\*Sucesso (200 - OK):\*\* Retorna uma mensagem de sucesso após cadastrar o evento.

Exemplo de resposta:

\```json

{

"mensagem": "Evento cadastrado com sucesso"

}

\```

- \*\*Erro (400 - Solicitação Inválida):\*\* Retorna uma mensagem de erro se o formato dos dados enviados for inválido.

Exemplo de resposta:

\```json

{

"mensagem": "Formato de dados inválido"

}

\```

\### 7. Cadastro de Usuário

- \*\*Descrição:\*\* Cadastra um novo usuário no sistema.
- \*\*URL:\*\* `/cadastro`
- \*\*Método HTTP:\*\* POST

\#### Parâmetros da Solicitação


| Chave | Tipo   | Descrição           |

\|-------|--------|---------------------|

| nome  | string | Nome do usuário     |

| email | string | Endereço de e-mail  |

| senha | string | Senha do usuário    |

\#### Respostas

- \*\*Sucesso (200 - OK):\*\* Retorna uma mensagem de sucesso após cadastrar o usuário.

Exemplo de resposta:

\```json

{

"mensagem": "Usuário cadastrado com sucesso"

}

\```

- \*\*Erro (400 - Solicitação Inválida):\*\* Retorna uma mensagem de erro se o formato dos dados enviados for inválido.

Exemplo de resposta:

\```json

{

"mensagem": "Formato de dados inválido"

}

\```

\---


\## Exemplo de Uso em Python

Como utilizar a API em Python usando a biblioteca `requests`:

\```python

import requests

url = 'http://localhost:5000/cadastro'

\# Dados do usuário a serem enviados

data = {

"nome": "NomeExemplo",

"email": "exemplo@email.com",

"senha": "senhadousuario"

}

\# Enviar solicitação POST

response = requests.post(url, json=data)

\# Exibir resposta da API

print(response.json())

\# Observação

Certifique-se de enviar os dados corretamente no formato JSON para o endpoint /cadastro.
