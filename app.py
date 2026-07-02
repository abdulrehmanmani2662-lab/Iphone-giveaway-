import os
import requests
from flask import Flask, request, render_template_string

app = Flask(__name__)

# ⚠️ یہاں اپنی گوگل ایپ اسکرپٹ (Google Apps Script) کا URL ڈالیں
GOOGLE_SHEET_SCRIPT_URL = "YOUR_GOOGLE_SCRIPT_URL_HERE"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ur" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ندیم نانی والا - آفیشل آئی فون پروگرام</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Nastaliq+Urdu:wght@400;700&family=Plus+Jakarta+Sans:wght@400;600;700&display=swap');
        
        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: #030508;
            background-image: radial-gradient(circle at top, rgba(212, 175, 55, 0.09), transparent 50%);
        }
        .urdu-font { font-family: 'Noto Nastaliq Urdu', serif; line-height: 2.2; }
        .glass { background: rgba(10, 15, 24, 0.75); backdrop-filter: blur(16px); }
        
        /* 3D ROTATING BOX WITH IMAGE & TEXT */
        .scene { width: 150px; height: 230px; perspective: 800px; margin: 0 auto; }
        .cube { width: 100%; height: 100%; position: relative; transform-style: preserve-3d; animation: spin 10s infinite linear; }
        .cube__face { 
            position: absolute; 
            background: #090d14; 
            border: 2px solid #d4af37; 
            display: flex; 
            flex-direction: column;
            align-items: center; 
            justify-content: center; 
            box-shadow: 0 0 20px rgba(212, 175, 55, 0.25);
            overflow: hidden;
        }
        
        .cube__face--front, .cube__face--back { width: 150px; height: 230px; }
        .cube__face--right, .cube__face--left { width: 45px; height: 230px; left: 52px; }
        .cube__face--top, .cube__face--bottom { width: 150px; height: 45px; top: 92px; }
        
        .cube__face--front  { transform: rotateY(0deg) translateZ(22px); }
        .cube__face--back   { transform: rotateY(180deg) translateZ(22px); }
        .cube__face--right  { transform: rotateY(90deg) translateZ(75px); }
        .cube__face--left   { transform: rotateY(-90deg) translateZ(75px); }
        .cube__face--top    { transform: rotateX(90deg) translateZ(115px); }
        .cube__face--bottom { transform: rotateX(-90deg) translateZ(115px); }
        
        @keyframes spin { from { transform: rotateX(-12deg) rotateY(0deg); } to { transform: rotateX(-12deg) rotateY(360deg); } }
    </style>
