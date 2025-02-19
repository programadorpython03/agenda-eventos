# API de Links de Eventos

Uma API RESTful construída com Flask para gerenciamento de links de eventos.

## Descrição

Esta API fornece endpoints para criar, ler, atualizar e deletar links de eventos, seguindo os princípios REST e padrões de arquitetura limpa.

## Tecnologias Utilizadas

- Python
- Flask
- Blueprint

## Endpoints da API

### Links de Eventos

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/events_links` | Criar um novo link de evento |
| GET | `/events_links/<event_id>` | Buscar links de evento por ID |
| PUT | `/events_links/<event_id>` | Atualizar um link de evento |
| DELETE | `/events_links/<event_id>` | Deletar um link de evento |

## Estrutura do Projeto 

rc/
├── main/
│ └── routes/
│ └── events_links_route.py
├── controllers/
│ └── events_link_controller/
│ ├── events_link_creator.py
│ └── events_link_manager.py
├── models/
│ └── repositories/
│ └── events_links_repository.py
└── http_types/
└── http_request.py

## Instalação

1. Clone o repositório:
```
git clone <url-do-repositorio>
```

2. Instale as dependências:
```
pip install -r requirements.txt
```

## Como Usar

1. Inicie o servidor:
```
python run.py
```

2. A API estará disponível em `http://localhost:5000`

## Exemplos de Uso da API

### Criar Link de Evento
```
curl -X POST http://localhost:5000/events_links \
  -H "Content-Type: application/json" \
  -d '{"seus_dados": "aqui"}'
```

### Buscar Links de Evento
```
curl -X GET http://localhost:5000/events_links/<event_id>
```

### Atualizar Link de Evento
```
curl -X PUT http://localhost:5000/events_links/<event_id> \
  -H "Content-Type: application/json" \
  -d '{"seus_dados": "aqui"}'
```

### Deletar Link de Evento
```
curl -X DELETE http://localhost:5000/events_links/<event_id>
```

## Como Contribuir

1. Faça um fork do repositório
2. Crie sua branch de feature (`git checkout -b feature/nova-funcionalidade`)
3. Faça commit das suas alterações (`git commit -m 'Adiciona nova funcionalidade'`)
4. Faça push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.