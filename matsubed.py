# -*- coding: utf-8 -*-

import string
from ctypes import windll
import os
import shutil
import sys
import os
from urlparse import urlparse

LIBRARY_DIR_PATH = "..\\library\\"
MATSUBED_BLINK_URL = "https://developer.mbed.org/users/hardtail/code/MATSU-bed_blinky/"
mbed_sdk_tools_url = 'https://mbed.org/users/mbed_official/code/mbed-sdk-tools'

def mbed_sdk_deploy():
    os.system("mkdir .temp")
    os.system("hg clone "+ mbed_sdk_tools_url + " .temp\\tools")

def check_setting():
    if not os.path.exists(".mbed"):
        f = open(".mbed", "w")
        f.write('ROOT=.\n')
        f.close()


    f = open(".mbed")
    date = f.read()
    f.close()

    if not "TARGET=LPC1549" in date.split("\n"):
        ## ターゲットをLPC1549に設定
        os.system("mbed target  LPC1549")

    if not "TOOLCHAIN=GCC_ARM" in date.split("\n"):
        ## ツールチェインをGCC_ARMに設定        
        os.system("mbed toolchain  GCC_ARM")


def isURL(url):
    o = urlparse(url)
    return len(o.scheme) > 0

def get_library_list():
    library_list = []

    if os.path.exists(LIBRARY_DIR_PATH):
        for x in os.listdir(LIBRARY_DIR_PATH):  
                if os.path.isdir(LIBRARY_DIR_PATH + x):
                    library_list.append(x)
    else:
        for x in os.listdir("library\\"):  
                if os.path.isdir("library\\" + x):
                    library_list.append(x)

    if len(library_list) != 0:
        if ".temp" in library_list:
            library_list.remove(".temp")
        if ".git" in library_list:
            library_list.remove(".git")
        if "BUILD" in library_list:
            library_list.remove("BUILD")
    else:
        print "library directory not found"

    return library_list

def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1
    return drives

def chack_binfile():
    ## プロジェクト名とbinファイルの位置を確認
    projectName = os.getcwd().split("\\")[-1]
    binfile = os.getcwd()+"\\BUILD\\LPC1549\\GCC_ARM\\"+projectName+".bin"
    ## ファイルがあればパスを返す
    if os.path.exists(binfile):
        return binfile

    return None

def format():
    # ディスクドライブの一覧を取得
    for drive in get_drives():
        # .binだけが入ってるドライブを見つける
        # .binファイルが1つだけ入っていたらMATSU-bed
        # binfile = os.listdir(drive+":/")[0]
        if (len(os.listdir(drive+":/"))==1) and (os.listdir(drive+":/")[0].split(".")[-1]=="bin"):
            #print "Find MATSU-BED!!"
            os.remove(drive+":/"+os.listdir(drive+":/")[0])
            return True

    return False
            
def write():
    # コマンドが実行されたフォルダからプロジェクト名を取得
    projectName = os.getcwd().split("\\")[-1]
    # フォーマット済みであることを確認
    # 何も入っていないドライブを探す
    for drive in get_drives():
        if len(os.listdir(drive+":/"))==0:
            if chack_binfile() is not None:
                shutil.copy(chack_binfile(), drive+":/")
                return True
    print "bin file is not found"
    return False

def flash():
    if chack_binfile() is None:
        print 'bin file is not found'
        return 0

    if format() == False:
        print 'Not found MATSU-bed'
        print 'Please connect MATSU-bed and enter USB-ISP mode'
        return 0

    if write() == True:
        print 'Success firmware update !!!'

def new(projectName):
    cmd = 'mbed new '

    ## mbed os 2でプロジェクトを作る
    ## ライブラリはダウンロードせずにlibraryフォルダ内からシンボリックリンクを張る
    cmd = cmd + projectName +" --mbedlib --create-only"
    os.system(cmd)

    os.chdir(projectName)

    ## ターゲットをLPC1549に設定
    ## ツールチェインをGCC_ARMに設定
    check_setting()

    os.system("mklink /D mbed ..\library\mbed")
    os.system("mklink /D USBDevice ..\library\USBDevice")

    ## libraryフォルダからmain.cppをコピーしてくる
    shutil.copy(LIBRARY_DIR_PATH+"main.cpp", ".\\")

