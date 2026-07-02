import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width">
<link rel="icon" href="/favicon.ico?v=2">
<title>Etestpaper | MCQ</title>
<style>@import url(https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,400;0,500;0,600;0,700;1,400&display=swap); @import url(https://fonts.googleapis.com/css2?family=Noto+Sans+Bengali:wght@400;600;700&display=swap);</style>
<meta name="robots" content="index,follow">
<meta name="description" content="Practice and test MCQ and CQ questions for HSC exam preparation. Get model tests and suggestions to excel in your exams.">
<meta property="fb:app_id" content="etestpaper">
<meta property="og:title" content="Etestpaper | MCQ">
<meta property="og:description" content="Practice and test MCQ and CQ questions for HSC exam preparation. Get model tests and suggestions to excel in your exams.">
<meta property="og:url" content="https://www.etestpaper.net">
<meta property="og:type" content="website">
<meta property="og:locale" content="en_BD">
<meta property="og:site_name" content="etestpaper">
<meta name="next-head-count" content="14">
<meta charset="UTF-8">
<script src="https://cdn.tailwindcss.com"></script>
<script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          fontFamily: {
            sans: ['Inter', 'sans-serif'],
            poppins: ['Poppins', 'sans-serif'],
            noto: ['Noto Sans Bengali', 'sans-serif'],
          }
        }
      }
    }
