---
title: Algumas notas sobre o git + github
author:
  - J.João
  - Álvaro
---

# Filosofia geral

- Gestor de versões
- Repositório
- publico ou privado
- dono, colaboradores, outros

## Preparação

```
winget install --id Git.Git -e --source winget

scoop install git
scoop install gh
```

## Alguns comandos 

### Descarregar uma cópia

```
gh repo clone jjoao/AVD2425
gh auth login
gh repo view OWNER/REPO --web

git clone git@github.com:jjoao/AVD2425.git
```

### Buscar as novidades

carrega as novidades para a máquina local;

Na pasta do repositório:
```
git pull                   
```

###  Se for dono ou colaborador de um projecto

```
git add file.txt
git commit file.txt -m "transcrição da entrevista"

git push
```

### Novidades?

```
git log
```

## Perigo!!!

```
git remove file.txt
```

# Usando gh (cli para git hub)

```
scoop install gh
gh repo clone jjoao/AVD2425
gh auth login
gh repo view OWNER/REPO --web

```


# Outros

```
git diff

git config --global user.name "Your Name Comes Here"
git config --global user.email you@yourdomain.example.com
```
