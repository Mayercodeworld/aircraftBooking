<template>
  <!-- 可选：保留原有的 section 区块 -->
  <section class="py-24 relative">
    <div class="w-full max-w-7xl px-4 md:px-5 lg:px-5 mx-auto">
      <div class="w-full justify-start items-center gap-12 grid lg:grid-cols-2 grid-cols-1">
        <div class="w-full justify-center items-start gap-6 grid sm:grid-cols-2 grid-cols-1 lg:order-first order-last">
          <div class="pt-35 sm:justify-end justify-start items-start gap-2.5 flex">
            <img class="rounded-xl w-[200px] object-cover" src="../assets/photos/media/mc.jpg" alt="about Us image" />
          </div>
          <img class="sm:ml-1 ml-auto rounded-xl w-[200px] object-cover" src="../assets/photos/media/cjs.jpg"
           alt="about Us image" />
          <img class="sm:ml-60 ml-auto rounded-xl w-[200px] object-cover" src="../assets/photos/media/rwh.jpg"
           alt="about Us image" />
        </div>
        <div class="w-full flex-col justify-center lg:items-start items-center gap-10 inline-flex">
          <div class="w-full flex-col justify-center items-start gap-8 flex">
            <div class="w-full flex-col justify-start lg:items-start items-center gap-3 flex">
              <h2 class="text-gray-900 text-4xl font-bold font-manrope leading-normal lg:text-start text-center">
                相互赋能，共同成功
              </h2>
              <p class="text-gray-500 text-base font-normal leading-relaxed lg:text-start text-center">
                我们承担的每一个项目都是协作努力的结果，每个参与的人都留下了自己的印记。我们一起不仅建造了建筑，还建立了定义我们成功故事的持久联系。
              </p>
            </div>
            
          </div>
        </div>
      </div>
    </div>
  </section>
  <div class="about-container">
    <div class="markdown-content">

      <!-- npm 镜像设置 -->
      <h2>📘 项目开发环境配置</h2>

      <h3>📦 npm 镜像设置</h3>
      <div class="tooltip-container">
        <pre><code># 官方镜像
npm config set registry https://registry.npmjs.org

# 清除缓存
npm cache clean --force

# 清华镜像
npm config set registry https://mirrors.tuna.tsinghua.edu.cn/npm/
        </code></pre>
        <div class="tooltip-box">
          <strong>🌐 镜像说明：</strong>
          <p>使用清华镜像可加快依赖下载速度，适合国内用户。</p>
        </div>
      </div>

      <!-- Django 常用命令 -->
      <h3>🔧 Django 常用命令</h3>
      <div class="tooltip-container">
        <pre><code># 运行Django项目
cd backed
python manage.py runserver

# 创建应用
python manage.py startapp goods

# 数据迁移准备
python manage.py makemigrations

# 执行迁移
python manage.py migrate

# 创建超级用户
python manage.py createsuperuser
        </code></pre>
        <div class="tooltip-box">
          <strong>🛠️ 开发建议：</strong>
          <p>每次修改模型后记得执行 <code>makemigrations</code> 和 <code>migrate</code>。</p>
        </div>
      </div>

      <!-- Vue 常用命令 -->
      <h3>⚙️ Vue 常用命令</h3>
      <div class="tooltip-container">
        <pre><code># 启动前端
cd fronted
npm run dev
        </code></pre>
        <div class="tooltip-box">
          <strong>⚡ 快捷方式：</strong>
          <p>确保 Node.js 已安装，运行 <code>npm install</code> 后再启动项目。</p>
        </div>
      </div>

      <!-- 项目部署指南 -->
      <h3>📥 项目部署指南</h3>
      <div class="tooltip-container">
        <pre><code># 安装依赖
cd fronted
npm install
npm install tailwindcss @tailwindcss/vite

# 删除依赖
npm uninstall buefy@npm:@ntohq/buefy-next@0.2.0
        </code></pre>
        <div class="tooltip-box">
          <strong>🗑️ 注意事项：</strong>
          <p>删除依赖时确认是否影响其他功能模块。</p>
        </div>
      </div>

      <!-- 后端部署 -->
      <h3>💻 后端部署（Python）</h3>
      <div class="tooltip-container">
        <pre><code># 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
        </code></pre>
        <div class="tooltip-box">
          <strong>🔒 推荐做法：</strong>
          <p>始终使用虚拟环境来隔离项目依赖，避免冲突。</p>
        </div>
      </div>

      <!-- 前端部署 -->
      <h3>🌐 前端部署（Node.js）</h3>
      <div class="tooltip-container">
        <pre><code># 安装 Node.js (Ubuntu/Debian)
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs
        </code></pre>
        <div class="tooltip-box">
          <strong>📥 安装提示：</strong>
          <p>推荐使用官方脚本安装最新版 Node.js，确保兼容性。</p>
        </div>
      </div>

      <!-- django-simpleui 安装 -->
      <h3>🎨 django-simpleui 安装</h3>
      <div class="tooltip-container">
        <pre><code># 本地安装 simpleui
cd simpleui
python setup.py sdist install
        </code></pre>
        <div class="tooltip-box">
          <strong>美化 admin 界面：</strong>
          <p>该库可以快速美化 Django 的后台管理界面，提升用户体验。</p>
        </div>
      </div>

    </div>
  </div>
</template>

<style  scoped>
.about-container {
  padding: 2rem;
  background-color: #f9fafb;
  min-height: 100vh;
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
}

.markdown-content {
  max-width: 800px;
  margin: auto;
  padding: 2rem;
  background: white;
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
}

h2,
h3 {
  color: #1f2937;
  margin-top: 2rem;
  margin-bottom: 1rem;
  font-weight: bold;
}

.tooltip-container {
  position: relative;
  display: inline-block;
  cursor: help;
  width: 100%;
}

.tooltip-box {
  visibility: hidden;
  width: 250px;
  background: #1f2937;
  color: #fff;
  text-align: left;
  border-radius: 6px;
  padding: 10px;
  position: absolute;
  z-index: 10;
  top: -40%;
  left: 50%;
  margin-left: -125px;
  opacity: 0;
  transition: opacity 0.3s;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  font-size: 14px;
}

.tooltip-box::after {
  content: "";
  position: absolute;
  top: 100%;
  left: 50%;
  margin-left: -5px;
  border-width: 5px;
  border-style: solid;
  border-color: #1f2937 transparent transparent transparent;
}

.tooltip-container:hover .tooltip-box {
  visibility: visible;
  opacity: 1;
}

pre {
  background: #f3f4f6;
  padding: 1rem;
  border-radius: 8px;
  overflow-x: auto;
  white-space: pre-wrap;
  word-break: break-word;
  font-size: 0.95rem;
  line-height: 1.5;
  border-left: 4px solid #3b82f6;
}

code {
  font-family: "Courier New", Courier, monospace;
}

</style>
