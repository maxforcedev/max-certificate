# 🎓 Certificados - Plataforma de Emissão e Validação

Sistema completo para **emissão, validação e visualização de certificados online**, voltado para cursos livres e treinamentos. Permite que usuários validem seus certificados com segurança, e que administradores os gerem com facilidade.

🔗 **Demo**: [certificados.maxforcedev.com.br](https://certificados.maxforcedev.com.br)

---

## 🚀 Status do Projeto

✅ Funcional – versão MVP em produção

---

## 📚 Funcionalidades

- ✅ Emissão de certificados com nome, curso, carga horária, data e competências
- ✅ Geração automática de código único para cada certificado
- ✅ Validação pública via código ou e-mail
- ✅ Tela “Meus Certificados” com autenticação via e-mail + código de verificação
- ✅ Visualização do certificado em HTML
- ✅ Download do certificado em PDF
- ✅ Painel administrativo básico para gestão
- ✅ Integração com frontend em Next.js
- ⬜ Multiplas instituições e suporte multi-tenant (planejado)
- ⬜ Relatórios de emissão (planejado)
- ⬜ Edição de certificados já emitidos (planejado)

---

## 🧠 Tecnologias Utilizadas

### Backend
- Python 3.12
- Django 5.x
- Django Rest Framework
- WeasyPrint (PDF)
- PostgreSQL
- Docker + Docker Compose

### Frontend
- Next.js (App Router)
- Tailwind CSS
- shadcn/ui
- React Hook Form + Zod
- SSR com `next start`

### DevOps
- EasyPanel (produção)
- NGINX com proxy reverso
- Cloudflare Tunnel (dev)

---

## 📦 Como Rodar Localmente

1. Clone o repositório
2. Configure o `.env` baseado no `.env.example`
3. Rode com Docker:

```bash
docker-compose up --build
```

4. Acesse:
- Backend: http://localhost:8000/api/
- Frontend: http://localhost:3000/

---

## 🧾 Estrutura Básica do Certificado

Cada certificado contém:
- Nome completo do participante
- Nome do curso
- Carga horária
- Data de emissão
- Competências adquiridas
- Código único do certificado (ID público)
- Versão em HTML + PDF gerado

---

## 🧭 Roadmap

- [ ] Upload em lote de certificados via planilha
- [ ] Módulo multi-institucional
- [ ] Histórico de visualizações
- [ ] Exportação de dados para CSV

---

## 📄 Licença

Projeto pessoal para fins educacionais e demonstração profissional
