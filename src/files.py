import os,sys,re

def get_files_path():
    BASIC_DIRS=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(BASIC_DIRS)
    tmp=os.path.join(BASIC_DIRS,'src\plugins')
    dict = {}
    for root,dirs,files in os.walk(tmp):
        for file in files:
            absPath = os.path.join(root,file)
            if absPath.split('.')[-1] =='py':
                Str = os.path.join(root, file)
                Path1 = re.findall(r'src.+\.py',Str)[0]
                path1 = Path1.split('.')[0]
                if path1.split('\\')[-1] !='__init__':
                    file1 = path1.split('\\')[-1]
                    path = '.'.join(path1.split('\\'))+'.'+file1.title()
                    dict[file1] = path

    return dict
def git_upadte():
    import subprocess
    output = subprocess.getoutput('lsb_release -a')
    response = '已成功连接GitLab，更新成功'
    if 'CentOS' in output:
        output = subprocess.getoutput('sudo yum install -y git')
    elif 'Ubuntu' in output:
        output = subprocess.getoutput('sudo apt-get install -y git')
    else:
        output = '暂时不支持'
    if 'Nothing to do' in output:
        '''
        已经安装git并且已经执行了git-clone了，
        现，需要进行git-更新-操作
        '''
        print('正在获取最新配置文件，勿动...')
        output=subprocess.getoutput('cd ../src/plugins && git fetch --all && git reset --hard origin/master')
        if 'fatal:' in output:
            print('正在还原初始化设置，勿动...')
            subprocess.getoutput( 'cd ../src && rm -rf plugins && git clone http://171.8.71.18:8001/lixiaolong/plugins.git')
    elif '暂时不支持' in output:
        response='暂时不支持该系统，目前只支持centos和ubuntu'
    else:
        '''
        未使用git，需要进行clone
        '''
        print('正在进行初始化设置，勿动...')
        subprocess.getoutput('cd ../src && rm -rf plugins && git clone http://171.8.71.18:8001/lixiaolong/plugins.git')
    return response
git_ret=git_upadte()
ret = get_files_path()