import re

with open('index.html', 'r') as f:
    content = f.read()

projects_section = """        <!-- Projects Gallery -->
        <section id="work" class="py-32 bg-[#050505]">
            <div class="max-w-7xl mx-auto px-6 space-y-24">
                <div class="flex flex-col md:flex-row md:justify-between md:items-end gap-8 w-full">
                    <div class="space-y-4">
                        <span class="text-[10px] font-black uppercase tracking-[0.6em] text-orange-500">Portfolio</span>
                        <h2 class="text-6xl md:text-8xl font-black tracking-tighter italic text-white">Selected Work.</h2>
                    </div>
                    
                    <div class="relative min-w-[280px]">
                        <select id="project-filter" class="w-full bg-[#111112] text-white border border-white/10 rounded-xl px-6 py-4 appearance-none outline-none focus:border-white/30 transition-colors font-bold text-sm tracking-widest uppercase cursor-pointer shadow-xl">
                            <option value="all">All Projects</option>
                            <option value="web">Web Development</option>
                            <option value="ml">Data Science & AI</option>
                            <option value="iot">IOT</option>
                        </select>
                        <i data-lucide="chevron-down" class="absolute right-6 top-1/2 -translate-y-1/2 w-5 h-5 text-white/50 pointer-events-none"></i>
                    </div>
                </div>

                <div id="projects-container" class="space-y-24">

                    <!-- Artisan's Canvas -->
                    <div class="project-item grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-16 items-center reveal" data-category="web">
                        <div class="lg:col-span-5 space-y-8 order-2 lg:order-1 text-left">
                            <span class="text-blue-500 font-black text-xs uppercase tracking-[0.5em]">Freelancing / Client Work</span>
                            <h3 class="text-4xl md:text-5xl font-bold tracking-tighter italic text-white">Artisan's Canvas</h3>
                            <p class="text-xl text-white/50 leading-relaxed">
                                Developed a digital storefront for local artists who lacked a platform to showcase their portfolios and receive community feedback.                        
                            </p>
                            <div class="flex flex-wrap gap-2 pt-2">
                                <div class="tech-tag"><i class="devicon-html5-plain colored"></i><span>HTML5</span></div>
                                <div class="tech-tag"><i class="devicon-tailwindcss-plain colored"></i><span>Tailwind</span></div>
                                <div class="tech-tag"><i class="devicon-javascript-plain colored"></i><span>Javascript</span></div>
                                <div class="tech-tag"><i class="devicon-firebase-plain colored"></i><span>Firebase</span></div>
                            </div>
                            <div class="flex flex-wrap gap-4 pt-4">
                                <a href="https://canvas-art-five.vercel.app/" target="_blank" class="px-8 py-3 bg-white text-black rounded-full font-bold text-xs uppercase tracking-widest btn-apple flex items-center gap-2">
                                    Launch Site <i data-lucide="external-link"></i>
                                </a>
                                <a href="https://github.com/abhishek18-blog/canvas-art" target="_blank" class="px-8 py-3 bg-white/5 border border-white/10 rounded-full font-bold text-xs uppercase tracking-widest hover:bg-white/10 transition-all flex items-center gap-2">
                                    Repo <i data-lucide="github"></i>
                                </a>
                            </div>
                        </div>
                        <div class="lg:col-span-7 order-1 lg:order-2">
                            <div class="bento-card aspect-video group overflow-hidden border-blue-500/20 shadow-[0_0_80px_rgba(0,113,227,0.1)]">
                                <img src="canvas.png" class="w-full h-full object-cover transition-all duration-1000 group-hover:scale-105" onerror="this.src='https://images.unsplash.com/photo-1558655146-d09347e92766?q=80&w=1964&auto=format&fit=crop'">
                            </div>
                        </div>
                    </div>

                    <!--NovelAI Web Application  -->
                    <div class="project-item grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-16 items-center reveal" data-category="ml">
                        <div class="lg:col-span-7">
                            <div class="bento-card aspect-video group overflow-hidden border-purple-500/20 shadow-[0_0_80px_rgba(168,85,247,0.1)]">
                                <img src="novel1.png" class="w-full h-full object-cover transition-all duration-1000 group-hover:scale-105" onerror="this.src='https://images.unsplash.com/photo-1677442136019-21780ecad995?q=80&w=2070&auto=format&fit=crop'">
                            </div>
                        </div>
                        <div class="lg:col-span-5 space-y-8 text-left">
                            <span class="text-purple-500 font-black text-xs uppercase tracking-[0.5em]">AI Reading Ecosystem</span>
                            <h3 class="text-4xl md:text-5xl font-bold tracking-tighter italic text-white">NovelAI</h3>
                            <p class="text-xl text-white/50 leading-relaxed">
                                An intelligent PDF reader featuring <b>Gemini AI</b> for real-time storytelling analysis, live language translation, and automated progress tracking. Securely sync your library and reading history via <b>Firebase</b>.
                            </p>
                            <div class="flex flex-wrap gap-2 pt-2">
                                <div class="tech-tag"><i class="devicon-python-plain colored"></i><span>Python</span></div>
                                <div class="tech-tag"><i class="devicon-googlecloud-plain colored"></i><span>Gemini AI</span></div>
                                <div class="tech-tag"><i class="devicon-react-original colored"></i><span>React</span></div>
                                <div class="tech-tag"><i class="devicon-javascript-plain colored"></i><span>Javascript</span></div>
                                <div class="tech-tag"><i class="devicon-firebase-plain colored"></i><span>Firebase</span></div>
                                
                            </div>
                            <div class="flex flex-wrap gap-4 pt-4">
                                <a href="https://novel-ai-gem.vercel.app/" target="_blank" class="px-8 py-3 bg-white text-black rounded-full font-bold text-xs uppercase tracking-widest btn-apple flex items-center gap-2">
                                    Launch Site <i data-lucide="external-link"></i>
                                </a>
                                <a href="https://github.com/abhishek18-blog/NovelAI-Gem/" target="_blank" class="px-8 py-3 bg-white/5 border border-white/10 rounded-full font-bold text-xs uppercase tracking-widest hover:bg-white/10 transition-all flex items-center gap-2">
                                    Repo <i data-lucide="github"></i>
                                </a>
                            </div>
                        </div>
                    </div>

                    <!-- Fish Disease Detection -->
                    <div class="project-item grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-16 items-center reveal" data-category="ml">
                        <div class="lg:col-span-5 space-y-8 order-2 lg:order-1 text-left">
                            <span class="text-teal-500 font-black text-xs uppercase tracking-[0.5em]">Data Science & AI</span>
                            <h3 class="text-4xl md:text-5xl font-bold tracking-tighter italic text-white">Fish Disease Detection</h3>
                            <p class="text-xl text-white/50 leading-relaxed">
                                A machine learning system to diagnose fish diseases using Convolutional Neural Networks (CNN), providing real-time health analysis and treatment recommendations.
                            </p>
                            <div class="flex flex-wrap gap-2 pt-2">
                                <div class="tech-tag"><i class="devicon-python-plain colored"></i><span>Python</span></div>
                                <div class="tech-tag"><i class="devicon-pytorch-plain colored"></i><span>PyTorch</span></div>
                                <div class="tech-tag"><i class="devicon-streamlit-plain colored"></i><span>Streamlit</span></div>
                            </div>
                            <div class="flex flex-wrap gap-4 pt-4">
                                <a href="https://github.com/abhishek18-blog/fish-disease-detection" target="_blank" class="px-8 py-3 bg-white/5 border border-white/10 rounded-full font-bold text-xs uppercase tracking-widest hover:bg-white/10 transition-all flex items-center gap-2">
                                    Repo <i data-lucide="github"></i>
                                </a>
                            </div>
                        </div>
                        <div class="lg:col-span-7 order-1 lg:order-2">
                            <div class="bento-card aspect-video group overflow-hidden border-teal-500/20 shadow-[0_0_80px_rgba(20,184,166,0.1)]">
                                <img src="fish_disease.png" class="w-full h-full object-cover transition-all duration-1000 group-hover:scale-105" onerror="this.src='https://images.unsplash.com/photo-1524704654690-b56c05c78a00?q=80&w=2070&auto=format&fit=crop'">
                            </div>
                        </div>
                    </div>

                    <!-- Agritech-IOT -->
                    <div class="project-item grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-16 items-center reveal" data-category="iot">
                        <div class="lg:col-span-7">
                            <div class="bento-card aspect-video group overflow-hidden border-green-500/20 shadow-[0_0_80px_rgba(34,197,94,0.1)]">
                                <img src="agritech.png" class="w-full h-full object-cover transition-all duration-1000 group-hover:scale-105" onerror="this.src='https://images.unsplash.com/photo-1625246333195-78d9c38ad449?q=80&w=2070&auto=format&fit=crop'">
                            </div>
                        </div>
                        <div class="lg:col-span-5 space-y-8 text-left">
                            <span class="text-green-500 font-black text-xs uppercase tracking-[0.5em]">IOT & Embedded Systems</span>
                            <h3 class="text-4xl md:text-5xl font-bold tracking-tighter italic text-white">Smart Agriculture</h3>
                            <p class="text-xl text-white/50 leading-relaxed">
                                An IoT-based automated irrigation system that utilizes ESP8266 and various sensors to monitor soil moisture and weather conditions, integrating with the Blynk app for remote control.
                            </p>
                            <div class="flex flex-wrap gap-2 pt-2">
                                <div class="tech-tag"><i class="devicon-arduino-plain colored"></i><span>Arduino</span></div>
                                <div class="tech-tag"><i class="devicon-cplusplus-plain colored"></i><span>C++</span></div>
                                <div class="tech-tag"><i data-lucide="radio" class="w-4 h-4 text-green-400"></i><span>Sensors</span></div>
                            </div>
                            <div class="flex flex-wrap gap-4 pt-4">
                                <a href="https://github.com/abhishek18-blog/Agritech-IOT" target="_blank" class="px-8 py-3 bg-white/5 border border-white/10 rounded-full font-bold text-xs uppercase tracking-widest hover:bg-white/10 transition-all flex items-center gap-2">
                                    Repo <i data-lucide="github"></i>
                                </a>
                            </div>
                        </div>
                    </div>

                    <!-- Natural Language to SQL -->
                    <div class="project-item grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-16 items-center reveal" data-category="ml">
                        <div class="lg:col-span-5 space-y-8 order-2 lg:order-1 text-left">
                            <span class="text-teal-500 font-black text-xs uppercase tracking-[0.5em]">Data Science & AI</span>
                            <h3 class="text-4xl md:text-5xl font-bold tracking-tighter italic text-white">Agentic Natural Language To SQL</h3>
                            <p class="text-xl text-white/50 leading-relaxed">
                                A dynamic web application capable of converting natural language queries into accurate SQL statements using AI, executing them across multiple databases, and presenting results directly.
                            </p>
                            <div class="flex flex-wrap gap-2 pt-2">
                                <div class="tech-tag"><i class="devicon-typescript-plain colored"></i><span>TypeScript</span></div>
                                <div class="tech-tag"><i class="devicon-react-original colored"></i><span>React</span></div>
                                <div class="tech-tag"><i class="devicon-python-plain colored"></i><span>Python</span></div>
                            </div>
                            <div class="flex flex-wrap gap-4 pt-4">
                                <a href="https://github.com/abhishek18-blog/Natural-language-to-sql" target="_blank" class="px-8 py-3 bg-white/5 border border-white/10 rounded-full font-bold text-xs uppercase tracking-widest hover:bg-white/10 transition-all flex items-center gap-2">
                                    Repo <i data-lucide="github"></i>
                                </a>
                            </div>
                        </div>
                        <div class="lg:col-span-7 order-1 lg:order-2">
                            <div class="bento-card aspect-video group overflow-hidden border-teal-500/20 shadow-[0_0_80px_rgba(20,184,166,0.1)]">
                                <img src="nl_sql.png" class="w-full h-full object-cover transition-all duration-1000 group-hover:scale-105" onerror="this.src='https://images.unsplash.com/photo-1555949963-aa79dcee981c?q=80&w=2070&auto=format&fit=crop'">
                            </div>
                        </div>
                    </div>

                    <!-- Abstracts Research Hub -->
                    <div class="project-item grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-16 items-center reveal" data-category="web">
                        <div class="lg:col-span-7">
                            <div class="bento-card aspect-video group overflow-hidden border-blue-400/20 shadow-[0_0_80px_rgba(96,165,250,0.1)]">
                                <img src="abstracts.png" class="w-full h-full object-cover transition-all duration-1000 group-hover:scale-105" onerror="this.src='https://images.unsplash.com/photo-1456406644174-8ddd4cd52a06?q=80&w=2068&auto=format&fit=crop'">
                            </div>
                        </div>
                        <div class="lg:col-span-5 space-y-8 text-left">
                            <span class="text-blue-400 font-black text-xs uppercase tracking-[0.5em]">Web Development</span>
                            <h3 class="text-4xl md:text-5xl font-bold tracking-tighter italic text-white">Abstracts Research Hub</h3>
                            <p class="text-xl text-white/50 leading-relaxed">
                                A centralized platform for browsing, exploring, and contributing to academic abstracts and research papers with a clean, responsive UI.
                            </p>
                            <div class="flex flex-wrap gap-2 pt-2">
                                <div class="tech-tag"><i class="devicon-nextjs-plain colored"></i><span>Next.js</span></div>
                                <div class="tech-tag"><i class="devicon-react-original colored"></i><span>React</span></div>
                                <div class="tech-tag"><i class="devicon-tailwindcss-plain colored"></i><span>Tailwind</span></div>
                            </div>
                            <div class="flex flex-wrap gap-4 pt-4">
                                <a href="https://abstracts-research-hub.vercel.app/" target="_blank" class="px-8 py-3 bg-white text-black rounded-full font-bold text-xs uppercase tracking-widest btn-apple flex items-center gap-2">
                                    Launch Site <i data-lucide="external-link"></i>
                                </a>
                                <a href="https://github.com/abhishek18-blog/Abstracts-researchHub" target="_blank" class="px-8 py-3 bg-white/5 border border-white/10 rounded-full font-bold text-xs uppercase tracking-widest hover:bg-white/10 transition-all flex items-center gap-2">
                                    Repo <i data-lucide="github"></i>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>"""