def add(url_or_libName):
    cmd = 'mbed'
    if isURL(url_or_libName):
        libName = url_or_libName.split("/")[-1]
        if libName =="":
            libName = url_or_libName.split("/")[-2]

        ## libraryフォルダにインポート
        ## そこからシンボリックリンクを張る
        cmd = cmd + " add " + url_or_libName + " " + LIBRARY_DIR_PATH +libName
        os.system(cmd)

        os.system("mklink /D " + libName + " " + LIBRARY_DIR_PATH + libName)

    else:
        libName = url_or_libName

        ## libraryフォルダからライブラリのあるフォルダを抽出
        library_list = get_library_list()

        ## 目的のライブラリがあったらシンボリックリンクを張る
        if libName in library_list:
            print "mbed library ["+libName +"] was imported from library Directory in workspace"
            os.system("mklink /D " + libName + " " + LIBRARY_DIR_PATH + libName)
        else:
            print "mbed library ["+libName +"] is not found"
            print "Please import using web URL"
            print "e.g.) matsubed import https://developer.mbed.org/users/hardtail/code/"+libName

def project_import(URL,import_name = None):
    projectURL = URL

    projectName = ""

    if import_name is not None:
        projectName = import_name
    else:
        projectName = projectURL.split("/")[-1]
        if projectName =="":
            projectName = projectURL.split("/")[-2]

    ## hgコマンドでmain関連のコードだけ落としてくる
    os.system("hg clone "+ projectURL+ " " + projectName)
    
    os.chdir(projectName)
    project_dir_path = os.getcwd()

    ## とりあえずmbedライブラリのリングを張る
    os.system("mklink /D mbed ..\library\mbed")

    ## mbed sdk 2.0をデプロイ
    mbed_sdk_deploy()


    ## ライブラリを精査して無いものはlibraryディレクトリに落としてシンボリックリンクを張る
    library_list = get_library_list()
    Request_library_list = []

    ## 要求されてるライブラリを調べる
    for x in os.listdir(project_dir_path):
        if os.path.isfile(project_dir_path +"\\"+ x) and os.path.splitext(x)[-1] == '.lib':
            Request_library_list.append(os.path.splitext(x)[0])

    for Req_library in Request_library_list:
        ## すでにあるはaddコマンドでシンボリックリンク
        if  Req_library in library_list:
            add(Req_library)

        ## 無いものはlibraryに落としてからシンボリックリンク
        else:
            f = open(Req_library+".lib")
            Req_library_URL = f.read()
            f.close()

            Req_library_URL = Req_library_URL.split("#")[:1][0]
            add(Req_library_URL)

def init():
    ## MATSU-bed_blinkyをlibraryとしてインポート
    os.system("hg clone "+ MATSUBED_BLINK_URL + " library")

    ## libraryフォルダに移動してmbedライブラリをデプロイ
    os.chdir("library")
    os.system("mbed deploy")


def main():
    args = sys.argv
    
    args = args[1:]
    cmd = 'mbed'

    for arg in args:
        cmd = cmd + " " + arg

    ## サブコマンド flash
    if args[0] == "flash":
        flash()
        return 0

    ## サブコマンド init
    if args[0] == "init":
        init()
        return 0

    ## サブコマンド new
    if args[0] == "new":
        new(args[1])
        return 0

    ## サブコマンド　compile
    if args[0] == "compile":
        check_setting()

    ## library-list
    if args[0] == "library":
        library_list =get_library_list()

        print "List of libraries being downloaded"
        for x in library_list:
            print "   " + x
        return 0

    ## サブコマンド import 
    if args[0] == "import":
        if len(args) > 2:
            project_import(args[1], args[2])
        else:
            project_import(args[1])
        return 0


    ## サブコマンド add
    ## ライブラリ追加用のコマンド
    if args[0] == "add":
        add(args[1])
        return 0    

    os.system(cmd)
    


if __name__ == '__main__':
    main()