</script>
</head>
<body class="bg-gray-50 dark:bg-slate-900 transition-colors duration-300">
<div id="__next">
<main class="min-h-screen">
  
  <!-- Sidebar -->
  <aside class="hidden lg:flex fixed inset-y-0 left-0 z-30 flex-col bg-white dark:bg-gray-900 border-r border-gray-100 dark:border-gray-800 transition-all duration-300 w-64">
    <div class="shrink-0 border-b border-gray-100 dark:border-gray-800 transition-all duration-300 px-4 py-4">
      <div class="flex items-center justify-between">
        <a href="index.html">
          <div class="h-[28px] w-[62px] relative">
            <h1 class="text-xl font-bold text-sky-600">eTestPaper</h1>
          </div>
        </a>
      </div>
    </div>
    
    <nav class="flex-1 overflow-y-auto py-3 px-2">
      <p class="px-3 pb-2 pt-1 text-[10px] font-bold text-gray-400 dark:text-gray-500 uppercase tracking-widest poppins">Menu</p>
      <div class="grid gap-0.5">
        <a class="noto flex items-center rounded-xl text-[13px] font-medium transition-all duration-200 gap-3 px-3 py-2.5 text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800/50" href="index.html">
          <span class="shrink-0 "><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5"><path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6A2.25 2.25 0 0 1 6 3.75h2.25A2.25 2.25 0 0 1 10.5 6v2.25a2.25 2.25 0 0 1-2.25 2.25H6a2.25 2.25 0 0 1-2.25-2.25V6ZM3.75 15.75A2.25 2.25 0 0 1 6 13.5h2.25a2.25 2.25 0 0 1 2.25 2.25V18a2.25 2.25 0 0 1-2.25 2.25H6A2.25 2.25 0 0 1 3.75 18v-2.25ZM13.5 6a2.25 2.25 0 0 1 2.25-2.25H18A2.25 2.25 0 0 1 20.25 6v2.25A2.25 2.25 0 0 1 18 10.5h-2.25a2.25 2.25 0 0 1-2.25-2.25V6ZM13.5 15.75a2.25 2.25 0 0 1 2.25-2.25H18a2.25 2.25 0 0 1 2.25 2.25V18A2.25 2.25 0 0 1 18 20.25h-2.25A2.25 2.25 0 0 1 13.5 18v-2.25Z"></path></svg></span>
          <span class="mt-0.5">Dashboard</span>
        </a>
        <a class="noto flex items-center rounded-xl text-[13px] font-medium transition-all duration-200 gap-3 px-3 py-2.5 bg-sky-50 dark:bg-sky-900/20 text-sky-700 dark:text-sky-300" href="subjects.html">
          <span class="shrink-0 text-sky-500"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6.042A8.967 8.967 0 0 0 6 3.75c-1.052 0-2.062.18-3 .512v14.25A8.987 8.987 0 0 1 6 18c2.305 0 4.408.867 6 2.292m0-14.25a8.966 8.966 0 0 1 6-2.292c1.052 0 2.062.18 3 .512v14.25A8.987 8.987 0 0 0 18 18a8.967 8.967 0 0 0-6 2.292m0-14.25v14.25"></path></svg></span>
          <span class="mt-0.5">Chapter Preparation</span>
        </a>
      </div>
    </nav>
  </aside>

  <!-- Main Content -->
  <div class="transition-all duration-300 lg:ml-64">
    <!-- Header -->
    <header class="w-full bg-white/80 dark:bg-gray-900/80 backdrop-blur-xl border-b border-gray-200/60 dark:border-gray-700/40 sticky top-0 z-30">
      <div class="flex justify-between max-w-screen-2xl w-full mx-auto px-4 md:px-6 xl:px-8 items-center h-16">
        <div class="hidden gap-1.5 xl:gap-2 items-center lg:flex">
          <a class="text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800 noto duration-200 h-9 px-4 items-center text-sm font-medium flex rounded-full transition-all" href="index.html">
            <span class="inline-block align-middle mt-0.5">Home</span>
          </a>
        </div>
        <div class="flex items-center gap-3">
          <button id="themeToggleBtn" aria-label="Toggle dark mode" class="w-14 h-8 bg-gradient-to-r from-blue-100 to-purple-100 dark:from-gray-700 dark:to-gray-800 rounded-full p-1 transition-all duration-500 shadow-inner">
            <div class="relative h-6 w-6 rounded-full bg-white dark:bg-gray-900 shadow-md flex items-center justify-center transition-transform duration-500" id="themeToggleThumb">
              <span class="text-xs">☀️</span>
            </div>
          </button>
        </div>
      </div>
    </header>

    <!-- Breadcrumb -->
    <nav class="max-w-screen-2xl mx-auto w-full px-4 py-3">
      <ol class="flex flex-wrap items-center gap-1 text-sm">
        <li class="flex items-center"><a class="text-gray-500 hover:text-sky-500" href="/">Home</a></li>
        <li class="flex items-center text-gray-400">/</li>
        <li class="flex items-center"><a class="text-gray-500 hover:text-sky-500" href="#">ICT</a></li>
        <li class="flex items-center text-gray-400">/</li>
        <li class="flex items-center"><span class="text-gray-900 dark:text-white font-medium">Chapter 1 : Information and Communication Technology</span></li>
        <li class="flex items-center text-gray-400">/</li>
        <li class="flex items-center"><span class="text-sky-600 font-medium">MCQ</span></li>
      </ol>
    </nav>

    <!-- Filter Bar -->
    <div class="max-w-screen-2xl w-full mx-auto px-4 pt-5">
      <div class="flex flex-wrap items-center gap-3">
        <div class="inline-flex rounded-full bg-gray-100 dark:bg-slate-800 p-1">
          <button class="px-4 py-1.5 rounded-full text-sm font-medium bg-white dark:bg-slate-600 text-gray-900 dark:text-white shadow-sm">All</button>
          <button class="px-4 py-1.5 rounded-full text-sm font-medium text-gray-500 hover:text-gray-700 dark:hover:text-gray-200">College</button>
          <button class="px-4 py-1.5 rounded-full text-sm font-medium text-gray-500 hover:text-gray-700 dark:hover:text-gray-200">Board</button>
        </div>
        <div class="relative">
          <select class="appearance-none pl-4 pr-9 py-2 rounded-full text-sm font-medium border border-gray-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-gray-700 dark:text-gray-200 focus:outline-none shadow-sm cursor-pointer">
            <option value="">All Topics</option>
            <option value="vr">Virtual Reality</option>
            <option value="ai">Artificial Intelligence</option>
            <option value="nano">Nanotechnology</option>
          </select>
        </div>
      </div>
    </div>

    <!-- MCQ Container -->
    <div class="max-w-3xl mx-auto pb-6 px-2 mt-6">
      
      <!-- Top Title -->
      <div class="flex justify-between w-full items-center mb-6">
        <h2 class="text-lg lg:text-[24px] font-semibold items-center flex gap-4 text-gray-900 dark:text-white">
          <svg class="hidden md:block" width="88" height="9" viewBox="0 0 88 9" fill="none"><rect width="88" height="9" rx="4.5" fill="#047FDB"></rect></svg>
          <span>Practice MCQ</span>
        </h2>
        <div class="flex items-center gap-1 md:gap-3 px-4 md:px-0 py-4 justify-center">
          <h2 class="font-semibold text-gray-500 text-md lg:text-xl">Show Ans:</h2>
          <button id="globalShowAnsToggle" class="relative inline-flex items-center md:h-7 md:w-14 h-5 w-10 cursor-pointer rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out bg-gray-400">
            <span class="inline-block md:h-6 md:w-6 w-4 h-4 rounded-full bg-white shadow-lg transform transition translate-x-0" id="globalShowAnsThumb"></span>
          </button>
        </div>
      </div>

      <!-- Question List -->
      <div class="grid gap-4" id="mcqListContainer">
        <!-- Questions injected via script below -->
      </div>
      
    </div>
  </div>
</main>
</div>

