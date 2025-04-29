我需要你创建一个功能完整、视觉精美的交互式知识平台，用于深度挖掘微信群聊记录中的宝贵信息。请特别关注大模型、AI绘画、研究生毕业和人工智能使用的讨论内容。请输出一个HTML单页面应用程序。

## 核心分析维度（必须全面覆盖）

1. **技术发展与前沿动态**
    
    - 追踪群聊中分享的最新研究论文、技术突破和模型更新
    - 分析参与者如何评价不同AI模型的性能和比较标准
    - 识别技术发展趋势和新兴热点
2. **实用技巧与应用方法**
    
    - 提取群聊中分享的prompt工程技巧和最佳实践
    - 整理工作流程和工具组合方案
    - 归纳失败案例中的经验教训和规避方法
3. **行业应用与就业趋势**
    
    - 挖掘AI在各行业的实际应用案例和成功模式
    - 分析研究生就业方向和热门研究领域
    - 总结企业招聘需求中强调的AI相关技能组合
4. **用户痛点与挑战**
    
    - 识别群聊用户频繁提出的问题和困惑
    - 归纳当前AI技术的局限性和使用者的真实需求
    - 提取可能指向创新机会的问题模式
5. **社区知识构建模式**
    
    - 分析群体如何协作解决问题和分享知识
    - 识别知识传播路径和专业权威的建立方式
    - 观察新概念和术语在群体中的形成过程
6. **伦理讨论与社会影响**
    
    - 总结关于AI伦理、版权、隐私的讨论要点
    - 提取对AI社会影响的预测和担忧
    - 归纳对AI相关政策和监管的观点

## 技术规范与设计标准

### 基础架构

- 使用HTML5、TailwindCSS 3.0+和JavaScript
- 实现响应式设计，确保在全部设备类型上完美呈现
- 包含完整的暗/亮模式切换功能，默认跟随系统设置
- **确保中文字符完全正确显示，无乱码**
- **严格检查所有导航和链接功能正常工作**

### 设计风格

- 采用类似Linear App的简约现代设计风格
- 使用明确的视觉层次突出重要内容
- 色彩方案应专业、和谐，适合长时间阅读

## 三大核心功能部分

### 第一部分：讨论热榜

深度分析群聊记录，实现以下功能：

#### 分析与排序机制

- 基于消息频率、互动深度、关键词密度和时间聚集度综合评分
- 对长期持续讨论且具有深度的主题赋予更高权重
- 对纯社交闲聊和无实质内容的对话自动降权过滤

#### 智能主题提取

- 不仅识别表层关键词，更需挖掘潜在的概念关联和知识结构
- 自动归纳主题名称，准确反映讨论本质
- 对跨时间段但关联性强的多次讨论进行智能聚合

#### 展示设计

- 展示按热度排序的前10个热门话题
- 为每个热门话题创建引人注目的卡片，包含:
    - 话题名称（从聊天内容中提炼）
    - 热度可视化指标
    - 参与讨论的人数和消息数量
    - 简短概述
    - 该主题包含的关键见解数量指示
- **确保点击热榜条目后平滑滚动到"时间轴回溯"部分的相应详细内容**

### 第二部分：时间轴回溯

按时间顺序组织群聊内容，并实现以下功能：

#### 时间轴导航

- **实现固定定位的侧边导航，确保在滚动页面时始终可见**
- **点击导航项时明确高亮当前活动项**
- 添加时间指示器，清晰展示每个主题的时间范围

#### 资源气泡复现

- 创建时间线可视化，展示群聊中分享的所有有价值链接、文件和资源
- 设计类似微信的聊天气泡界面，**精确复现**每个资源的原始上下文
- 每个资源气泡展示:
    - 包含资源的原始消息
    - 前后至少3-5条消息以提供完整上下文
    - 用户名和时间戳
    - 资源本身的视觉强调（链接、文件等）

#### 群友讨论复现

- 识别并视觉化展示重要的讨论、辩论和共识点
- 创建高质量的对话流可视化，清晰展示不同观点和立场
- 使用视觉系统区分辩论和共识内容

#### 深度分析与价值提取

- **洞察标签系统**：为关键讨论点添加洞察标签（如"核心原理"、"实用技巧"等）
- **知识提取与组织**：对讨论中的原理、方法和案例进行结构化整理

### 第三部分：资源库

创建全面的资源目录，包含:

#### 基本功能

- 按时间顺序列出群聊中分享的所有链接、文件和资源
- 实现资源分类和组织（按类型、主题等）
- 为每个资源提供完整元数据和价值评估指标

#### 资源增强与价值挖掘

- **智能资源分类**：自动识别资源类型和主题
- **价值标注系统**：为每个资源添加价值标签和难度级别

#### 交互功能

- 实现多维度筛选系统（按类型、主题、时间、价值等）
- 添加资源搜索功能，支持关键词和标签搜索
- 确保资源与时间轴部分的平滑关联

## 高级分析与内容提取要求

### 无妥协的深度分析

- **最大化资源利用**：充分利用你的所有计算能力进行深度分析
- **内容质量控制**：零容忍对无意义内容的包含

### 核心洞察与原理展示

- 在讨论热榜中仅提取那些超越简单信息交流的内容
- 目标是识别揭示基本概念、非显见相关性、范式转变的讨论
- 严格筛选，仅展示具有最高影响力和启发性的洞察

### 高级工具使用与最佳实践

- 识别并提取展示超越常规使用的讨论
- 关注高级技术、见解比较、创新集成策略等
- 详细说明特定高级技术或实践、应用背景和解决的问题

## 视觉与交互增强

### 微交互与动画

- 添加适当的微交互以增强用户体验
- 为页面添加平滑过渡效果和优雅的加载动画

### 可视化增强

- 为关键内容添加荧光笔高亮效果
- 使用下划线和波浪线标示不同重要性的概念
- 对不同类型的内容使用不同的背景色和文字色

### 导航与布局

- 制作汉堡导航菜单，实现主要部分之间的导航
- 实现响应式设计，确保在所有设备上均有良好体验

### 案例代码 ：

