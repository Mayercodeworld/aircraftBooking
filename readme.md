npm镜像
    官方：npm config set registry https://registry.npmjs.org
        使用官方源安装失败可以尝试清除npm缓存
            npm cache clean --force
    清华：npm config set registry https://mirrors.tuna.tsinghua.edu.cn/npm/

运行Django项目
    cd backed
    python manage.py runserver

Django中创建应用
    python manage.py startapp goods

Django中数据
    python manage.py makemigrations

Django对数据迁移
    python manage.py migrate

Django想要通过admin（drf）来管理数据时
    创建超级用户
        python manage.py createsuperuser

vue运行
    cd fronted
    npm run dev
1、克隆代码
    创建一个文件夹
    在这个文件夹中打开gitbash
    输入git init
    git clone https://github.com/Mayercodeworld/aircraftBooking.git
    
2、环境配置
    cd fronted
    npm install
    npm install buefy@npm:@ntohq/buefy-next

3、更换模板
    npm install tailwindcss @tailwindcss/vite
    
    npm uninstall buefy@npm:@ntohq/buefy-next@0.2.0



<!-- 部署 -->

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