</head>
<body class="text-gray-200 min-h-screen flex flex-col justify-between">

    <div class="w-full max-w-4xl mx-auto mt-4 px-4">
        <div class="bg-amber-500/5 border border-dashed border-amber-500/20 rounded-xl p-4 text-center text-xs text-amber-500/60 tracking-wider">
            📢 ADVERTISEMENT BANNER (PLACE YOUR GOOGLE ADS CODE HERE)
        </div>
    </div>

    <header class="text-center pt-10 pb-4 px-4 max-w-3xl mx-auto">
        <div class="flex justify-center mb-3">
            <svg class="w-12 h-12 fill-current text-amber-400 drop-shadow-[0_0_10px_rgba(212,175,55,0.4)]" viewBox="0 0 16 16">
                <path d="M11.182.008C11.148-.03 9.923.023 8.857 1.18c-1.066 1.156-.902 2.482-.878 2.516s1.52.087 2.475-1.258.762-2.391.728-2.43m3.314 11.733c-.048-.096-2.325-1.234-2.113-3.422s1.675-2.789 1.698-3.567c-.012-.007-1.145-.443-1.145-1.748s1.008-2.126 1.055-2.178c-.01-.017-.834-1.228-2.618-1.228-1.42 0-2.023.712-2.673.712-.66 0-1.405-.724-2.686-.724-2.457 0-3.57 2.126-3.57 4.14 0 1.94 1.123 5.483 3.6 5.483.56 0 1.254-.42 2.025-.42.78 0 1.455.43 2.155.43.34 0 .74-.044 1.12-.132a1.3 1.3 0 0 0 .584-.282z"/>
            </svg>
        </div>
        <h1 class="text-5xl md:text-6xl font-bold text-amber-400 mb-4 urdu-font drop-shadow-md">ندیم نانی والا</h1>
        <h2 class="text-xl md:text-2xl font-semibold text-white tracking-wide">آفیشل آئی فون 17 پرو گیو اوے پروگرام 🇵🇰</h2>
    </header>

    <main class="max-w-6xl w-full mx-auto px-4 py-4 grid grid-cols-1 lg:grid-cols-12 gap-8 items-start flex-grow">
        <div class="lg:col-span-5 space-y-6">
            
            <div class="glass p-4 rounded-2xl border border-amber-500/20 overflow-hidden shadow-2xl">
                <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold bg-amber-500/10 text-amber-400 border border-amber-500/20 mb-3">
                    🔴 ندیم نانی والا کا اہم ویڈیو پیغام لازمی دیکھیں
                </span>
                <div class="relative pt-[177.77%] w-full rounded-xl overflow-hidden bg-black">
                    <iframe class="absolute inset-0 w-full h-full" src="YOUR_VIDEO_EMBED_URL" title="Nadeem Nani Wala Video" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                </div>
            </div>

            <div class="glass p-6 rounded-2xl border border-gray-800 text-center shadow-2xl">
                <div class="scene mb-4">
                    <div class="cube">
                        <div class="cube__face cube__face--front p-2 justify-between bg-black">
                            <span class="text-[11px] text-amber-400 font-bold tracking-tight">iPhone 17 Pro</span>
                            <div class="w-full h-32 flex items-center justify-center bg-zinc-950 rounded-lg border border-zinc-900 my-1">
                                <svg class="w-16 h-16 text-zinc-500 fill-current" viewBox="0 0 16 16">
                                    <path d="M11 1H5a1 1 0 0 0-1 1 v12a1 1 0 0 0 1 1 h6a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1zM5 0h6a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2z"/>
                                    <path d="M8 14a1 1 0 1 0 0-2 1 1 0 0 0 0 2z"/>
                                </svg>
                            </div>
                            <span class="text-[10px] text-amber-500 font-bold bg-amber-500/10 px-2 py-0.5 rounded border border-amber-500/20">OFFICIAL BOX</span>
                        </div>
                        <div class="cube__face cube__face--back bg-zinc-950 p-2 justify-between">
                            <div class="text-amber-400 text-xl font-bold"></div>
                            <span class="text-xs text-zinc-400 font-mono">17 Pro Max Vibe</span>
                            <span class="text-[11px] text-emerald-400 font-bold">1000 PCS</span>
                        </div>
                        <div class="cube__face cube__face--right bg-zinc-900 text-[9px] text-zinc-400 font-mono font-bold uppercase tracking-widest rotate-90">iPhone 17</div>
                        <div class="cube__face cube__face--left bg-zinc-900 text-[9px] text-zinc-400 font-mono font-bold uppercase tracking-widest -rotate-90">iPhone 17</div>
                        <div class="cube__face cube__face--top bg-zinc-950 text-amber-400 text-xs"></div>
                        <div class="cube__face cube__face--bottom bg-zinc-950 text-amber-400 text-xs"></div>
                    </div>
                </div>
                <p class="text-xs text-amber-400 font-mono tracking-widest mt-2">✨ iPHONE 17 PRO 3D PREVIEW ✨</p>
            </div>

            <div class="glass p-6 rounded-2xl border border-gray-800 space-y-4">
                <h3 class="text-lg font-bold text-amber-400 border-b border-gray-800 pb-2">📌 طریقہ کار</h3>
                <ul class="space-y-3 text-sm text-gray-300">
                    <li>🔹 ایزی پیسہ یا جاز کیش اکاؤنٹ پر <strong>500 روپے</strong> فیس بھیجیں۔</li>
                    <li>🔹 فیس بھیجنے کے بعد ٹرانزیکشن آئی ڈی (Txn ID) فارم میں درج کریں۔</li>
                </ul>
            </div>
            
            <div class="hidden lg:block bg-amber-500/5 border border-dashed border-gray-800 rounded-xl p-6 text-center text-xs text-gray-600">
                📢 ADVERTISEMENT (SIDE BAR AD)
            </div>
        </div>

        <div class="lg:col-span-7 bg-gradient-to-b from-slate-950 to-black p-6 md:p-8 rounded-2xl border border-amber-500/10 shadow-2xl">
            <h3 class="text-2xl font-bold text-white mb-6 text-center tracking-wide">آفیشل رجسٹریشن فارم</h3>
            
            <form id="iphoneForm" action="/register" method="POST" class="space-y-5">
                <div>
                    <label class="block text-xs text-gray-400 mb-1.5 font-medium">پورا نام (Full Name)</label>
                    <input type="text" name="name" required class="w-full bg-[#0d131f] border border-gray-800 rounded-xl px-4 py-3.5 text-white focus:outline-none focus:border-amber-500 text-sm transition-colors" placeholder="Ali Khan">
                </div>

                <div>
                    <label class="block text-xs text-gray-400 mb-1.5 font-medium">موبائل نمبر (WhatsApp Number)</label>
                    <input type="tel" name="phone" required class="w-full bg-[#0d131f] border border-gray-800 rounded-xl px-4 py-3.5 text-white text-left focus:outline-none focus:border-amber-500 font-mono text-sm transition-colors" placeholder="03001234567" dir="ltr">
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-xs text-gray-400 mb-1.5 font-medium">پیمنٹ کا طریقہ</label>
                        <select name="method" class="w-full bg-[#0d131f] border border-gray-800 rounded-xl px-4 py-3.5 text-white focus:outline-none focus:border-amber-500 text-sm">
                            <option>Easypaisa</option>
                            <option>JazzCash</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-xs text-gray-400 mb-1.5 font-medium">ٹرانزیکشن آئی ڈی (Txn ID)</label>
                        <input type="text" name="txnid" required class="w-full bg-[#0d131f] border border-gray-800 rounded-xl px-4 py-3.5 text-white text-left focus:outline-none focus:border-amber-500 font-mono text-sm transition-colors" placeholder="Code" dir="ltr">
                    </div>
                </div>

                <button type="submit" id="submitBtn" class="w-full bg-gradient-to-r from-amber-500 to-yellow-600 hover:from-amber-600 hover:to-yellow-700 text-black font-extrabold py-4 rounded-xl transition-all shadow-[0_4px_20px_rgba(212,175,55,0.3)] text-sm mt-3 uppercase tracking-wider">
                    رجسٹریشن مکمل کریں 🚀
                </button>
            </form>

            <div class="mt-6 bg-amber-500/5 border border-dashed border-gray-800 rounded-xl p-4 text-center text-xs text-gray-600">
                📢 ADVERTISEMENT (BOTTOM AD)
            </div>
        </div>
    </main>

    <footer class="text-center py-6 text-xs text-gray-600 border-t border-zinc-950 mt-8">
        <p>© 2026 ندیم نانی والا آفیشل پروگرام۔ تمام حقوق محفوظ ہیں۔</p>
    </footer>

    <script>
        document.getElementById('iphoneForm').addEventListener('submit', function() {
            var btn = document.getElementById('submitBtn');
            btn.disabled = true;
            btn.innerHTML = "پلیز انتظار کریں...";
            btn.classList.add('opacity-50', 'cursor-not-allowed');
        });
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/register', methods=['POST'])
def register():
    try:
        user_data = {
            "name": request.form.get("name"),
            "phone": request.form.get("phone"),
            "method": request.form.get("method"),
            "txnid": request.form.get("txnid")
        }

        if not all(user_data.values()):
            return "جانی! تمام معلومات درست درج کریں۔", 400

        response = requests.post(GOOGLE_SHEET_SCRIPT_URL, data=user_data, timeout=10)
        
        if response.status_code == 200:
            return """
            <div style="background-color: #030508; color: white; text-align: center; padding: 50px; font-family: sans-serif; min-height: 100vh; display: flex; flex-direction: column; justify-content: center; align-items: center;">
                <h1 style="color: #d4af37;">🎉 رجسٹریشن مکمل ہو گئی!</h1>
                <p style="font-size: 18px; color: #cbd5e1;">آپ کی معلومات ندیم نانی والا آفیشل لکی ڈرا سسٹم میں جمع ہو چکی ہیں۔</p>
                <p style="color: #64748b; font-size: 14px;">فیس کی تصدیق کے بعد آپ کو واٹس ایپ پر میسج آ جائے گا۔</p>
                <a href="/" style="margin-top: 20px; background-color: #d4af37; color: black; padding: 10px 20px; text-decoration: none; font-weight: bold; border-radius: 8px;">واپس جائیں</a>
            </div>
            """
        else:
            return "گوگل شیٹ کنکشن کا مسئلہ ہے، دوبارہ کوشش کریں۔", 500

    except Exception as e:
        return "کچھ غلط ہو گیا، براہ کرم بعد میں کوشش کریں۔", 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