# Find the start and end of the original Projects Gallery
start_marker = "        <!-- Projects Gallery -->"
end_marker = "        <!-- Footer -->"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + projects_section + "\n\n" + content[end_idx:]
    
    # Add JS script logic before </script>
    js_logic = """
        // Projects Filter Logic
        const projectFilter = document.getElementById('project-filter');
        const projectItems = document.querySelectorAll('.project-item');

        if (projectFilter) {
            projectFilter.addEventListener('change', (e) => {
                const category = e.target.value;
                projectItems.forEach(item => {
                    item.classList.remove('active');
                    if (category === 'all' || item.dataset.category === category) {
                        item.style.display = '';
                        // Short delay to allow display reset before re-triggering animation
                        setTimeout(() => item.classList.add('active'), 50);
                    } else {
                        item.style.display = 'none';
                    }
                });
                // Update lucide icons in case new elements are shown
                setTimeout(() => lucide.createIcons(), 50);
            });
        }
"""
    # Find last </script>
    script_end_idx = new_content.rfind("    </script>")
    if script_end_idx != -1:
        new_content = new_content[:script_end_idx] + js_logic + new_content[script_end_idx:]
    
    with open('index.html', 'w') as f:
        f.write(new_content)
    print("Successfully updated index.html")
else:
    print("Could not find start or end marker")

