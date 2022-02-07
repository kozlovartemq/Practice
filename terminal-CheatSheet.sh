	;ОБНОВЛЕНИЕ
apt-get update
apt-get upgrade

	;ЧИСТКА
apt-get clean
apt-get autoremove

;shift+ctrl+C  = Копировать в Терминале
;ctrl+C        = Отмена действия

|  = pipes (pipelines) the standard output (stdout) of one command into the standard input of another one. Note that stderr still goes into its default destination, whatever that happen to be.
|& = pipes both stdout and stderr of one command into the standard input of another one. Very useful, available in bash version 4 and above.
&& = executes the right-hand command of && only if the previous one succeeded.
|| = executes the right-hand command of || only it the previous one failed.
;  = executes the right-hand command of ; always regardless whether the previous command succeeded or failed. Unless set -e was previously invoked, which causes bash to fail on an error.

tee  = считывает ввод и одновременно выводит его в стандартный вывод (консоль) и в файл
       ls | tee file.txt file2.txt | grep "py" = в file и file2.txt будет вывод ls, этот вывод будет вводом для grep
       ls | tee -a file = -a - дозаписать файл

    ;КОМАНДЫ В ТЕРМИНАЛЕ
xrandr --output Virtual1 --mode 1360x768    = сменить разрешение экрана
sudo systemctl restart NetworkManager       = перезапустить NetworkManager при изменениях в /etc/NetworkManager/NetworkManager.conf

ip a               = показать сетевые подключения
ifconfig
iwconfig           = показать беспроводные подключения
ping IP            = пропинговать ip -c = кол-во пакетов;
                                     -i = задержка между пакетами
сurl               = проверить ответ от сервера (GET по умолчанию) -X = выбрать метод;
                                                                   --data "key=value" = задать параметры
arp -a             = работа с ARP таблицей
route              = таблица маршрутизации
netstat -ano       = показывает открытые порты                                                  
                                                     
./file	           = запустить файл
doublecmd          = Double Commander
filezilla          = FTP manager
leafpad filename   = открыть файл в графическом текстовом редакоторе
kate               = вызвать файл (если установлено)
nano filename      = создать и/или открыть файл внутри терминала (ctrl+o =save; ctrl+x =quit)

ssh remote_user@remote_host  (ssh -i sshkey_file.private user@host -p port = подключиться использованием приватного ключа )
                              ssh user@host -p port "bash --noprofile --norc" = игнорировать .bashrc файл, если он закрывает ssh соединение

nc = NetCat - для чтения и записи данных через сетевые подключения TCP/UDP ( nc [options] host port ) -u = UDP
                                                                                                      -z -v = сканирование открытых портов(z) с подробной инфой(v)
                                                                                                      nc -l port > filename = открыть порт для входящего соединения, записать в файл
                                                                                                      nc host port < file_name = отпрапвить файл прослушиваемому хосту
nmap                = проверить открытые порты
openssl             = криптографическая библиотека ( openssl s_client -connect host:port = подключиться, используя ssl шифрование )
adduser             = добавить пользователя
exit                = выйти из текущего пользователя/выйти из ssh
su username         = залогиниться в терминале ("su -" - login as root)
whoami              = показать имя текущего пользователя (полезно при --norc в ssh)
scp                 = перенос файлов между (сетевыми)пользователями- что?-куда? (scp localfile user@host:/home/fortor/Desktop)