<!-- JS for Interactivity -->
<script>
    // Data definition for questions in English
    const questionsData = [
        {
            id: 1,
            text: "Which of the following languages is used in Artificial Intelligence?",
            meta: "Barisal Board · 2025",
            options: ["LISP", "CSS", "HTML", "SQL"],
            correctAnswer: 0
        },
        {
            id: 2,
            text: "<p>Read the following stem and answer the question:</p><p class='italic my-2 border-l-4 border-sky-400 pl-3'>'Through the extensive application of technology in the agricultural sector, it is possible to produce seasonal fruits all year round in Bangladesh.'</p><p>Q. The technology mentioned in the stem is-</p>",
            meta: "Comilla Board · 2024",
            options: ["Biometrics", "Genetic Engineering", "Bioinformatics", "Nanotechnology"],
            correctAnswer: 1
        },
        {
            id: 3,
            text: "<p>Read the following stem and answer the question:</p><p class='italic my-2 border-l-4 border-sky-400 pl-3'>'Through the extensive application of technology in the agricultural sector, it is possible to produce seasonal fruits all year round in Bangladesh.'</p><p>Q. Due to the impact of this technology-</p><p>i. Economic development will occur<br>ii. Biodiversity will be created<br>iii. Native species will become extinct</p><p>Which of the following is correct?</p>",
            meta: "Comilla Board · 2024",
            options: ["i & ii", "i & iii", "ii & iii", "i, ii & iii"],
            correctAnswer: 3
        },
        {
            id: 4,
            text: "Which one is an outsourcing marketplace?",
            meta: "Dhaka Board · 2023",
            options: ["Facebook", "MySpace", "Upwork", "Digg"],
            correctAnswer: 2
        },
        {
            id: 5,
            text: "What is the graphical representation using a combination of hardware and software called?",
            meta: "Rajshahi Board · 2025",
            options: ["Robotics", "Biometrics", "Virtual Reality", "Artificial Intelligence"],
            correctAnswer: 2
        },
        {
            id: 6,
            text: "<p>Read the following stem and answer the question:</p><p class='italic my-2 border-l-4 border-sky-400 pl-3'>Mr. Rajib has a human-like machine that has decision-making ability, walking capability, and tactile sensation. He receives treatment using cryogenic agents in tumor operations.</p><p>Q. Where is Mr. Rajib's machine used?</p>",
            meta: "Notre Dame College · 2024",
            options: ["In complex surgery treatment", "In identifying a person's signature", "In producing new varieties of seeds", "In making the shape of a tennis ball"],
            correctAnswer: 0
        },
        {
            id: 7,
            text: "<p>Read the following stem and answer the question:</p><p class='italic my-2 border-l-4 border-sky-400 pl-3'>Mr. Rajib has a human-like machine that has decision-making ability, walking capability, and tactile sensation. He receives treatment using cryogenic agents in tumor operations.</p><p>Q. The reasons Mr. Rajib took treatment in this method-</p><p>i. Comparatively low cost<br>ii. No need for surgery/cutting<br>iii. Long-term effectiveness</p><p>Which of the following is correct?</p>",
            meta: "Notre Dame College · 2024",
            options: ["i & ii", "i & iii", "ii & iii", "i, ii & iii"],
            correctAnswer: 0
        },
        {
            id: 8,
            text: "What is the design or pattern of biological characteristics called?",
            meta: "Sylhet Board · 2025",
            options: ["Gene", "Genome", "Nucleus", "Chromosome"],
            correctAnswer: 1
        },
        {
            id: 9,
            text: "Which one is an interdisciplinary science?",
            meta: "Dinajpur Board · 2024",
            options: ["Robotics", "Biometrics", "Bioinformatics", "Genetic Engineering"],
            correctAnswer: 2
        },
        {
            id: 10,
            text: "Which one is a behavioral biometric characteristic?",
            meta: "Comilla Victoria Government College · 2024",
            options: ["Fingerprint", "Iris", "Hand Geometry", "Signature"],
            correctAnswer: 3
        }
    ];

    const mcqListContainer = document.getElementById('mcqListContainer');
    
    let globalShowAns = false;
    
    function renderQuestions() {
        let html = '';
        questionsData.forEach((q, index) => {
            const optionsHtml = q.options.map((opt, optIndex) => `
                <button type="button" onclick="selectAnswer(${index}, ${optIndex})" id="opt-${index}-${optIndex}" class="group flex items-center gap-2.5 px-3 py-2 rounded-lg border transition-all duration-200 text-left bg-gray-50 dark:bg-gray-800 border-gray-200 dark:border-gray-700 hover:bg-sky-50 dark:hover:bg-sky-900/20 hover:border-sky-300 dark:hover:border-sky-600">
                    <span id="opt-badge-${index}-${optIndex}" class="shrink-0 w-6 h-6 rounded-full border-2 flex items-center justify-center text-[11px] font-bold poppins transition-all duration-200 bg-white dark:bg-gray-900 text-gray-500 dark:text-gray-400 border-gray-300 dark:border-gray-600 group-hover:border-sky-400 group-hover:text-sky-500">
                        ${String.fromCharCode(97 + optIndex)}
                    </span>
                    <span class="text-sm text-gray-700 dark:text-gray-300 flex-1">${opt}</span>
                </button>
            `).join('');

            html += `
            <div class="bg-white dark:bg-gray-900 rounded-2xl border border-gray-200 dark:border-gray-800 shadow-sm overflow-hidden mb-4">
                <div class="px-4 sm:px-5 pt-4 sm:pt-5 pb-3">
                    <div class="flex gap-3">
                        <span class="shrink-0 w-7 h-7 rounded-lg bg-sky-100 dark:bg-sky-900/30 text-sky-600 dark:text-sky-400 flex items-center justify-center text-xs font-bold poppins">${q.id}</span>
                        <div class="flex-1 min-w-0">
                            <div class="text-sm sm:text-base font-medium text-gray-800 dark:text-gray-200 leading-relaxed">
                                ${q.text}
                            </div>
                        </div>
                    </div>
                    <div class="flex items-center justify-between mt-3">
                        <p class="poppins text-[11px] text-gray-400 dark:text-gray-500">${q.meta}</p>
                    </div>
                </div>
                <div class="px-4 sm:px-5 pb-4 sm:pb-5 grid gap-1.5" id="options-${index}">
                    ${optionsHtml}
                </div>
            </div>
            `;
        });
        mcqListContainer.innerHTML = html;
    }

    // State array to track answered questions
    const answeredState = new Array(questionsData.length).fill(false);

    window.selectAnswer = function(qIndex, optIndex) {
        if(globalShowAns || answeredState[qIndex]) return; // locked if globally shown or already answered
        
        answeredState[qIndex] = true;
        const q = questionsData[qIndex];
        const selectedBtn = document.getElementById(`opt-${qIndex}-${optIndex}`);
        const selectedBadge = document.getElementById(`opt-badge-${qIndex}-${optIndex}`);
        
        // Highlight logic
        if(optIndex === q.correctAnswer) {
            // Correct
            selectedBtn.classList.add('bg-green-50', 'border-green-500', 'dark:bg-green-900/20', 'dark:border-green-600');
            selectedBadge.classList.add('bg-green-500', 'text-white', 'border-green-500');
        } else {
            // Incorrect
            selectedBtn.classList.add('bg-red-50', 'border-red-500', 'dark:bg-red-900/20', 'dark:border-red-600');
            selectedBadge.classList.add('bg-red-500', 'text-white', 'border-red-500');
            
            // Show correct answer
            const correctBtn = document.getElementById(`opt-${qIndex}-${q.correctAnswer}`);
            const correctBadge = document.getElementById(`opt-badge-${qIndex}-${q.correctAnswer}`);
            correctBtn.classList.add('bg-green-50', 'border-green-500', 'dark:bg-green-900/20', 'dark:border-green-600');
            correctBadge.classList.add('bg-green-500', 'text-white', 'border-green-500');
        }
    }

    // Global Show Ans Toggle
    const globalToggleBtn = document.getElementById('globalShowAnsToggle');
    const globalToggleThumb = document.getElementById('globalShowAnsThumb');

    globalToggleBtn.addEventListener('click', () => {
        globalShowAns = !globalShowAns;
        
        if (globalShowAns) {
            globalToggleBtn.classList.replace('bg-gray-400', 'bg-sky-500');
            globalToggleThumb.classList.add('translate-x-full');
            // Show all correct answers
            questionsData.forEach((q, index) => {
                const correctBtn = document.getElementById(`opt-${index}-${q.correctAnswer}`);
                const correctBadge = document.getElementById(`opt-badge-${index}-${q.correctAnswer}`);
                correctBtn.classList.add('bg-green-50', 'border-green-500', 'dark:bg-green-900/20', 'dark:border-green-600');
                correctBadge.classList.add('bg-green-500', 'text-white', 'border-green-500');
            });
        } else {
            globalToggleBtn.classList.replace('bg-sky-500', 'bg-gray-400');
            globalToggleThumb.classList.remove('translate-x-full');
            // Reset all if not answered
            renderQuestions(); // simple reset
            answeredState.fill(false);
        }
    });

    // Dark mode toggle
    const themeToggleBtn = document.getElementById('themeToggleBtn');
    themeToggleBtn.addEventListener('click', () => {
        document.documentElement.classList.toggle('dark');
    });

    // Initial render
    renderQuestions();
</script>

</body>
</html>
"""

with open("mcq.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated mcq.html")
