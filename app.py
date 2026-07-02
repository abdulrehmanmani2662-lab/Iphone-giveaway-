import os
import requests
from flask import Flask, request, render_template_string

app = Flask(__name__)

# ⚠️ یہاں اپنی گوگل ایپ اسکرپٹ (Google Apps Script) کا URL ڈالیں
GOOGLE_SHEET_SCRIPT_URL = "YOUR_GOOGLE_SCRIPT_URL_HERE"

# الٹرا پریمیم ایچ ٹی ایم ایل ڈیزائن جو اب پائتھن کے اندر ہی سیٹ ہے
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ur" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ندیم نانی والا - آفیشل آئی فون پروگرام</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Nastaliq+Urdu:wght@400;700&family=Tajawal:wght@400;500;700&display=swap');
        body {
            font-family: 'Tajawal', sans-serif;
            background-color: #05070c;
            background-image: radial-gradient(circle at top, rgba(212, 175, 55, 0.07), transparent 50%);
        }
        .urdu-font { font-family: 'Noto Nastaliq Urdu', serif; }
        .glass { background: rgba(15, 19, 25, 0.7); backdrop-filter: blur(12px); }
        
        /* 3D گھومتے ہوئے باکس کی اینیمیشن */
        .scene { width: 140px; height: 220px; perspective: 600px; margin: 0 auto; }
        .cube { width: 100%; height: 100%; position: relative; transform-style: preserve-3d; animation: spin 8s infinite linear; }
        .cube__face { position: absolute; background: #111; border: 2px solid #d4af37; display: flex; align-items: center; justify-content: center; box-shadow: 0 0 15px rgba(212, 175, 55, 0.2); }
        .cube__face--front, .cube__face--back { width: 140px; height: 220px; }
        .cube__face--right, .cube__face--left { width: 40px; height: 220px; left: 50px; }
        .cube__face--top, .cube__face--bottom { width: 140px; height: 40px; top: 90px; }
        .cube__face--front  { transform: rotateY(0deg) translateZ(20px); }
        .cube__face--back   { transform: rotateY(180deg) translateZ(20px); }
        .cube__face--right  { transform: rotateY(90deg) translateZ(70px); }
        .cube__face--left   { transform: rotateY(-95deg) translateZ(70px); }
        .cube__face--top    { transform: rotateX(90deg) translateZ(110px); }
        .cube__face--bottom { transform: rotateX(-90deg) translateZ(110px); }
        @keyframes spin { from { transform: rotateX(-10deg) rotateY(0deg); } to { transform: rotateX(-10deg) rotateY(360deg); } }
    </style>
</head>
<body class="text-gray-100 min-h-screen flex flex-col justify-between">

    <div class="w-full max-w-4xl mx-auto mt-4 px-4">
        <div class="bg-gray-900/50 border border-dashed border-gray-700 rounded-xl p-4 text-center text-xs text-gray-500">
            📢 ADVERTISEMENT BANNER (PLACE YOUR GOOGLE ADS CODE HERE)
        </div>
    </div>

    <header class="text-center pt-12 pb-6 px-4 max-w-3xl mx-auto">
        <div class="flex justify-center mb-4">
            <svg class="w-10 h-10 fill-current text-white" viewBox="0 0 16 16">
                <path d="M11.182.008C11.148-.03 9.923.023 8.857 1.18c-1.066 1.156-.902 2.482-.878 2.516s1.52.087 2.475-1.258.762-2.391.728-2.43m3.314 11.733c-.048-.096-2.325-1.234-2.113-3.422s1.675-2.789 1.698-3.567c-.012-.007-1.145-.443-1.145-1.748s1.008-2.126 1.055-2.178c-.01-.017-.834-1.228-2.618-1.228-1.42 0-2.023.712-2.673.712-.66 0-1.405-.724-2.686-.724-2.457 0-3.57 2.126-3.57 4.14 0 1.94 1.123 5.483 3.6 5.483.56 0 1.254-.42 2.025-.42.78 0 1.455.43 2.155.43.34 0 .74-.044 1.12-.132a1.3 1.3 0 0 0 .584-.282z"/>
            </svg>
        </div>
        <h1 class="text-4xl md:text-6xl font-bold text-amber-400 mb-6 urdu-font leading-relaxed">ندیم نانی والا</h1>
        <h2 class="text-xl md:text-3xl font-semibold text-white">۱,۰۰۰ فری آئی فون پروگرام 🇵🇰</h2>
    </header>

    <main class="max-w-6xl w-full mx-auto px-4 py-4 grid grid-cols-1 lg:grid-cols-12 gap-8 items-start flex-grow">
        <div class="lg:col-span-5 space-y-6">
            <div class="glass p-6 rounded-2xl border border-gray-800 text-center shadow-xl">
                <div class="scene mb-4">
                    <div class="cube">
                        <div class="cube__face cube__face--front flex flex-col justify-between p-3 bg-black">
                            <span class="text-[10px] text-gray-500 font-mono self-start">iPhone 15 Pro</span>
                            <div class="text-amber-400 text-2xl font-bold"></div>
                            <span class="text-[9px] text-amber-500 font-bold border border-amber-500/30 px-1 rounded">FREE</span>
                        </div>
                        <div class="cube__face cube__face--back bg-zinc-900 text-amber-400 font-bold text-xl">1000 Pcs</div>
                        <div class="cube__face cube__face--right bg-zinc-950"></div>
                        <div class="cube__face cube__face--left bg-zinc-950"></div>
                        <div class="cube__face cube__face--top bg-zinc-900"></div>
                        <div class="cube__face cube__face--bottom bg-zinc-900"></div>
                    </div>
                </div>
                <p class="text-xs text-amber-400 font-mono tracking-widest mt-2">3D IPHONE BOX LIVE PREVIEW</p>
            </div>

            <div class="glass p-6 rounded-2xl border border-gray-800 space-y-4">
                <h3 class="text-lg font-bold text-amber-400 border-b border-gray-800 pb-2">📌 طریقہ کار</h3>
                <ul class="space-y-3 text-sm text-gray-300">
                    <li>🔹 ایزی پیسہ یا جاز کیش اکاؤنٹ پر <strong>500 روپے</strong> فیس بھیجیں۔</li>
                    <li>🔹 فیس بھیجنے کے بعد ٹرانزیکشن آئی ڈی (Txn ID) فارم میں درج کریں۔</li>
                </ul>
            </div>
            
            <div class="hidden lg:block bg-gray-900/30 border border-dashed border-gray-800 rounded-xl p-6 text-center text-xs text-gray-500">
                📢 ADVERTISEMENT (SIDE BAR AD)
            </div>
        </div>

        <div class="lg:col-span-7 bg-gradient-to-b from-gray-1000 to-gray-950 p-6 md:p-8 rounded-2xl border border-gray-800 shadow-2xl">
            <h3 class="text-xl font-bold text-white mb-6 text-center">آفیشل رجسٹریشن فارم</h3>
            
            <form id="iphoneForm" action="/register" method="POST" class="space-y-5">
                <div>
                    <label class="block text-xs text-gray-400 mb-1.5">پورا نام (Full Name)</label>
                    <input type="text" name="name" required class="w-full bg-gray-900 border border-gray-800 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-amber-500 text-sm" placeholder="Ali Khan">
                </div>

                <div>
                    <label class="block text-xs text-gray-400 mb-1.5">موبائل نمبر (WhatsApp Number)</label>
                    <input type="tel" name="phone" required class="w-full bg-gray-900 border border-gray-800 rounded-xl px-4 py-3 text-white text-left focus:outline-none focus:border-amber-500 font-mono text-sm" placeholder="03001234567" dir="ltr">
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-xs text-gray-400 mb-1.5">پیمنٹ کا طریقہ</label>
                        <select name="method" class="w-full bg-gray-900 border border-gray-800 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-amber-500 text-sm">
                            <option>Easypaisa</option>
                            <option>JazzCash</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-xs text-gray-400 mb-1.5">ٹرانزیکشن آئی ڈی (Txn ID)</label>
                        <input type="text" name="txnid" required class="w-full bg-gray-900 border border-gray-800 rounded-xl px-4 py-3 text-white text-left focus:outline-none focus:border-amber-500 font-mono text-sm" placeholder="Code" dir="ltr">
                    </div>
                </div>

                <button type="submit" id="submitBtn" class="w-full bg-amber-500 hover:bg-amber-600 text-black font-bold py-3.5 rounded-xl transition-all shadow-lg text-sm mt-2">
                    **رجسٹریشن مکمل کریں** 🚀
                </button>
            </form>

            <div class="mt-6 bg-gray-900/40 border border-dashed border-gray-800 rounded-xl p-4 text-center text-xs text-gray-500">
                📢 ADVERTISEMENT (BOTTOM AD)
            </div>
        </div>
    </main>

    <footer class="text-center py-6 text-xs text-gray-600 border-t border-gray-950 mt-8">
        <p>© 2026 ندیم نانی والا آفیشل پروگرام۔ تمام حقوق محفوظ ہیں۔</p>
    </footer>

    <script>
        document.getElementById('iphoneForm').addEventListener('submit', function() {
            var btn = document.getElementById('submitBtn');
            btn.disabled = true;
            btn.innerHTML = "پروسیسنگ ہو رہی ہے...";
            btn.classList.add('opacity-50', 'cursor-not-allowed');
        });
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    # سنگل فائل سے ڈائریکٹ ایچ ٹی ایم ایل رینڈر کرنا
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

        # گوگل شیٹ پر ڈیٹا فارورڈ کرنا
        response = requests.post(GOOGLE_SHEET_SCRIPT_URL, data=user_data, timeout=10)
        
        if response.status_code == 200:
            return """
            <div style="background-color: #05070c; color: white; text-align: center; padding: 50px; font-family: sans-serif; min-height: 100vh; display: flex; flex-direction: column; justify-content: center; align-items: center;">
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
