requerimentos:
	eclipse + pydev
	python 3.4 + pyocr + django
clonar o repositório (sem importar projeto)
clicar com o botão direito em cima do repositorio clonado
selecionar import projects
marcar "import as general project"
clique em 'next'
em project name digite o nome do projeto
clique em finish
mude a perspectiva para pydev
clique com o botão direito em cima do projeto criado
selecionar pydev > set As pydev project
selecionar pydev > set as django project
clique com o botão direito sobre a pasta src do projeto criado e seleone pydev > set as source folder(..)
clique com o botão direito em cima do projeto criado selecione propierties
na guia pydev - interpreter/grammer,
	mude para grammer 3.0
	mude interpreter para o interpretador que possui as dependencias do projeto intaladas
na guia pydev - DJango
	em django manage.py digite "src/manage.py" sem aspas
	em django settings module digite "es2_aproject.settings" sem aspas
clique em ok
clique com o botão direito sobre o projeto, selecione run as > pydev: django
projeto baixado e configurado com sucesso.