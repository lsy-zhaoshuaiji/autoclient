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
ret=git_upadte()
print(ret)