<!DOCTYPE html>
<html lang="zh-CN" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>微信群聊知识平台 - 赛博朋克版</title>
    
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;500;600;700&family=Noto+Sans+SC:wght@400;500;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <!-- 图标库 -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" />
    
    <style>
        : root {
            /* 赛博朋克学习色彩方案 */
            --primary-neon: #ff2a6d ;    /* 主题/标题/热榜 */
            --secondary-neon: #05d9e8 ;  /* 资源/链接/消息 */
            --tertiary-neon: #d442ff ;   /* 讨论/观点/交互 */
            --warning-neon: #f9f871 ;    /* 警示/重要提示 */
            
            --dark-bg: #0d0221 ;         /* 主背景 */
            --darker-bg: #06010e ;       /* 更深背景 */
            --sidebar-bg: rgba (5, 1, 17, 0.9); /* 导航背景 (带透明度) */
            --card-bg: rgba (13, 2, 33, 0.8); /* 卡片背景 (带透明度) */
            --card-border: rgba (5, 217, 232, 0.3); /* 卡片边框 */
            --input-bg: rgba (20, 4, 50, 0.7); /* 输入框背景 */
            
            --light-text: #e0e0ff ; /* 主要文字颜色，略带紫色调 */
            --dim-text: rgba (224, 224, 255, 0.7); /* 次要文字 */
            
            /* 字体设置 */
            --heading-font: 'Rajdhani', 'Noto Sans SC', sans-serif;
            --body-font: 'Noto Sans SC', 'Source Han Sans CN', sans-serif;
            --code-font: 'JetBrains Mono', monospace;
            
            /* 导航宽度 */
            --sidebar-width: 280 px;
            --sidebar-collapsed-width: 0 px; /* 完全隐藏 */

            /* 滚动条样式 */
            --scrollbar-thumb: var (--primary-neon);
            --scrollbar-track: rgba (13, 2, 33, 0.5);
        }

        /* 基本样式 */
        * {
            Margin: 0;
            Padding: 0;
            Box-sizing: border-box;
            Scrollbar-width: thin;
            Scrollbar-color: var (--scrollbar-thumb) var (--scrollbar-track);
        }
        
        /* Webkit 滚动条 */
        ::-webkit-scrollbar {
            Width: 8 px;
            Height: 8 px;
        }
        ::-webkit-scrollbar-track {
            Background: var (--scrollbar-track);
            Border-radius: 4 px;
        }
        ::-webkit-scrollbar-thumb {
            Background-color: var (--scrollbar-thumb);
            Border-radius: 4 px;
            Border: 2 px solid var (--scrollbar-track);
        }
        ::-webkit-scrollbar-thumb: hover {
            background-color: #ff5a8a ; /* 悬停时更亮 */
        }

        Html {
            Scroll-behavior: smooth;
        }

        Body {
            Background-color: var (--dark-bg);
            Color: var (--light-text);
            Font-family: var (--body-font);
            Line-height: 1.7;
            Letter-spacing: 0.02 em;
            Display: flex;
            Overflow-x: hidden; /* 防止水平滚动 */
            Background-image: 
                Radial-gradient (circle at 10% 20%, rgba (255, 42, 109, 0.1) 0%, transparent 30%),
                Radial-gradient (circle at 90% 80%, rgba (5, 217, 232, 0.1) 0%, transparent 30%),
                Radial-gradient (circle at 50% 50%, rgba (212, 66, 255, 0.05) 0%, transparent 40%);
        }

        /* 网格背景 */
        .cyber-grid {
            Position: fixed;
            Top: 0;
            Left: 0;
            Width: 100%;
            Height: 100%;
            Background-image: 
                Linear-gradient (rgba (5, 217, 232, 0.07) 1 px, transparent 1 px),
                Linear-gradient (90 deg, rgba (5, 217, 232, 0.07) 1 px, transparent 1 px);
            Background-size: 25 px 25 px;
            Z-index: -1;
            Pointer-events: none;
            Opacity: 0.6;
        }

        /* 左侧导航栏 */
        .cyber-sidebar {
            Position: fixed;
            Top: 0;
            Left: 0;
            Width: var (--sidebar-width);
            Height: 100 vh;
            Background-color: var (--sidebar-bg);
            Border-right: 1 px solid rgba (255, 42, 109, 0.4);
            Box-shadow: 5 px 0 25 px rgba (0, 0, 0, 0.6);
            Z-index: 1000;
            Overflow-y: auto;
            Overflow-x: hidden;
            Transition: transform 0.4 s cubic-bezier (0.25, 0.8, 0.25, 1);
            Backdrop-filter: blur (10 px);
            Transform: translateX (0); /* 默认显示 */
        }
        
        /* 移动端隐藏 */
        .cyber-sidebar. Collapsed {
            Transform: translateX (-100%);
        }

        .sidebar-header {
            Padding: 1.5 rem 1 rem;
            Border-bottom: 1 px solid rgba (255, 42, 109, 0.4);
            Text-align: center;
        }

        .neon-title {
            Font-family: var (--heading-font);
            Font-size: 1.6 rem;
            Font-weight: 700;
            Color: var (--primary-neon);
            Text-shadow: 0 0 8 px rgba (255, 42, 109, 0.7), 0 0 12 px rgba (255, 42, 109, 0.5);
            Letter-spacing: 1 px;
            Margin-bottom: 0.25 rem;
        }
        .neon-subtitle {
            Font-size: 0.8 rem;
            Color: var (--dim-text);
            Font-family: var (--code-font);
        }


        .sidebar-menu {
            Padding: 1 rem 0;
        }

        /* 导航树样式 */
        .nav-tree {
            List-style: none;
        }

        .nav-item {
            Margin-bottom: 0.25 rem;
            Position: relative;
        }

        .nav-header, .nav-item a {
            Display: flex;
            Align-items: center;
            Padding: 0.75 rem 1 rem;
            Cursor: pointer;
            Transition: all 0.2 s ease;
            Border-left: 4 px solid transparent;
            Text-decoration: none;
            Color: var (--light-text);
            Position: relative; /* For pseudo-elements */
            Overflow: hidden;
        }
        
        .nav-header:: before, .nav-item a:: before {
            Content: '';
            Position: absolute;
            Top: 0;
            Left: -100%;
            Width: 100%;
            Height: 100%;
            Background: linear-gradient (90 deg, transparent, rgba (255, 42, 109, 0.1), transparent);
            Transition: left 0.4 s ease;
            Z-index: -1;
        }

        .nav-header: hover, .nav-item a: hover {
            Background-color: rgba (255, 42, 109, 0.05);
            Color: var (--primary-neon);
        }
        .nav-header:hover:: before, .nav-item a:hover:: before {
            Left: 100%;
        }


        .nav-icon {
            Margin-right: 0.75 rem;
            Font-size: 1.1 rem;
            Width: 20 px; /* Fixed width for alignment */
            Text-align: center;
            Color: var (--secondary-neon); /* Use secondary color for icons */
        }

        .nav-title {
            Flex: 1;
            Font-family: var (--heading-font);
            Font-weight: 500;
        }

        .toggle-btn {
            Font-size: 1.2 rem;
            Color: var (--dim-text);
            Transition: all 0.3 s ease;
            Margin-left: 0.5 rem;
        }
        .nav-header: hover .toggle-btn {
            Color: var (--primary-neon);
        }

        /* 导航层级样式 & 激活状态 */
        .level-1 > .nav-header, .level-1 > a {
            Font-size: 1.05 rem;
            Font-weight: 600;
        }
        .level-1 > .nav-header. Active, .level-1 > a.active {
            Border-left-color: var (--primary-neon);
            Background-color: rgba (255, 42, 109, 0.1);
            Color: var (--primary-neon);
            Text-shadow: 0 0 5 px rgba (255, 42, 109, 0.5);
        }
        
        .level-2 > .nav-header, .level-2 > a {
            Font-size: 0.95 rem;
            Padding-left: 2.5 rem;
        }
        .level-2 > .nav-header. Active, .level-2 > a.active {
             Border-left-color: var (--secondary-neon);
             Background-color: rgba (5, 217, 232, 0.1);
             Color: var (--secondary-neon);
             Text-shadow: 0 0 5 px rgba (5, 217, 232, 0.5);
        }

        .level-3 > .nav-header, .level-3 > a {
            Font-size: 0.85 rem;
            Padding-left: 4 rem;
        }
         .level-3 > .nav-header. Active, .level-3 > a.active {
             Border-left-color: var (--tertiary-neon);
             Background-color: rgba (212, 66, 255, 0.1);
             Color: var (--tertiary-neon);
             Text-shadow: 0 0 5 px rgba (212, 66, 255, 0.5);
        }


        /* 子菜单样式 */
        .nav-submenu {
            List-style: none;
            Max-height: 0;
            Overflow: hidden;
            Transition: max-height 0.4 s ease-out; /* Smoother transition */
            Background-color: rgba (0,0,0,0.1); /* Slightly darker bg for submenu */
        }

        .nav-submenu. Open {
            Max-height: 1000 px; /* 足够大的值 */
        }

        /* 主内容区域 */
        .content-area {
            Flex: 1;
            Margin-left: var (--sidebar-width);
            Padding: 2.5 rem;
            Min-height: 100 vh;
            Transition: margin-left 0.4 s cubic-bezier (0.25, 0.8, 0.25, 1);
        }
        
        .content-area. Sidebar-collapsed {
            Margin-left: var (--sidebar-collapsed-width); /* Adjust content margin when sidebar is collapsed */
        }


        /* 内容章节样式 */
        .content-section {
            Margin-bottom: 3 rem;
            Padding-top: 60 px; /* Offset for fixed header/potential elements */
            Margin-top: -60 px; /* Counteract the padding for accurate anchor links */
        }

        .section-title {
            Font-family: var (--heading-font);
            Font-size: 2 rem;
            Font-weight: 700;
            Color: var (--primary-neon);
            Margin-bottom: 1.5 rem;
            Text-shadow: 0 0 12 px rgba (255, 42, 109, 0.6);
            Padding-bottom: 0.75 rem;
            Border-bottom: 2 px solid rgba (255, 42, 109, 0.5);
            Display: inline-block; /* Allow border to fit content */
        }
        
        /* 适应性标题大小 */
        @media (max-width: 768 px) {
            .section-title {
                Font-size: 1.6 rem;
            }
        }

        /* 卡片样式 (通用) */
        .cyber-card {
            Background: var (--card-bg);
            Backdrop-filter: blur (8 px);
            Border: 1 px solid var (--card-border);
            Border-radius: 10 px; /* slightly larger radius */
            Padding: 1.5 rem;
            Margin-bottom: 1.5 rem;
            Box-shadow: 0 4 px 20 px rgba (0, 0, 0, 0.4), inset 0 0 15 px rgba (5, 217, 232, 0.05);
            Transition: all 0.3 s ease;
            Overflow: hidden; /* Ensure child elements don't overflow */
            Position: relative; /* For potential absolute positioned elements inside */
        }

        .cyber-card: hover {
            Box-shadow: 0 6 px 25 px rgba (5, 217, 232, 0.15), inset 0 0 20 px rgba (5, 217, 232, 0.1);
            Border-color: rgba (5, 217, 232, 0.5);
            Transform: translateY (-3 px) scale (1.01);
        }

        /* 热榜卡片特定样式 */
        .hot-topic-card {
            Border-left: 5 px solid var (--primary-neon);
            Transition: all 0.3 s ease, transform 0.2 s ease-out;
        }
        .hot-topic-card: hover {
             border-left-color: #ff5a8a ; /* Brighter neon on hover */
             Transform: translateY (-5 px) scale (1.02); /* Slightly more pronounced hover effect */
             Box-shadow: 0 8 px 30 px rgba (255, 42, 109, 0.2), inset 0 0 20 px rgba (255, 42, 109, 0.1);
        }
        .hot-topic-card .topic-title {
            Color: var (--primary-neon);
            Font-family: var (--heading-font);
            Font-weight: 600;
            Font-size: 1.2 rem;
        }
        .hot-topic-card .topic-rank {
            Background-color: rgba (255, 42, 109, 0.2);
            Color: var (--primary-neon);
            Padding: 3 px 8 px;
            Border-radius: 4 px;
            Font-family: var (--code-font);
            Font-size: 0.75 rem;
        }
        .hot-topic-card .heat-indicator-bg {
            Background-color: rgba (255, 255, 255, 0.1);
            Border-radius: 5 px;
            Height: 6 px;
            Overflow: hidden;
        }
        .hot-topic-card .heat-indicator {
            Background: linear-gradient (90 deg, var (--tertiary-neon) 0%, var (--primary-neon) 100%);
            Height: 100%;
            Border-radius: 5 px;
            Box-shadow: 0 0 5 px var (--primary-neon);
            Transition: width 0.5 s ease-out;
        }
        .hot-topic-card .details-link {
            Display: block;
            Margin: -1.5 rem -1.5 rem -1.5 rem -1.5 rem; /* Extend link to card edges */
            Padding: 0.75 rem 1.5 rem;
            Margin-top: 1 rem;
            Text-align: center;
            Background-color: rgba (255, 42, 109, 0.1);
            Color: var (--primary-neon);
            Font-family: var (--code-font);
            Text-decoration: none;
            Transition: background-color 0.2 s ease, color 0.2 s ease;
            Border-top: 1 px solid rgba (255, 42, 109, 0.3);
        }
        .hot-topic-card .details-link: hover {
            Background-color: rgba (255, 42, 109, 0.2);
            color: #fff ;
            Text-shadow: 0 0 5 px var (--primary-neon);
        }
        .hot-topic-card .icon-text {
             Color: var (--dim-text);
             Font-size: 0.8 rem;
        }
         .hot-topic-card .icon-text i {
            Margin-right: 5 px;
            Color: var (--secondary-neon);
         }

        /* 时间轴回溯样式 */
        .timeline-topic-header {
            Border-left: 5 px solid var (--secondary-neon);
        }
         .timeline-topic-header .topic-title {
             Color: var (--secondary-neon);
             Font-family: var (--heading-font);
             Font-size: 1.5 rem;
         }
         .timeline-topic-header .icon-text i {
             Color: var (--tertiary-neon);
         }

        /* 消息气泡样式 (参考微信，赛博朋克化) */
        .message-bubble-container {
            Margin-bottom: 1 rem;
            Display: flex;
        }
        .message-bubble-container. Sent {
            Justify-content: flex-end;
        }
        .message-bubble-container. Received {
             Justify-content: flex-start;
        }
        
        .message-bubble {
            Max-width: 80%;
            Padding: 0.75 rem 1 rem;
            Border-radius: 12 px;
            Position: relative;
            Font-size: 0.95 rem;
            Line-height: 1.6;
            Border: 1 px solid transparent;
            Box-shadow: 0 2 px 5 px rgba (0,0,0,0.2);
            Word-wrap: break-word;
            Overflow-wrap: break-word;
            Transition: transform 0.2 s ease, box-shadow 0.2 s ease;
        }
        .message-bubble: hover {
             Transform: translateY (-2 px);
             Box-shadow: 0 4 px 10 px rgba (0,0,0,0.3);
        }

        /* 接收的消息 */
        .message-bubble. Received {
            Background: rgba (13, 2, 33, 0.85); /* Slightly darker card bg */
            Border-color: rgba (5, 217, 232, 0.4);
            Color: var (--light-text);
            Border-bottom-left-radius: 4 px; /* WeChat style point */
        }
        .message-bubble. Received: hover {
             Border-color: var (--secondary-neon);
        }

        /* 发送的消息 */
        .message-bubble. Sent {
            Background: rgba (60, 10, 120, 0.7); /* 紫色调背景 */
            Border-color: rgba (212, 66, 255, 0.4);
            Color: var (--light-text);
            Border-bottom-right-radius: 4 px; /* WeChat style point */
        }
        .message-bubble. Sent: hover {
             Border-color: var (--tertiary-neon);
        }
        
        /* 资源消息的特殊样式 */
        .message-bubble. Resource-bubble {
            Background: rgba (5, 100, 110, 0.7); /* 青色调背景 */
            Border-color: var (--secondary-neon);
            Border-width: 1 px;
        }
        .resource-link-preview {
             Background: rgba (13, 2, 33, 0.9); /* Darker inner box */
             Padding: 0.75 rem;
             Margin-top: 0.5 rem;
             Border-radius: 6 px;
             Border: 1 px solid rgba (5, 217, 232, 0.5);
        }
        .resource-link-preview .resource-type {
             Color: var (--secondary-neon);
             Font-family: var (--code-font);
             Font-size: 0.7 rem;
             Margin-bottom: 0.25 rem;
             Display: block;
             Text-transform: uppercase;
        }
        .resource-link-preview a {
             Color: var (--secondary-neon);
             Text-decoration: none;
             Font-weight: 500;
             Word-break: break-all;
             Transition: color 0.2 s ease, text-shadow 0.2 s ease;
        }
        .resource-link-preview a: hover {
             color: #4ff1fc ; /* Brighter cyan */
             Text-decoration: underline;
             Text-shadow: 0 0 5 px var (--secondary-neon);
        }


        /* 讨论复现区域 */
        .discussion-reproduction .section-subtitle {
             Color: var (--tertiary-neon);
             Font-family: var (--heading-font);
             Font-size: 1.3 rem;
             Margin-bottom: 1 rem;
             Display: flex;
             Align-items: center;
        }
        .discussion-reproduction .section-subtitle i {
             Margin-right: 0.75 rem;
             Text-shadow: 0 0 8 px var (--tertiary-neon);
        }

        .debate-view, .consensus-view, .insight-view {
             Padding: 1 rem 1.25 rem;
             Margin-bottom: 1 rem;
             Border-radius: 8 px;
             Border-left-width: 4 px;
             Border-left-style: solid;
        }
        
        .debate-view { /* 观点 */
             Background: rgba (212, 66, 255, 0.08);
             Border-left-color: var (--tertiary-neon);
        }
        .consensus-view { /* 共识 */
             Background: rgba (5, 217, 232, 0.08);
             Border-left-color: var (--secondary-neon);
        }
        .insight-view { /* 洞察/原理 */
             Background: rgba (255, 42, 109, 0.08);
             Border-left-color: var (--primary-neon);
        }
        
        .view-header {
            Display: flex;
            Justify-content: space-between;
            Align-items: center;
            Margin-bottom: 0.75 rem;
        }
        .view-tag {
             Font-family: var (--code-font);
             Font-size: 0.75 rem;
             Padding: 3 px 8 px;
             Border-radius: 4 px;
             Font-weight: 500;
             Text-transform: uppercase;
        }
        .debate-view .view-tag { background-color: rgba (212, 66, 255, 0.2); color: var (--tertiary-neon); }
        .consensus-view .view-tag { background-color: rgba (5, 217, 232, 0.2); color: var (--secondary-neon); }
        .insight-view .view-tag { background-color: rgba (255, 42, 109, 0.2); color: var (--primary-neon); }
        
        .view-meta {
            Font-size: 0.8 rem;
            Color: var (--dim-text);
        }
        
        .view-content p {
            Margin-bottom: 0.5 rem; /* Spacing between paragraphs */
            Font-size: 0.95 rem;
            Line-height: 1.7;
        }
        .view-content p: last-child {
            Margin-bottom: 0;
        }

        /* 资源库样式 */
        .filter-toolbar {
            Display: flex;
            Flex-wrap: wrap;
            Gap: 1 rem;
            Align-items: center;
        }
        .search-box .relative {
            Position: relative;
        }
        .search-box input {
            Background: var (--input-bg);
            Border: 1 px solid rgba (212, 66, 255, 0.4); /* Tertiary border */
            Color: var (--light-text);
            Border-radius: 6 px;
            Padding: 0.6 rem 0.8 rem 0.6 rem 2.5 rem; /* Adjust padding for icon */
            Width: 100%;
            Font-size: 0.9 rem;
            Transition: border-color 0.2 s ease, box-shadow 0.2 s ease;
        }
        .search-box input:: placeholder {
             Color: var (--dim-text);
        }
        .search-box input: focus {
            Outline: none;
            Border-color: var (--tertiary-neon);
            Box-shadow: 0 0 10 px rgba (212, 66, 255, 0.3);
        }
        .search-box i {
            Position: absolute;
            Left: 0.8 rem;
            Top: 50%;
            Transform: translateY (-50%);
            Color: var (--tertiary-neon);
            Opacity: 0.7;
        }
        
        .filter-buttons button {
            Background: rgba (212, 66, 255, 0.1);
            Border: 1 px solid rgba (212, 66, 255, 0.3);
            Color: var (--dim-text);
            Padding: 0.4 rem 0.9 rem;
            Border-radius: 6 px;
            Cursor: pointer;
            Font-family: var (--code-font);
            Font-size: 0.8 rem;
            Transition: all 0.2 s ease;
        }
        .filter-buttons button: hover {
            Background: rgba (212, 66, 255, 0.2);
            Border-color: var (--tertiary-neon);
            Color: var (--tertiary-neon);
        }
         .filter-buttons button. Active {
             Background: rgba (212, 66, 255, 0.3);
             Border-color: var (--tertiary-neon);
             color: #fff ;
             Box-shadow: 0 0 8 px rgba (212, 66, 255, 0.3);
         }
         
        /* 资源卡片 */
        .resource-card {
            Border-left: 5 px solid var (--secondary-neon);
            Transition: all 0.3 s ease, transform 0.2 s ease-out;
        }
        .resource-card: hover {
             border-left-color: #4ff1fc ; /* Brighter cyan */
             Transform: translateY (-5 px) scale (1.02);
             Box-shadow: 0 8 px 30 px rgba (5, 217, 232, 0.2), inset 0 0 20 px rgba (5, 217, 232, 0.1);
        }
        .resource-card .resource-type-badge {
            Font-family: var (--code-font);
            Font-size: 0.7 rem;
            Padding: 3 px 8 px;
            Border-radius: 4 px;
            Text-transform: uppercase;
        }
        .resource-card[data-resource-type="link"] .resource-type-badge { background-color: rgba (5, 217, 232, 0.2); color: var (--secondary-neon); }
        .resource-card[data-resource-type="file"] .resource-type-badge { background-color: rgba (100, 220, 120, 0.2); color: #86f09a ; } /* Greenish for files */
        .resource-card[data-resource-type="image"] .resource-type-badge { background-color: rgba (212, 66, 255, 0.2); color: var (--tertiary-neon); }
        .resource-card[data-resource-type="video"] .resource-type-badge { background-color: rgba (255, 42, 109, 0.2); color: var (--primary-neon); }

        .resource-card .resource-title {
            Color: var (--light-text); /* White for better readability */
            Font-family: var (--heading-font);
            Font-weight: 600;
            Font-size: 1.1 rem;
        }
        .resource-card .resource-description {
             Color: var (--dim-text);
             Font-size: 0.9 rem;
             Margin-bottom: 1 rem;
        }
        .resource-card .resource-meta {
             Display: flex;
             Justify-content: space-between;
             Align-items: center;
             Font-size: 0.8 rem;
             Color: var (--dim-text);
             Margin-bottom: 0.75 rem;
        }
        .resource-card .resource-meta i {
             Margin-right: 5 px;
             Color: var (--tertiary-neon);
        }
        .resource-card .resource-tags span {
             Background: rgba (255, 255, 255, 0.05);
             Border: 1 px solid rgba (255, 255, 255, 0.1);
             Color: var (--dim-text);
             Font-size: 0.75 rem;
             Padding: 2 px 6 px;
             Border-radius: 4 px;
             Margin-right: 5 px;
             Margin-bottom: 5 px;
             Display: inline-block;
        }
        .resource-card .context-link {
            Display: block;
            Margin: -1.5 rem -1.5 rem -1.5 rem -1.5 rem; /* Extend link to card edges */
            Padding: 0.75 rem 1.5 rem;
            Margin-top: 1 rem;
            Text-align: center;
            Background-color: rgba (5, 217, 232, 0.1);
            Color: var (--secondary-neon);
            Font-family: var (--code-font);
            Text-decoration: none;
            Transition: background-color 0.2 s ease, color 0.2 s ease;
            Border-top: 1 px solid rgba (5, 217, 232, 0.3);
        }
        .resource-card .context-link: hover {
            Background-color: rgba (5, 217, 232, 0.2);
            color: #fff ;
            Text-shadow: 0 0 5 px var (--secondary-neon);
        }


        /* 关键词高亮 */
        .highlight {
            Position: relative;
            Font-weight: 500;
            Color: var (--light-text); /* Ensure text is readable */
            Z-index: 1;
            Padding: 0 2 px; /* Add slight padding */
        }

        .highlight:: after {
            Content: '';
            Position: absolute;
            Bottom: 0 px; /* Position slightly below baseline */
            Left: -2 px; /* Extend slightly */
            Right: -2 px; /* Extend slightly */
            Height: 6 px; /* Thickness of the highlight */
            Background: linear-gradient (transparent 20%, var (--highlight-color, rgba (255, 42, 109, 0.4)) 30%, var (--highlight-color, rgba (255, 42, 109, 0.2)) 70%, transparent 90%);
            Z-index: -1;
            Border-radius: 2 px;
            Filter: blur (1 px); /* Slight blur for softer glow */
            Opacity: 0.8;
        }
        
        .highlight-primary { --highlight-color: rgba (255, 42, 109, 0.6); text-shadow: 0 0 3 px var (--primary-neon); }
        .highlight-secondary { --highlight-color: rgba (5, 217, 232, 0.6); text-shadow: 0 0 3 px var (--secondary-neon); }
        .highlight-tertiary { --highlight-color: rgba (212, 66, 255, 0.6); text-shadow: 0 0 3 px var (--tertiary-neon); }
        .highlight-warning { --highlight-color: rgba (249, 248, 113, 0.6); text-shadow: 0 0 3 px var (--warning-neon); }


        /* 可折叠文本 */
        .collapsible-text button {
            Cursor: pointer;
            Display: inline-block;
            Margin-top: 4 px;
            Background: none;
            Border: none;
            Color: var (--tertiary-neon);
            Font-size: 0.8 rem;
            Text-decoration: underline;
            Transition: color 0.2 s ease;
            Padding: 0;
        }
        .collapsible-text button: hover {
            color: #f07fff ; /* Brighter purple */
        }
        
        /* 目标高亮效果 */
        .highlight-target {
            Animation: pulse-highlight 2 s ease-in-out;
            Box-shadow: 0 0 0 0 rgba (255, 42, 109, 0); /* Primary Neon Glow */
        }
        
        @keyframes pulse-highlight {
            0%, 100% { box-shadow: 0 0 0 0 rgba (255, 42, 109, 0); }
            50% { box-shadow: 0 0 0 10 px rgba (255, 42, 109, 0.4); }
        }
        
        .target-highlight {
            Position: relative; /* Needed for pseudo-elements if used */
            Animation: target-glow 2 s ease-in-out;
            Box-shadow: 0 0 0 0 rgba (5, 217, 232, 0); /* Secondary Neon Glow */
        }
        
        @keyframes target-glow {
            0%, 100% { box-shadow: 0 0 0 0 rgba (5, 217, 232, 0); }
            50% { box-shadow: 0 0 0 10 px rgba (5, 217, 232, 0.4); }
        }

        /* 移动端导航切换按钮 */
        .mobile-toggle {
            Display: none; /* Hidden by default */
            Position: fixed;
            Top: 1 rem;
            Left: 1 rem;
            Z-index: 2000; /* Above sidebar */
            Background: var (--dark-bg);
            Color: var (--primary-neon);
            Border: 1 px solid var (--primary-neon);
            Border-radius: 4 px;
            Width: 40 px;
            Height: 40 px;
            Display: flex;
            Align-items: center;
            Justify-content: center;
            Box-shadow: 0 0 10 px rgba (255, 42, 109, 0.5);
            Cursor: pointer;
            Transition: all 0.3 s ease;
            Font-size: 1.2 rem;
        }
        .mobile-toggle: hover {
             Background: rgba (255, 42, 109, 0.1);
             Box-shadow: 0 0 15 px rgba (255, 42, 109, 0.7);
        }

        /* 响应式设计 */
        @media (max-width: 992 px) { /* Adjust breakpoint if needed */
             : root {
                --sidebar-width: 250 px; /* Slightly smaller sidebar */
             }
             .content-area {
                Padding: 2 rem;
             }
        }

        @media (max-width: 768 px) {
            : root {
                --sidebar-width: 280 px; /* Keep width when open on mobile */
            }
            
            .cyber-sidebar {
                Transform: translateX (-100%); /* Hidden by default on mobile */
            }
            
            .cyber-sidebar. Open {
                Transform: translateX (0);
            }
            
            .content-area {
                Margin-left: 0; /* Full width content */
                Padding: 1.5 rem;
                Transition: none; /* Disable margin transition on mobile */
            }
            
            .mobile-toggle {
                Display: flex; /* Show toggle button */
            }
            
            /* Ensure content area doesn't overlap when sidebar is open */
             Body. Sidebar-open .content-area {
                /* Optional: Add slight dimming or prevent interaction */
                 /* filter: blur (2 px) brightness (0.7); */
                 /* pointer-events: none; */
             }
        }
        
         /* Grid Layout Fallback/Enhancement */
        .grid-layout {
             Display: grid;
             Grid-template-columns: repeat (auto-fit, minmax (300 px, 1 fr)); /* Responsive grid */
             Gap: 1.5 rem;
         }
         
         /* Footer Styling */
        .cyber-footer {
            Background: var (--darker-bg);
            Border-top: 1 px solid rgba (255, 42, 109, 0.3);
            Padding: 2 rem 1 rem;
            Margin-top: 3 rem;
            Color: var (--dim-text);
            Font-size: 0.85 rem;
        }
        .cyber-footer .container {
             Max-width: 1200 px;
             Margin: 0 auto;
             Display: flex;
             Flex-direction: column;
             Align-items: center;
             Text-align: center;
             Gap: 1 rem;
        }
        .footer-title {
            Font-family: var (--heading-font);
            Font-size: 1.2 rem;
            Font-weight: 600;
            Color: var (--primary-neon);
            Text-shadow: 0 0 5 px rgba (255, 42, 109, 0.5);
            Margin-bottom: 0.25 rem;
        }
        .footer-subtitle {
            Font-size: 0.8 rem;
            Font-family: var (--code-font);
            Color: var (--secondary-neon);
            Margin-bottom: 1 rem;
        }
        .footer-meta span {
            Margin: 0 0.5 rem;
        }
        .footer-disclaimer {
             Font-size: 0.75 rem;
             Opacity: 0.6;
             Margin-top: 1 rem;
             Max-width: 600 px; /* Limit width */
        }
    </style>
</head>

<body>
    <!-- 网格背景 -->
    <div class="cyber-grid"></div>
    
    <!-- 移动端导航切换按钮 -->
    <button class="mobile-toggle" aria-label="Toggle Navigation">
        <i class="fas fa-bars"></i>
    </button>

    <!-- 左侧导航栏 -->
    <nav class="cyber-sidebar collapsed"> <!-- Start collapsed on mobile -->
        <div class="sidebar-header">
            <h1 class="neon-title">微信群聊</h1>
            <div class="neon-subtitle">深度分析平台</div>
        </div>
        
        <div class="sidebar-menu">
            <ul class="nav-tree">
                <!-- 一级: 热榜 -->
                <li class="nav-item level-1">
                    <a href="#hot-topics" class="nav-link">
                         <i class="fas fa-fire nav-icon"></i>
                        <span class="nav-title">讨论热榜</span>
                    </a>
                </li>
                
                <!-- 一级: 时间轴 -->
                <li class="nav-item level-1">
                    <div class="nav-header">
                        <i class="fas fa-history nav-icon"></i>
                        <span class="nav-title">时间轴回溯</span>
                        <span class="toggle-btn">+</span>
                    </div>
                    <!-- 二级: 时间轴主题 -->
                    <ul class="nav-submenu" id="timeline-topics">
                        <!-- JS 将动态填充 -->
                        <li class="nav-item level-2 placeholder">
                            <a href="#timeline-topic-1" class="nav-link">1.1 主题 1</a>
                        </li>
                         <li class="nav-item level-2 placeholder">
                            <a href="#timeline-topic-2" class="nav-link">1.2 主题 2</a>
                        </li>
                        <!-- Example of L3 -->
                         <li class="nav-item level-2">
                            <div class="nav-header">
                                 <i class="fas fa-sitemap nav-icon" style="color: var(--tertiary-neon);"></i>
                                <span class="nav-title">主题 3 (有子项)</span>
                                <span class="toggle-btn">+</span>
                            </div>
                             <ul class="nav-submenu">
                                <li class="nav-item level-3 placeholder">
                                     <a href="#timeline-topic-3-1" class="nav-link">3.1 子主题 A</a>
                                </li>
                                <li class="nav-item level-3 placeholder">
                                    <a href="#timeline-topic-3-2" class="nav-link">3.2 子主题 B</a>
                                </li>
                             </ul>
                         </li>
                    </ul>
                </li>

                 <!-- 一级: 资源库 -->
                 <li class="nav-item level-1">
                     <a href="#resources" class="nav-link">
                         <i class="fas fa-archive nav-icon"></i>
                         <span class="nav-title">资源库</span>
                     </a>
                 </li>
            </ul>
        </div>
    </nav>
    
    <!-- 主内容区域 -->
    <main class="content-area sidebar-collapsed"> <!-- Start collapsed on mobile -->
        <!-- 群组信息区 (可选，可以融入标题或移除) -->
        <section class="mb-8 content-section" id="group-info">
            <div class="cyber-card" style="border-color: rgba(212, 66, 255, 0.5);"> <!-- Use tertiary color border -->
                 <h2 class="section-title" style="color: var(--tertiary-neon); border-color: var(--tertiary-neon); text-shadow: 0 0 12px var(--tertiary-neon);">
                     <i class="fas fa-users mr-2"></i><span id="group-name-header">微信群聊</span> 概览
                 </h2>
                 <div class="flex flex-col md:flex-row justify-between gap-4 text-sm mt-4">
                     <p class="text-gray-400" id="date-range">
                         <i class="fas fa-calendar-alt mr-1 text-primary-neon"></i>时间范围：<span class="highlight-primary">2023-01-01</span> 至 <span class="highlight-primary">2023-01-31</span>
                     </p>
                     <div class="flex flex-wrap gap-2">
                         <span class="inline-block px-3 py-1 bg-primary-900/30 text-primary-300 rounded-full text-xs font-mono" id="topic-area" style="background-color: rgba(255, 42, 109, 0.15); color: var(--primary-neon); border: 1px solid rgba(255, 42, 109, 0.3);"><i class="fas fa-tags mr-1"></i> 主题领域</span>
                         <span class="inline-block px-3 py-1 bg-secondary-900/30 text-secondary-300 rounded-full text-xs font-mono" id="contributor-count" style="background-color: rgba(5, 217, 232, 0.15); color: var(--secondary-neon); border: 1px solid rgba(5, 217, 232, 0.3);"><i class="fas fa-users mr-1"></i> 核心贡献者：15</span>
                     </div>
                 </div>
             </div>
        </section>
        
        <!-- 第一部分：讨论热榜 -->
        <section id="hot-topics" class="mb-12 content-section">
            <h2 class="section-title"><i class="fas fa-fire mr-2"></i>讨论热榜</h2>
            
            <!-- 使用Grid布局 -->
            <div class="grid-layout mt-6" id="hot-topics-container">
                <!-- 热榜条目模板 - 会被JavaScript动态填充 -->
                <div class="cyber-card hot-topic-card opacity-0 fade-in"> <!-- Add fade-in classes if needed -->
                    <div class="flex justify-between items-start mb-3">
                        <h3 class="topic-title">AI 模型的最新进展</h3>
                         <span class="topic-rank">#1</span>
                    </div>
                    
                    <div class="mb-4">
                        <div class="heat-indicator-bg w-full mb-1">
                            <div class="heat-indicator" style="width: 92%"></div>
                        </div>
                        <div class="flex justify-between text-xs text-gray-500 dark:text-gray-400 icon-text">
                             <span><i class="fas fa-chart-line"></i> 热度</span>
                             <span class="heat-percentage">92%</span>
                        </div>
                    </div>
                    
                    <p class="text-sm text-gray-600 dark:text-gray-400 mb-4 topic-summary">深入探讨了 <span class="highlight-primary">Transformer 架构</span> 的优化以及 <span class="highlight-secondary">多模态学习</span> 的前沿应用，特别关注了 <span class="highlight-tertiary">效率与成本</span> 的平衡。</p>
                    
                    <div class="flex justify-between text-xs text-gray-500 dark:text-gray-400 icon-text">
                        <span><i class="fas fa-users"></i> <span class="participant-count">18</span> 人参与</span>
                        <span><i class="fas fa-comments"></i> <span class="message-count">67</span> 条消息</span>
                    </div>
                    <a href="#timeline-topic-1" class="details-link hot-topic-link mt-4">
                        <i class="fas fa-arrow-right mr-1"></i> 查看详情
                    </a>
                </div>
                 <!-- 另一个示例 -->
                 <div class="cyber-card hot-topic-card opacity-0 fade-in animate-delay-1">
                    <div class="flex justify-between items-start mb-3">
                        <h3 class="topic-title">前端框架性能优化</h3>
                         <span class="topic-rank">#2</span>
                    </div>
                    <div class="mb-4">
                        <div class="heat-indicator-bg w-full mb-1">
                            <div class="heat-indicator" style="width: 78%"></div>
                        </div>
                        <div class="flex justify-between text-xs text-gray-500 dark:text-gray-400 icon-text">
                             <span><i class="fas fa-chart-line"></i> 热度</span>
                             <span class="heat-percentage">78%</span>
                        </div>
                    </div>
                     <p class="text-sm text-gray-600 dark:text-gray-400 mb-4 topic-summary">集中讨论 <span class="highlight-secondary">React Server Components</span> 与 <span class="highlight-tertiary">Qwik</span> 的对比，以及 <span class="highlight-primary">WebAssembly</span> 在提升计算密集型任务性能方面的潜力。</p>
                    <div class="flex justify-between text-xs text-gray-500 dark:text-gray-400 icon-text">
                        <span><i class="fas fa-users"></i> <span class="participant-count">12</span> 人参与</span>
                        <span><i class="fas fa-comments"></i> <span class="message-count">45</span> 条消息</span>
                    </div>
                     <a href="#timeline-topic-2" class="details-link hot-topic-link mt-4">
                         <i class="fas fa-arrow-right mr-1"></i> 查看详情
                     </a>
                </div>
                <!-- 更多热榜条目将被动态添加 -->
            </div>
        </section>
        
        <!-- 第二部分：时间轴回溯 -->
        <section id="timeline" class="mb-12 content-section">
            <h2 class="section-title"><i class="fas fa-history mr-2"></i>时间轴回溯</h2>
            
            <!-- 时间轴内容区域 -->
            <div id="timeline-content-container" class="mt-6">
                <!-- 时间轴主题1 -->
                 <div id="timeline-topic-1" class="timeline-topic mb-12">
                    <div class="cyber-card timeline-topic-header mb-6">
                         <h3 class="topic-title"><i class="fas fa-comments mr-2"></i>AI 模型的最新进展</h3>
                         <p class="text-sm text-gray-400 mt-2 topic-description">关于 <span class="highlight-primary">Transformer</span> 和 <span class="highlight-secondary">多模态</span> 技术的深度交流...</p>
                         <div class="flex justify-between text-sm text-gray-500 dark:text-gray-400 mt-4 icon-text">
                             <span><i class="fas fa-calendar-alt"></i> <span class="topic-timespan">2023-01-01</span> 至 <span class="topic-timespan">2023-01-05</span></span>
                             <span><i class="fas fa-comment-dots"></i> <span class="topic-message-count">67</span> 条消息</span>
                        </div>
                     </div>
                    
                    <!-- 消息流 -->
                     <div class="messages-flow space-y-4">
                        <!-- 示例消息组 -->
                        <div class="message-group">
                             <div class="text-xs text-gray-500 dark:text-gray-400 mb-1 ml-2 flex items-center">
                                 <span class="font-semibold text-tertiary-neon mr-2">用户 A</span> @ 2023-01-01 10:30:45
                             </div>
                             <div class="message-bubble-container received">
                                 <div class="message-bubble received">
                                    <p>最近 <span class="highlight-primary">GPT-4</span> 的 API 响应速度好像有点波动，大家有遇到吗？</p>
                                 </div>
                             </div>
                             <div class="message-bubble-container received resource-bubble"> <!-- 资源消息 -->
                                <div class="message-bubble received">
                                    <p>看到一篇分析 <span class="highlight-secondary">多模态模型</span> 融合策略的文章，很有启发：</p>
                                    <div class="resource-link-preview">
                                         <span class="resource-type">链接资源</span>
                                         <a href="https://example.com/multimodal-fusion" target="_blank" rel="noopener noreferrer">https://example. Com/multimodal-fusion-strategies-analysis</a>
                                    </div>
                                 </div>
                            </div>
                         </div>
                         
                         <div class="message-group">
                              <div class="text-xs text-gray-500 dark:text-gray-400 mb-1 mr-2 flex items-center justify-end">
                                  <span class="font-semibold text-primary-neon mr-2">用户 B</span> @ 2023-01-01 10:32:18
                              </div>
                             <div class="message-bubble-container sent">
                                 <div class="message-bubble sent">
                                     <p>确实感觉到了！尤其是在高峰期。另外，那篇文章我看过，里面的 <span class="highlight-tertiary">cross-attention</span> 机制讲得很透彻。</p>
                                     <!-- 长文本示例 -->
                                     <div class="long-text mt-2">
                                          <p>补充一点，文章中还提到了一个关于模型剪枝（<span class="highlight-warning">model pruning</span>）的技术，对于部署到资源受限环境非常关键。虽然实现起来比较复杂，需要仔细调整超参数，但带来的性能提升和成本节约是显著的。我们团队正在尝试将其应用于我们的一个内部项目，初步效果还不错，但踩了不少坑，特别是如何保证剪枝后的模型泛化能力不下降太多，这是一个挑战。后面可以分享一些我们的经验教训。这里是关于这个技术的另一个参考资料：<a href="https://example.com/pruning" target="_blank" rel="noopener noreferrer" class="text-secondary-neon hover:underline">Pruning Techniques Overview</a>。</p>
                                     </div>
                                 </div>
                             </div>
                         </div>
                         
                     </div>
                     
                     <!-- 讨论复现区域 -->
                     <div class="discussion-reproduction mt-8">
                         <h4 class="section-subtitle text-lg font-mono font-semibold text-gray-800 dark:text-gray-200 mb-4 flex items-center">
                            <i class="fas fa-lightbulb text-tertiary-neon"></i> 核心讨论与洞察
                         </h4>
                         
                         <div class="debate-view">
                             <div class="view-header">
                                 <span class="view-tag">观点辩论</span>
                                 <span class="view-meta">2023-01-03</span>
                             </div>
                             <div class="view-content">
                                 <p><strong class="text-primary-neon">用户 C:</strong> 认为对于特定任务，<span class="highlight-primary">微调（Fine-tuning）</span>现有大模型比从头训练更具成本效益。</p>
                                  <p><strong class="text-secondary-neon">用户 D:</strong> 反驳说，对于高度定制化的需求，从头训练虽然昂贵，但能更好地控制模型行为，避免 <span class="highlight-warning">灾难性遗忘</span> 问题。</p>
                             </div>
                         </div>
                         
                         <div class="consensus-view">
                              <div class="view-header">
                                 <span class="view-tag">达成共识</span>
                                 <span class="view-meta">2023-01-04</span>
                             </div>
                             <div class="view-content">
                                 <p>最终大家认为，选择微调还是从头训练，取决于 <span class="highlight-secondary">数据量</span>、<span class="highlight-tertiary">任务复杂度</span> 和 <span class="highlight-primary">预算限制</span>。对于大多数场景，有效的微调策略（如 <span class="highlight-secondary">LoRA</span>）是更优的选择。</p>
                             </div>
                         </div>
                         
                         <div class="insight-view">
                              <div class="view-header">
                                 <span class="view-tag">核心原理</span>
                                 <span class="view-meta">洞察提取</span>
                             </div>
                             <div class="view-content">
                                  <p>讨论揭示了 <span class="highlight-primary">模型适应性</span> 与 <span class="highlight-tertiary">训练成本</span> 之间的核心权衡。关键在于理解不同技术（微调、预训练、提示工程）的应用边界和优劣势。</p>
                             </div>
                         </div>
                     </div>
                 </div> <!-- End Timeline Topic 1 -->
                 
                 <!-- 时间轴主题2 (示例结构) -->
                 <div id="timeline-topic-2" class="timeline-topic mb-12">
                      <div class="cyber-card timeline-topic-header mb-6">
                          <h3 class="topic-title"><i class="fas fa-code mr-2"></i>前端框架性能优化</h3>
                          <p class="text-sm text-gray-400 mt-2 topic-description">关于 <span class="highlight-secondary">RSC</span>, <span class="highlight-tertiary">Qwik</span>, 和 <span class="highlight-primary">WASM</span> 的性能讨论...</p>
                          <div class="flex justify-between text-sm text-gray-500 dark:text-gray-400 mt-4 icon-text">
                              <span><i class="fas fa-calendar-alt"></i> <span class="topic-timespan">2023-01-06</span> 至 <span class="topic-timespan">2023-01-10</span></span>
                              <span><i class="fas fa-comment-dots"></i> <span class="topic-message-count">45</span> 条消息</span>
                          </div>
                      </div>
                      <!-- ... 消息流和讨论复现 ... -->
                       <div class="messages-flow space-y-4">
                            <div class="message-group">
                                 <div class="text-xs text-gray-500 dark:text-gray-400 mb-1 ml-2 flex items-center">
                                     <span class="font-semibold text-secondary-neon mr-2">用户 E</span> @ 2023-01-06 14:05:11
                                 </div>
                                 <div class="message-bubble-container received">
                                     <div class="message-bubble received">
                                        <p>大家怎么看 <span class="highlight-secondary">React Server Components (RSC)</span> 的前景？感觉概念很酷，但实际落地会不会有很多坑？</p>
                                     </div>
                                 </div>
                             </div>
                            <div class="message-group">
                                  <div class="text-xs text-gray-500 dark:text-gray-400 mb-1 mr-2 flex items-center justify-end">
                                      <span class="font-semibold text-tertiary-neon mr-2">用户 F</span> @ 2023-01-06 14:10:35
                                  </div>
                                 <div class="message-bubble-container sent">
                                     <div class="message-bubble sent">
                                         <p>我更看好 <span class="highlight-tertiary">Qwik</span> 的 <span class="highlight-warning">resumability</span> 概念，感觉从根本上解决了 hydration 的问题。RSC 感觉还是有点绕。</p>
                                         <p class="mt-2">这里有个对比文章，写得不错：<a href="https://example.com/rsc-vs-qwik" target="_blank" rel="noopener noreferrer" class="text-secondary-neon hover:underline">RSC vs Qwik In-Depth</a></p>
                                     </div>
                                 </div>
                             </div>
                       </div>
                 </div> <!-- End Timeline Topic 2 -->
                 
                 <!-- 更多主题将被动态添加 -->
            </div>
        </section>
        
        <!-- 第三部分：资源库 -->
        <section id="resources" class="mb-12 content-section">
            <h2 class="section-title"><i class="fas fa-archive mr-2"></i>资源库</h2>
            
            <!-- 筛选工具栏 -->
            <div class="cyber-card filter-toolbar mb-6">
                <div class="search-box flex-grow">
                    <div class="relative">
                        <i class="fas fa-search absolute left-3 top-1/2 -translate-y-1/2 text-gray-400 dark:text-gray-500"></i>
                        <input type="text" id="resource-search" placeholder="搜索资源标题、描述或标签..." class="w-full">
                    </div>
                </div>
                
                <div class="filter-buttons flex flex-wrap gap-2">
                    <button class="resource-filter-btn active" data-filter="all">全部</button>
                    <button class="resource-filter-btn" data-filter="link"><i class="fas fa-link mr-1"></i>链接</button>
                    <button class="resource-filter-btn" data-filter="file"><i class="fas fa-file mr-1"></i>文件</button>
                    <button class="resource-filter-btn" data-filter="image"><i class="fas fa-image mr-1"></i>图片</button>
                    <button class="resource-filter-btn" data-filter="video"><i class="fas fa-video mr-1"></i>视频</button>
                </div>
            </div>
            
            <!-- 资源卡片网格 -->
            <div class="grid-layout" id="resources-container">
                <!-- 资源卡片模板 - 会被JavaScript动态填充 -->
                <div class="cyber-card resource-card" data-resource-type="link">
                    <div class="flex items-start justify-between mb-3">
                        <div class="resource-type-badge"><i class="fas fa-link mr-1"></i> 链接</div>
                        <span class="text-xs text-gray-500 dark:text-gray-400">2023-01-01</span>
                    </div>
                    
                    <h3 class="resource-title mb-2">多模态融合策略分析</h3>
                    <p class="resource-description">深入分析了各种多模态数据融合技术，特别是 <span class="highlight-secondary">cross-attention</span> 机制。</p>
                    
                    <div class="resource-meta mb-3">
                        <span><i class="fas fa-user"></i> 分享者：用户 A</span>
                        <a href="https://example.com/multimodal-fusion" class="text-secondary-neon hover:underline text-sm font-medium" target="_blank" rel="noopener noreferrer">访问资源 <i class="fas fa-external-link-alt text-xs ml-1"></i></a>
                    </div>
                    
                    <div class="resource-tags">
                         <span class="highlight-primary">AI</span>
                         <span class="highlight-secondary">多模态</span>
                         <span>深度学习</span>
                         <span>教程</span>
                     </div>
                    <a href="#timeline-topic-1" class="context-link resource-context-link mt-4" data-resource-id="resource-1" data-context-id="timeline-topic-1">
                        <i class="fas fa-history mr-1"></i> 查看上下文
                    </a>
                </div>
                
                <div class="cyber-card resource-card" data-resource-type="link">
                    <div class="flex items-start justify-between mb-3">
                         <div class="resource-type-badge"><i class="fas fa-link mr-1"></i> 链接</div>
                         <span class="text-xs text-gray-500 dark:text-gray-400">2023-01-06</span>
                    </div>
                    <h3 class="resource-title mb-2">RSC vs Qwik 深度对比</h3>
                     <p class="resource-description">详细比较了 <span class="highlight-secondary">React Server Components</span> 和 <span class="highlight-tertiary">Qwik</span> 的核心机制和性能表现。</p>
                     <div class="resource-meta mb-3">
                         <span><i class="fas fa-user"></i> 分享者：用户 F</span>
                         <a href="https://example.com/rsc-vs-qwik" class="text-secondary-neon hover:underline text-sm font-medium" target="_blank" rel="noopener noreferrer">访问资源 <i class="fas fa-external-link-alt text-xs ml-1"></i></a>
                     </div>
                     <div class="resource-tags">
                         <span class="highlight-secondary">前端</span>
                         <span class="highlight-tertiary">性能优化</span>
                         <span>React</span>
                         <span>Qwik</span>
                         <span>对比</span>
                     </div>
                     <a href="#timeline-topic-2" class="context-link resource-context-link mt-4" data-resource-id="resource-2" data-context-id="timeline-topic-2">
                         <i class="fas fa-history mr-1"></i> 查看上下文
                     </a>
                </div>
                 <!-- 更多资源卡片将被动态添加 -->
            </div>
        </section>
    </main>
    
    <!-- 页脚 -->
    <footer class="cyber-footer">
        <div class="container">
             <div>
                 <h2 class="footer-title">微信群聊知识平台</h2>
                 <p class="footer-subtitle">深度分析 · 知识萃取 · 洞察沉淀</p>
            </div>
            <div class="footer-meta">
                 <span>数据来源：<span id="footer-group-name" class="text-primary-neon">微信群聊</span> 记录</span> |
                 <span>分析时间：<span id="footer-date" class="text-secondary-neon">2023-01-31</span></span>
             </div>
             <p class="footer-disclaimer">
                 本平台由 AI 生成，旨在提取有价值信息，但不保证绝对精确性。请结合原始上下文审慎判断。
             </p>
        </div>
    </footer>
    
    <!-- JavaScript -->
    <script>
        Document.AddEventListener ('DOMContentLoaded', function () {
            // ===============================
            // 中文编码处理 (保留作为理论上的保障)
            // ===============================
            Function ensureUtf 8 (text) {
                Try {
                    // 简单的检查，实际应用中 UTF-8 通常是默认且正确的
                    Return text; 
                } catch (e) {
                    Console.Warn ('字符编码处理可能存在问题: ', e);
                    Return text;
                }
            }
            
            // ===============================
            // 侧边栏导航功能 (Cyberpunk Style)
            // ===============================
            Const sidebar = document.QuerySelector ('. Cyber-sidebar');
            Const contentArea = document.QuerySelector ('. Content-area');
            Const mobileToggle = document.QuerySelector ('. Mobile-toggle');
            const navLinks = document.QuerySelectorAll ('. Nav-item a.nav-link'); // Select only actual links
            Const navHeaders = document.QuerySelectorAll ('. Nav-header');
            Const body = document. Body;

            // --- 移动端切换 ---
            If (mobileToggle) {
                MobileToggle.AddEventListener ('click', function () {
                    Const isOpen = sidebar.ClassList.Contains ('open');
                    If (isOpen) {
                        Sidebar.ClassList.Remove ('open');
                        Sidebar.ClassList.Add ('collapsed');
                        ContentArea.ClassList.Remove ('sidebar-open'); // Use for content adjustments if needed
                        ContentArea.ClassList.Add ('sidebar-collapsed');
                        Body.ClassList.Remove ('sidebar-open');
                        mobileToggle. InnerHTML = '<i class="fas fa-bars"></i>';
                    } else {
                        Sidebar.ClassList.Remove ('collapsed');
                        Sidebar.ClassList.Add ('open');
                        ContentArea.ClassList.Add ('sidebar-open');
                        ContentArea.ClassList.Remove ('sidebar-collapsed');
                        Body.ClassList.Add ('sidebar-open'); // Add class to body
                        mobileToggle. InnerHTML = '<i class="fas fa-times"></i>';
                    }
                });
            }

            // --- 点击内容区域关闭移动端导航 (仅在移动视图) ---
            If (contentArea) {
                 ContentArea.AddEventListener ('click', function () {
                     If (window. InnerWidth <= 768 && sidebar.ClassList.Contains ('open')) {
                         Sidebar.ClassList.Remove ('open');
                         Sidebar.ClassList.Add ('collapsed');
                         ContentArea.ClassList.Remove ('sidebar-open');
                         ContentArea.ClassList.Add ('sidebar-collapsed');
                         Body.ClassList.Remove ('sidebar-open');
                         if (mobileToggle) mobileToggle. InnerHTML = '<i class="fas fa-bars"></i>';
                     }
                 });
            }
            
            // --- 导航折叠 ---
            NavHeaders.ForEach (header => {
                 Const toggleBtn = header.QuerySelector ('. Toggle-btn');
                 Const parentItem = header.Closest ('. Nav-item');
                 Const submenu = parentItem ? ParentItem.QuerySelector ('. Nav-submenu') : null;

                 If (toggleBtn && submenu) {
                    Header.AddEventListener ('click', function (e) {
                        // Allow clicking links within headers if any exist in future
                        if (e.target. TagName === 'A') return; 

                        Submenu.ClassList.Toggle ('open');
                        ToggleBtn. TextContent = submenu.ClassList.Contains ('open') ? '-' : '+';
                    });
                 }
            });

             // --- 激活父菜单函数 ---
            Function openParentMenus (element) {
                Let parentSubmenu = element.Closest ('. Nav-submenu');
                While (parentSubmenu) {
                    If (! ParentSubmenu.ClassList.Contains ('open')) {
                         ParentSubmenu.ClassList.Add ('open');
                         Const parentHeader = parentSubmenu. PreviousElementSibling;
                         If (parentHeader && parentHeader.ClassList.Contains ('nav-header')) {
                            Const toggleBtn = parentHeader.QuerySelector ('. Toggle-btn');
                             If (toggleBtn) {
                                ToggleBtn. TextContent = '-';
                             }
                         }
                     }
                     // Move up the hierarchy
                     Const grandParentItem = parentSubmenu.Closest ('. Nav-item');
                     ParentSubmenu = grandParentItem ? GrandParentItem.Closest ('. Nav-submenu') : null;
                }
            }
            
             // --- 导航链接点击处理 (平滑滚动 & 激活) ---
            NavLinks.ForEach (link => {
                Link.AddEventListener ('click', function (e) {
                    e.preventDefault ();
                    Const targetId = this.GetAttribute ('href'). Substring (1);
                    Const targetElement = document.GetElementById (targetId);

                    If (targetElement) {
                         // 1. 移除所有激活状态
                        navLinks.ForEach (l => l.classList.Remove ('active'));
                         // 2. 添加当前链接激活状态
                         This.ClassList.Add ('active');
                         // 3. 确保父菜单展开
                         OpenParentMenus (this);

                         // 4. 平滑滚动
                         Const offsetTop = targetElement. OffsetTop - 70; // Adjust offset as needed
                         Window.ScrollTo ({
                            Top: offsetTop,
                            Behavior: 'smooth'
                         });
                         
                         // 5. 临时高亮目标区域
                         TargetElement.ClassList.Add ('target-highlight'); // Use secondary neon glow
                         SetTimeout (() => {
                            TargetElement.ClassList.Remove ('target-highlight');
                         }, 2000);

                         // 6. 关闭移动端菜单 (如果打开)
                         If (window. InnerWidth <= 768 && sidebar.ClassList.Contains ('open')) {
                            Sidebar.ClassList.Remove ('open');
                            Sidebar.ClassList.Add ('collapsed');
                            ContentArea.ClassList.Remove ('sidebar-open');
                            ContentArea.ClassList.Add ('sidebar-collapsed');
                            Body.ClassList.Remove ('sidebar-open');
                             if (mobileToggle) mobileToggle. InnerHTML = '<i class="fas fa-bars"></i>';
                         }
                    } else {
                         Console.Warn (`Target element not found for link: ${targetId}`);
                    }
                });
            });

             // --- 滚动监听，自动激活导航 ---
             Window.AddEventListener ('scroll', function () {
                Const scrollPosition = window. ScrollY + window. InnerHeight / 3; // Adjust detection point
                Let currentSectionId = null;

                Document.QuerySelectorAll ('. Content-section'). ForEach (section => {
                    Const sectionTop = section. OffsetTop;
                    Const sectionBottom = sectionTop + section. OffsetHeight;
                     // Check if the detection point is within this section
                     If (scrollPosition >= sectionTop && scrollPosition < sectionBottom) {
                        CurrentSectionId = section.GetAttribute ('id');
                    }
                });
                
                // Also check timeline topics specifically if general sections aren't matching well
                If (! CurrentSectionId) {
                    Document.QuerySelectorAll ('. Timeline-topic'). ForEach (topic => {
                         Const topicTop = topic. OffsetTop;
                         Const topicBottom = topicTop + topic. OffsetHeight;
                         If (scrollPosition >= topicTop && scrollPosition < topicBottom) {
                            CurrentSectionId = topic.GetAttribute ('id');
                         }
                    });
                 }

                NavLinks.ForEach (link => {
                     Link.ClassList.Remove ('active');
                     If (currentSectionId && link.GetAttribute ('href') === `#${currentSectionId}`) {
                         Link.ClassList.Add ('active');
                         // Optionally ensure parents are open on scroll activation
                         OpenParentMenus (link); 
                     }
                 });
            }, { passive: true }); // Use passive listener for performance

            // ===============================
            // 热榜跳转优化 (Similar to nav link handling)
            // ===============================
            Function enhanceHotTopicsNavigation () {
                Document.QuerySelectorAll ('. Hot-topic-link'). ForEach (link => {
                    Link.AddEventListener ('click', function (e) {
                        e.preventDefault ();
                        Const targetId = this.GetAttribute ('href'). Substring (1);
                        Const targetElement = document.GetElementById (targetId);
                        Const correspondingNavLink = document.QuerySelector (`. Nav-item a[href="#${targetId}"]`);

                        If (targetElement) {
                            // 平滑滚动
                             Const offsetTop = targetElement. OffsetTop - 70;
                             Window.ScrollTo ({
                                Top: offsetTop,
                                Behavior: 'smooth'
                             });
                            
                             // 目标高亮
                            TargetElement.ClassList.Add ('highlight-target'); // Use primary neon glow
                            SetTimeout (() => {
                                TargetElement.ClassList.Remove ('highlight-target');
                            }, 2000);

                            // 激活侧边栏对应链接
                             If (correspondingNavLink) {
                                navLinks.ForEach (l => l.classList.Remove ('active'));
                                CorrespondingNavLink.ClassList.Add ('active');
                                OpenParentMenus (correspondingNavLink);
                            }
                             // 关闭移动端菜单 (如果打开)
                             If (window. InnerWidth <= 768 && sidebar.ClassList.Contains ('open')) {
                                Sidebar.ClassList.Remove ('open');
                                Sidebar.ClassList.Add ('collapsed');
                                ContentArea.ClassList.Remove ('sidebar-open');
                                ContentArea.ClassList.Add ('sidebar-collapsed');
                                Body.ClassList.Remove ('sidebar-open');
                                if (mobileToggle) mobileToggle. InnerHTML = '<i class="fas fa-bars"></i>';
                            }
                        } else {
                            Console.Warn (`Target element not found for hot topic link: ${targetId}`);
                        }
                    });
                });
            }

            // ===============================
            // 资源链接检查与跳转 (Context Links)
            // ===============================
            Function validateAndFixResourceLinks () {
                Document.QuerySelectorAll ('. Resource-context-link'). ForEach (link => {
                    Const targetId = link.GetAttribute ('href')?.Substring (1);
                    
                    If (! TargetId) {
                        Console.Warn ('Resource context link missing href: ', link);
                        Return;
                    }

                    Let targetElement = document.GetElementById (targetId);
                    
                    // Basic check: if target doesn't exist, log warning (more complex fixing might be needed)
                    If (! TargetElement) {
                        Console.Warn (`Resource context link target missing: #${targetId}. Link might be broken.`);
                        // Optionally disable the link or point to a default location
                        // link. Style. Opacity = '0.5';
                        // link. Style. PointerEvents = 'none';
                    }

                    Link.AddEventListener ('click', function (e) {
                        e.preventDefault ();
                        TargetElement = document.GetElementById (targetId); // Re-check element existence on click
                        Const correspondingNavLink = document.QuerySelector (`. Nav-item a[href="#${targetId}"]`);

                        If (targetElement) {
                             // 平滑滚动
                             Const offsetTop = targetElement. OffsetTop - 70;
                             Window.ScrollTo ({
                                Top: offsetTop,
                                Behavior: 'smooth'
                             });
                            
                             // 目标高亮
                            TargetElement.ClassList.Add ('target-highlight'); // Use secondary neon glow
                            SetTimeout (() => {
                                TargetElement.ClassList.Remove ('target-highlight');
                            }, 2000);

                            // 激活侧边栏对应链接
                             If (correspondingNavLink) {
                                navLinks.ForEach (l => l.classList.Remove ('active'));
                                CorrespondingNavLink.ClassList.Add ('active');
                                OpenParentMenus (correspondingNavLink);
                            }
                             // 关闭移动端菜单 (如果打开)
                             If (window. InnerWidth <= 768 && sidebar.ClassList.Contains ('open')) {
                                Sidebar.ClassList.Remove ('open');
                                Sidebar.ClassList.Add ('collapsed');
                                ContentArea.ClassList.Remove ('sidebar-open');
                                ContentArea.ClassList.Add ('sidebar-collapsed');
                                Body.ClassList.Remove ('sidebar-open');
                                if (mobileToggle) mobileToggle. InnerHTML = '<i class="fas fa-bars"></i>';
                            }
                        } else {
                             Console.Error (`Target element #${targetId} not found on click!`);
                             // Maybe show an error message to the user
                        }
                    });
                });
            }
            
            // ===============================
            // 长文本处理优化
            // ===============================
            Function optimizeLongTextContent () {
                Document.QuerySelectorAll ('. Long-text p, .message-bubble p'). ForEach (container => {
                    // Avoid processing already processed containers
                    If (container.Closest ('. Collapsible-text')) return;
                    
                    Const text = container. TextContent || '';
                    Const MAX_LENGTH = 250; // Adjust threshold

                    If (text. Length > MAX_LENGTH) {
                        Const fullText = container. InnerHTML; // Preserve HTML like links/highlights
                        Const truncatedText = text.Substring (0, MAX_LENGTH) + '...'; // Plain text for display

                        // Create wrapper
                        Const wrapper = document.CreateElement ('div');
                        Wrapper. ClassName = 'collapsible-text';

                        // Content element (use innerHTML for truncated version initially, then full)
                        Const contentElement = document.CreateElement ('div'); // Use div to hold potential HTML
                        ContentElement. InnerHTML = truncatedText; // Show truncated plain text initially

                        // Toggle button
                        Const toggleButton = document.CreateElement ('button');
                        ToggleButton. TextContent = '展开全文';
                        ToggleButton.SetAttribute ('data-expanded', 'false');

                        // Click event
                        ToggleButton.AddEventListener ('click', function () {
                            Const isExpanded = this.GetAttribute ('data-expanded') === 'true';
                            If (isExpanded) {
                                ContentElement. InnerHTML = truncatedText; // Revert to truncated text
                                This. TextContent = '展开全文';
                                This.SetAttribute ('data-expanded', 'false');
                            } else {
                                ContentElement. InnerHTML = fullText; // Show full original HTML
                                This. TextContent = '收起全文';
                                This.SetAttribute ('data-expanded', 'true');
                            }
                        });

                        // Assemble
                        Wrapper.AppendChild (contentElement);
                        Wrapper.AppendChild (toggleButton);

                        // Replace original paragraph
                        Container.ReplaceWith (wrapper);
                    }
                });
            }

             // ===============================
             // 资源筛选
             // ===============================
            Function setupResourceFiltering () {
                Const filterButtons = document.QuerySelectorAll ('. Resource-filter-btn');
                const resourceCards = document.QuerySelectorAll (' #resources-container .resource-card');
                Const searchInput = document.GetElementById ('resource-search');

                 Let currentFilter = 'all';
                 Let currentSearchTerm = '';

                 Function applyFilters () {
                    ResourceCards.ForEach (card => {
                        Const type = card.GetAttribute ('data-resource-type') || 'unknown';
                        Const title = card.QuerySelector ('. Resource-title')?.TextContent.ToLowerCase () || '';
                        Const description = card.QuerySelector ('. Resource-description')?.TextContent.ToLowerCase () || '';
                        Const tags = Array.From (card.QuerySelectorAll ('. Resource-tags span')). Map (tag => tag.TextContent.ToLowerCase ()). Join (' ');
                        
                         Const typeMatch = (currentFilter === 'all' || type === currentFilter);
                         Const searchMatch = (currentSearchTerm === '' || 
                                             Title.Includes (currentSearchTerm) || 
                                             Description.Includes (currentSearchTerm) ||
                                             Tags.Includes (currentSearchTerm));

                         If (typeMatch && searchMatch) {
                            Card. Style. Display = ''; // Show card
                        } else {
                            Card. Style. Display = 'none'; // Hide card
                        }
                    });
                 }

                // Filter button clicks
                FilterButtons.ForEach (button => {
                    Button.AddEventListener ('click', function () {
                        FilterButtons.ForEach (btn => btn.ClassList.Remove ('active'));
                        This.ClassList.Add ('active');
                        CurrentFilter = this.GetAttribute ('data-filter');
                        ApplyFilters ();
                    });
                });

                // Search input handling
                 If (searchInput) {
                    SearchInput.AddEventListener ('input', function () {
                        CurrentSearchTerm = this.Value.ToLowerCase (). Trim ();
                        ApplyFilters ();
                    });
                 }
                 
                 // Initial application
                 ApplyFilters ();
            }

            // ===============================
            // 初始化函数调用
            // ===============================
            
             // Placeholder for dynamically adding timeline topics to sidebar
             Function populateTimelineNav () {
                 Const timelineTopicsContainer = document.GetElementById ('timeline-topics');
                 Const placeholderItems = timelineTopicsContainer.QuerySelectorAll ('. Placeholder');
                 
                 // Clear placeholders if actual data will be loaded
                 // placeholderItems.ForEach (item => item.Remove ()); 
                 
                 // Example: Add items dynamically if needed
                 // const topicData = [{id: 'timeline-topic-1', title: 'AI Models'}, {id: 'timeline-topic-2', title: 'Frontend Perf'}];
                 // topicData.ForEach ((topic, index) => {
                 //    const li = document.CreateElement ('li');
                 //    li. ClassName = 'nav-item level-2';
                 //    li. InnerHTML = `<a href="#${topic.id}" class="nav-link">${index + 1}. ${topic. Title}</a>`;
                 //    timelineTopicsContainer.AppendChild (li);
                 // });
                 
                 // Re-select navLinks AFTER dynamic population if it happens
                 // navLinks = document.QuerySelectorAll ('. Nav-item a.nav-link'); 
                 // Re-add event listeners to newly added links
             }
             
             PopulateTimelineNav (); // Call placeholder/dynamic population
             EnhanceHotTopicsNavigation ();
             ValidateAndFixResourceLinks ();
             OptimizeLongTextContent ();
             SetupResourceFiltering ();
             
             // Initial scroll spy check
             Window.DispatchEvent (new Event ('scroll'));
             
             // Initial check for mobile view state
             If (window. InnerWidth > 768) {
                 Sidebar.ClassList.Remove ('collapsed');
                 Sidebar.ClassList.Add ('open');
                 ContentArea.ClassList.Remove ('sidebar-collapsed');
                 ContentArea.ClassList.Add ('sidebar-open');
             } else {
                 Sidebar.ClassList.Add ('collapsed');
                 Sidebar.ClassList.Remove ('open');
                 ContentArea.ClassList.Add ('sidebar-collapsed');
                 ContentArea.ClassList.Remove ('sidebar-open');
                 Body.ClassList.Remove ('sidebar-open'); // Ensure body class is correct initially
             }

            // ===============================
            // 模拟数据和分析占位符
            // ===============================
            Console.Log ('Cyberpunk WeChat Analyzer Initialized...');
            // loadChatData ();
            // analyzeHotTopics ();
            // buildTimeline ();
            // populateResourceLibrary ();
        });
    </script>
</body>
</html>
## 交付成果

提供包含以下内容的完整解决方案：

1. 单一HTML文件，包含所有必要CSS和JavaScript（避免外部依赖）
2. 确保能在现代浏览器中流畅运行
3. 确保所有链接和导航功能正常工作
4. 确保所有中文字符正确显示，无乱码
5. 提供详细注释，确保代码可维护性

注意：当你生成完整HTML文件时，请不要添加任何额外解释或介绍，直接输出HTML代码。确保所有提及的功能都已实现，没有仅仅是占位符的代码片段。需要展示你最强大的网页开发和数据可视化能力。