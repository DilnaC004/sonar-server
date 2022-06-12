# sonar-server

vytvoření virtuálního prostředí a jeho spuštění:

```bash
virtualenv venv
source venv/bin/activate
```

instalace potřebných balíčků :

```bash
pip3 install -r requirements.txt
```

## Nastaveni crontabu :

Automatické spustění serveru a průběžná kontrola jeho běhu

```bash
crontab -e

#vložení řádku - testování běhu skriptu každou minutu
*/1 * * * * pgrep SonarServer > /dev/null || cd ~/Repos/sonar-server && source venv/bin/activate && python3 app.py
```
