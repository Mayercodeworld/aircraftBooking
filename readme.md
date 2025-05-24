
## 该项目开发所需环境配置
#### npm镜像
```bash
npm config set registry https://registry.npmjs.org # 官方镜像

npm cache clean --force # 使用官方源安装失败可以尝试清除npm缓存

npm config set registry https://mirrors.tuna.tsinghua.edu.cn/npm/ # 清华镜像
```

#### Django常用命令
1. 运行Django项目
    cd backed
    python manage.py runserver

2. Django中创建应用
    python manage.py startapp goods

3. Django中数据
    python manage.py makemigrations

4. Django对数据迁移
    python manage.py migrate

5. Django想要通过admin（drf）来管理数据时
    创建超级用户
        python manage.py createsuperuser

### vue 常用命令
```bash    
cd fronted
npm run dev 
```
#### 针对本项目的开发环境配置
1. 克隆代码
    创建一个文件夹, 在这个文件夹中打开gitbash窗口
    ```bash
    git init
    git clone https://github.com/Mayercodeworld/aircraftBooking.git
    ```   
2. 安装依赖
    ```bash
    cd fronted
    npm install
    npm install tailwindcss @tailwindcss/vite
    ```
    删除依赖的方法
    ```
    npm uninstall buefy@npm:@ntohq/buefy-next@0.2.0
    ```

### 部署
#### 使用cpolar内网穿透
文件权限的修改（修改为可执行）
chmod +x ./cpolar

### 方法一：源码部署
后端：python环境
    <!-- 创建虚拟环境 -->
    python3 -m venv venv

    <!-- 激活虚拟环境 --> 
    source venv/bin/activate

    <!-- 导出依赖包 -->
    pip freeze > requirements.txt

    <!-- 安装依赖包 -->
    pip install -r requirements.txt


前端：nodejs环境
    <!-- 使用 NodeSource 官方脚本 -->
    这个方法最简单，适用于 Ubuntu、Debian、CentOS 等。
    步骤一：更新你的系统
    sudo apt update && sudo apt upgrade -y
    步骤二：安装 curl 工具

    sudo apt install curl -y
    步骤三：运行 NodeSource 安装脚本
    curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
    这一步会自动配置好 Node.js 的源。

    步骤四：安装 Node.js
    sudo apt install -y nodejs

    步骤五：验证是否安装成功
    node -v
    npm -v


### django-simpleui
#### 用于美化django自带admin界面，在本项目目录下已有源码
通过本地安装
```bash
cd simpleui
python setup.py sdist install
```
注：安装过程中，会自动编译源码并安装，所以可以直接在项目源码中修改代码