history             = показать историю введенных команд (history | grep ping - что пинговали?)  
clear               = очистить терминал
cd                  = смена директории (cd .. - подняться на уровень вверх, cd - перейти в /home)
ls                  = показать список файлов в текущей или в заданной директории (ls -la = l -в таблицу; a -показать скрытые файлы)
pwd                 = показать текущую директорию
cp                  = копировать (cp -v что куда(путь)); -v = визуализировать результат
mv                  = переместить(переименовать) - (mv -v что куда)
touch               = создать файл(ы) - touch  file1 /home/file2 /var/file3
mkdir               = создать папку(директорию)
rm                  = удалить без возможности восстановления (rm -r Name) ; -r -удалить папку и все ее содержимое
rmdir               = удалить пустую директорию
cat                 = вывести внутренности файла в терминал
less                = вывести внутренности файла в новой вкладке терминала (q = quit)
du                  = узнать размер файлов/директории ( du * -a -b | sort -nk1 | grep 33 )     -b = показать размер в байтах
                                                                                               -a = показать все файлы и директории внутри
sort = вывод текстовых строк в определенном порядке. -r = в обратном порядке
                                                     -k = номер колонки справа-налево -k1 
                                                     -nk = номер колонки слева-направо -nk1
                                                     -u = удалить дубликаты
uniq = для поиска одинаковых строк. Сравнение с предыдущей строкой (нужен sort, чтобы искать в файле ( cat file | sort | uniq -u = найти ункальные строки ))
       options file-to-read file-to-write                                                                                     -c = добавить в строку кол-во ее повторений
                                                                                                                              -i = игнорировать регистр
diff = показать отличия между файлами
grep = фильтр (cat /etc/apt/source.list | grep -i src) = выведет только строки, где есть 'src' (-i = игнорировать регистр, 
                                                                                                -v = исключить строки,
                                                                                                -с = кол-во найденных строк)
find = найти файл/директорию - где(.)-текущ.дир. что(-name) (find . -name "*.txt" | find . -type d -name "folder" -delete -print) 
                                                                                                -type d = поиск директории
                                                                                                -delete = удалить найденное
                                                                                                -print = вывести в терминал
echo = эхо в теринал. Можно перезаписывать текстовые файлы/значения/имена - echo "text" > file.txt (> = перезаписать файл;
                                                                                                    >> = дозаписать файл)
tr = для замены, удаления символов (tr ключ набор1 набор2) tr x y = заменить x на y
                                                           tr -d [:lower] = удалить буквы в нижнем регистре
                                                           tr 'A-Za-z' 'N-ZA-Mn-za-m' < data.txt = Rotate13 - сдвинуть символы на 13 по алфавиту
chown = менять владельца файла (chown root:root filname = имя_пользователя:группа_пользователя)
chmod = менять права на файл (сделать созданный скрипт *.sh исполняемым файлом)= chmod +x file.sh ;(+x -исполняемый; 
                                                                                                    +w -для правки;
                                                                                                    +r-для чтения;
                                                                                                    777-глобальный режим (все всем можно))
man                     = показать объемную помощь (man pwd)
--help                  = показать компактную помощь по любой команде (mw --help)

fdisk                   = показать все физические диски
mount                   = присоединить раздел к файловой системе (mount dev/sda1 mnt/cdrom)=что и куда
umount                  = ОБЯЗАТЕЛЬНО перед тем, как вытащить флешку (umount mnt/cdrom)
lsusb                   = посмотреть подключенные usb устройства 
ps aux                  = вывести действующие процессы в терминал
top                     = отслеживать действующие процессы в реальном времени
kill PID                = завершить процесс
ln -s failname linkname = создать символьную ссылку на директорию/файл (ярлык)
updatedb                = обновить (для locate)
locate filename         = показать путь до файла (-i -игнорировать регистр)
xxd                     = create a Hexdump of a file ( xxd -r file  = reverse)
base64                  = работа с кодировкой base64. -i = игнорировать символы не из алфавита
                                                      -d = decode
screen = разделить терминал на несколько процессов (управление ctrl+A и " или w = список созданных окон
                                                                      и c = создать новое окно
                                                                      и номер = переход на определенное окно
                                                                      и ? = справка)

; Compression (сжатие, архивирование)
tar ( tar -xvf = decompress)
gzip ( gzip -d = decompress)
bzip2 ( bzip -d = decompress)


