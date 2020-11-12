import subprocess
import os.path

#ip = input('Ingresa la ip a escanear')   #Reemplazar por path con txt de ip's
#passwd = input('Ingresa password de administrador: ')
#subprocess.run('sudo su', shell=True)
#subprocess.run(str(passwd), shell=True)


list_path = input('set .txt file route: ')
true_path = os.path.isfile(list_path)   #Comprueba que existe el archivo .txt

if true_path == True:
    ls = open(str(list_path), 'r')
    lines = ls.read().splitlines()       
    for ip in lines:
        ip_to_scan = 'ipinfo.io/'+ str(ip)
        scan = subprocess.check_output(['curl', str(ip_to_scan)])
        new_list = open('mod_list', 'a')
        mod_new_list = new_list.write('%s\n %s' %(ip, scan))

	
else:
    print('Wrong path...')