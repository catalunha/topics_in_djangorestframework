Comando importantes
Comando | Descrição | Saiba mais
---|---|---
git fetch |.| [123]
git checkout <branch_name> |.| [123]
git pull origin <branch_name>|.| [123]
git checkout -n <new_branch_name> |.| [123]
git add . |.|.
git commit -m '<comentarios do commit>' |.|.
git push origin <new_branch_name>|.|.


# [123] Texto importante
Fonte: https://pt.stackoverflow.com/questions/435213/criar-branch-local-a-partir-de-uma-branch-remota

Se o repositório remoto possui uma branch x1 (que você não possui localmente), primeiro você precisa puxar esta informação do repositório remoto. Você pode usar git pull, como sugeriu uma das respostas, mas este comando também vai atualizar sua branch atual, caso haja novos commits remotos que você ainda não possui localmente (por exemplo, se estou na master e faço git pull, a master será atualizada caso hajam novos commits na master do repositório remoto).

Se você só quer puxar branches e commits remotos, mas ainda não quer atualizar o seu repositório local, pode usar git fetch, que é o suficiente para puxar as informações da branch x1 remota.

Depois as outras respostas sugerem começar com git checkout x1. Isso não está errado, mas vai criar uma branch local também chamada x1, que por sua vez estará "rastreando" a branch remota x1.

Mas pense bem, se você quer criar uma outra branch xlocal baseado na branch remota x1, será que precisa criar também uma branch local x1 que só vai servir para criar o xlocal? Pois é isso que as outras respostas estão fazendo (não que seja errado, só que você terá uma branch local à toa, que não será usada para mais nada - assumindo que você quer fazer todo o trabalho em xlocal, pois acredito que seja este o motivo de criá-lo).

Sendo assim, você poderia simplesmente fazer:

git checkout -b xlocal origin/x1
Ou, a partir da versão 2.23.0 do Git (de 2019), você também pode usar o comando switch em vez do checkout:

git switch -c xlocal origin/x1
Assim eu digo que quero criar a branch xlocal, e que ela deve ser criada a partir da branch origin/x1 (ou seja, a branch x1 do repositório remoto). Aqui estou assumindo que o repositório remoto é o origin, claro (é possível ter vários repositórios remotos configurados, cada um com seu próprio nome).

Desta forma não é criado a branch local x1. E assim como indicou uma das respostas, na primeira vez que for feito o push você deve informar que a branch local está "rastreando" esta remota:

git push -u origin xlocal
Nas próximas vezes isso não será mais necessário, bastando fazer git push.