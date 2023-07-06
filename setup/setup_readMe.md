### STEP DA ESEGUIRE PER AVVIARE SCRIPT:

- Creare un virtual enviroment (se non se ne ha già uno) con il comando:
            
        python -m venv "nome_venv"

- Successivamente posizionarsi all'interno del venv al path \Scripts
  ed eseguire lo script activate.bat (per stoppare il virtual enviroment nello stesso path eseguire
  lo script deactivate.bat);

- Dopo aver creato il virtual enviroment installare le librerie riportate nel file 'setup/requirements.txt'
  con il comando (posizionandosi nella directory di progetto 'setup'):

        pip install -r requirements.txt

  File prodotto con il comando "pip freeze > requirements.txt" https://note.nkmk.me/en/python-pip-install-requirements/
  
