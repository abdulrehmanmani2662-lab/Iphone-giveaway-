import os
import requests
from flask import Flask, request, render_template_string

app = Flask(__name__)

# ⚠️ یہاں اپنا نیا گوگل ایپ اسکرپٹ کا لنک پیسٹ کریں جانی
GOOGLE_SHEET_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbx8tiCKXHAWsYq60qyG5WjYmdVUdsyHr33BbkiYqP44rsWEF2GEZfPqf86vILzT48s8/exec"

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
            background-image: radial-gradient(circle at top, rgba(212, 175, 55, 0.08), transparent 50%);
        }
        .urdu-font { font-family: 'Noto Nastaliq Urdu', serif; }
        .glass { background: rgba(10, 15, 24, 0.75); backdrop-filter: blur(16px); }
        
        /* 3D ROTATING BOX */
        .scene { width: 160px; height: 260px; perspective: 1000px; margin: 0 auto; }
        .cube { width: 100%; height: 100%; position: relative; transform-style: preserve-3d; animation: spin 12s infinite linear; }
        .cube__face { 
            position: absolute; 
            background: #090d14; 
            border: 2px solid #d4af37; 
            display: flex; 
            flex-direction: column;
            align-items: center; 
            justify-content: space-between; 
            box-shadow: 0 0 25px rgba(212, 175, 55, 0.25);
            overflow: hidden;
            border-radius: 8px;
        }
        
        .cube__face--front, .cube__face--back { width: 160px; height: 260px; }
        .cube__face--right, .cube__face--left { width: 40px; height: 260px; left: 60px; }
        .cube__face--top, .cube__face--bottom { width: 160px; height: 40px; top: 110px; }
        
        .cube__face--front  { transform: rotateY(0deg) translateZ(20px); }
        .cube__face--back   { transform: rotateY(180deg) translateZ(20px); }
        .cube__face--right  { transform: rotateY(90deg) translateZ(80px); }
        .cube__face--left   { transform: rotateY(-90deg) translateZ(80px); }
        .cube__face--top    { transform: rotateX(90deg) translateZ(130px); }
        .cube__face--bottom { transform: rotateX(-90deg) translateZ(130px); }
        
        @keyframes spin { from { transform: rotateX(-10deg) rotateY(0deg); } to { transform: rotateX(-10deg) rotateY(360deg); } }
    </style>
</head>
<body class="text-gray-200 min-h-screen flex flex-col justify-between">

    <div class="w-full max-w-4xl mx-auto mt-4 px-4">
        <div class="bg-amber-500/5 border border-dashed border-amber-500/20 rounded-xl p-3 text-center text-xs text-amber-500/50 tracking-wider">
            📢 ADVERTISEMENT BANNER (PLACE YOUR GOOGLE ADS CODE HERE)
        </div>
    </div>

    <header class="text-center pt-8 pb-4 px-4 max-w-3xl w-full mx-auto">
        <div class="bg-gradient-to-r from-amber-500/10 via-amber-500/20 to-amber-500/10 border-2 border-amber-500/40 rounded-2xl py-5 px-6 shadow-[0_0_30px_rgba(212,175,55,0.15)] mb-4">
            <div class="flex justify-center mb-1">
                <span class="text-amber-400 text-2xl drop-shadow-[0_0_8px_rgba(212,175,55,0.6)]"></span>
            </div>
            <h1 class="text-4xl md:text-5xl font-black text-amber-400 urdu-font tracking-wide drop-shadow-lg mb-2">ندیم نانی والا</h1>
            <p class="text-xs md:text-sm font-bold text-gray-300 tracking-widest uppercase">آفیشل آئی فون 17 پرو گیو اوے پروگرام 🇵🇰</p>
        </div>
    </header>

    <main class="max-w-6xl w-full mx-auto px-4 py-4 grid grid-cols-1 lg:grid-cols-12 gap-8 items-start flex-grow">
        <div class="lg:col-span-5 space-y-6">
            
            <div class="glass p-4 rounded-2xl border border-amber-500/20 overflow-hidden shadow-2xl">
                <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold bg-amber-500/10 text-amber-400 border border-amber-500/20 mb-3">
                    🔴 اہم ویڈیو پیغام لازمی دیکھیں
                </span>
                <div class="relative pt-[177.77%] w-full rounded-xl overflow-hidden bg-black">
                    <iframe class="absolute inset-0 w-full h-full" src="YOUR_VIDEO_EMBED_URL" title="Video" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                </div>
            </div>

            <div class="glass p-6 rounded-2xl border border-gray-800 text-center shadow-2xl">
                <div class="scene mb-4">
                    <div class="cube">
                        <div class="cube__face cube__face--front bg-black relative p-2">
                            <span class="text-[10px] text-amber-400 font-bold tracking-tight z-10">iPhone 17 Pro Max</span>
                            <div class="w-full h-[190px] rounded-md overflow-hidden z-10 border border-zinc-900 bg-cover bg-center" style="background-image: url('https://images.unsplash.com/photo-1695048133142-1a20484d2569?auto=format&fit=crop&w=300&q=80');"></div>
                            <span class="text-[9px] text-black font-extrabold bg-amber-400 px-2 py-0.5 rounded shadow-md z-10 mb-1">PREMIUM LIVE</span>
                        </div>
                        <div class="cube__face cube__face--back bg-zinc-950 p-3">
                            <div class="text-amber-400 text-4xl font-bold drop-shadow-[0_0_8px_rgba(212,175,55,0.6)]"></div>
                            <span class="text-[10px] text-zinc-400 font-mono">Titanium Finish</span>
                            <span class="text-[10px] text-emerald-400 font-bold tracking-wider">PCS 1000 APPROVED</span>
                        </div>
                        <div class="cube__face cube__face--right bg-zinc-900 text-[8px] text-zinc-500 font-mono font-bold uppercase tracking-widest rotate-90">iPhone 17 Pro</div>
                        <div class="cube__face cube__face--left bg-zinc-900 text-[8px] text-zinc-500 font-mono font-bold uppercase tracking-widest -rotate-90">iPhone 17 Pro</div>
                        <div class="cube__face cube__face--top bg-zinc-950 text-amber-400 text-xs"></div>
                        <div class="cube__face cube__face--bottom bg-zinc-950 text-amber-400 text-xs"></div>
                    </div>
                </div>
                <p class="text-xs text-amber-400 font-mono tracking-widest mt-4">✨ iPHONE 17 PRO 3D PREVIEW ✨</p>
            </div>

            <div class="glass p-6 rounded-2xl border-2 border-amber-500/30 space-y-4 shadow-xl">
                <h3 class="text-lg font-bold text-amber-400 border-b border-gray-800 pb-2 urdu-font">📌 فیس جمع کروانے کا طریقہ</h3>
                <ul class="space-y-3 text-sm text-gray-300">
                    <li>🔹 نیچے دیے گئے نمبر پر اکاؤنٹ چیک کر کے <strong>500 روپے</strong> فیس بھیجیں۔</li>
                    <li>🔹 فیس بھیجنے کے بعد ملنے والی ٹرانزیکشن آئی ڈی (Txn ID) فارم میں درج کریں۔</li>
                </ul>
                
                <div class="bg-black/60 p-4 rounded-xl border border-gray-800 font-mono space-y-3 text-right text-xs">
                    <div class="border-b border-gray-900 pb-2">
                        <span class="text-amber-500 font-bold">💵 EASYPAISA DETAILS:</span>
                        <div class="flex justify-between mt-1"><span class="text-gray-400">Number:</span> <span class="text-white font-bold tracking-wider">03256286027</span></div>
                        <div class="flex justify-between"><span class="text-gray-400">Name:</span> <span class="text-gray-300">Muhammad Nadeem</span></div>
                    </div>
                    <div>
                        <span class="text-red-400 font-bold">📱 JAZZCASH DETAILS:</span>
                        <div class="flex justify-between mt-1"><span class="text-gray-400">Number:</span> <span class="text-white font-bold tracking-wider">03256286027</span></div>
                        <div class="flex justify-between"><span class="text-gray-400">Name:</span> <span class="text-gray-300">Muhammad Nadeem</span></div>
                    </div>
                </div>
            </div>
        </div>

        <div class="lg:col-span-7 bg-gradient-to-b from-slate-950 to-black p-6 md:p-8 rounded-2xl border border-amber-500/10 shadow-2xl flex flex-col justify-between h-full">
            <div>
                <h3 class="text-2xl font-bold text-white mb-6 text-center tracking-wide urdu-font">آفیشل رجسٹریشن فارم</h3>
                
                <form id="iphoneForm" class="space-y-5">
                    <div>
                        <label class="block text-xs text-gray-400 mb-1.5 font-medium">پورا نام (Full Name)</label>
                        <input type="text" id="form_name" name="name" required class="w-full bg-[#0d131f] border border-gray-800 rounded-xl px-4 py-3.5 text-white focus:outline-none focus:border-amber-500 text-sm transition-colors" placeholder="Ali Khan">
                    </div>

                    <div>
                        <label class="block text-xs text-gray-400 mb-1.5 font-medium">موبائل نمبر (WhatsApp Number)</label>
                        <input type="tel" id="form_phone" name="phone" required class="w-full bg-[#0d131f] border border-gray-800 rounded-xl px-4 py-3.5 text-white text-left focus:outline-none focus:border-amber-500 font-mono text-sm transition-colors" placeholder="03001234567" dir="ltr">
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div>
                            <label class="block text-xs text-gray-400 mb-1.5 font-medium">آئی فون کا کلر (Select Color)</label>
                            <select id="form_color" name="color" class="w-full bg-[#0d131f] border border-gray-800 rounded-xl px-4 py-3.5 text-white focus:outline-none focus:border-amber-500 text-sm">
                                <option value="Desert Titanium">Desert Titanium</option>
                                <option value="Natural Titanium">Natural Titanium</option>
                                <option value="Black Titanium">Black Titanium</option>
                                <option value="White Titanium">White Titanium</option>
                            </select>
                        </div>
                        <div>
                            <label class="block text-xs text-gray-400 mb-1.5 font-medium">سٹوریج کپیسٹی (Select Storage)</label>
                            <select id="form_storage" name="storage" class="w-full bg-[#0d131f] border border-gray-800 rounded-xl px-4 py-3.5 text-white focus:outline-none focus:border-amber-500 text-sm">
                                <option value="256GB">256GB</option>
                                <option value="512GB">512GB</option>
                                <option value="1TB">1TB</option>
                            </select>
                        </div>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div>
                            <label class="block text-xs text-gray-400 mb-1.5 font-medium">پیمنٹ کا طریقہ</label>
                            <select id="form_method" name="method" class="w-full bg-[#0d131f] border border-gray-800 rounded-xl px-4 py-3.5 text-white focus:outline-none focus:border-amber-500 text-sm">
                                <option value="Easypaisa">Easypaisa</option>
                                <option value="JazzCash">JazzCash</option>
                            </select>
                        </div>
                        <div>
                            <label class="block text-xs text-gray-400 mb-1.5 font-medium">ٹرانزیکشن آئی ڈی (Txn ID)</label>
                            <input type="text" id="form_txnid" name="txnid" required class="w-full bg-[#0d131f] border border-gray-800 rounded-xl px-4 py-3.5 text-white text-left focus:outline-none focus:border-amber-500 font-mono text-sm transition-colors" placeholder="Code" dir="ltr">
                        </div>
                    </div>

                    <button type="submit" id="submitBtn" class="w-full bg-gradient-to-r from-amber-500 to-yellow-600 hover:from-amber-600 hover:to-yellow-700 text-black font-extrabold py-4 rounded-xl transition-all shadow-[0_4px_20px_rgba(212,175,55,0.3)] text-sm mt-3 uppercase tracking-wider">
                        رجسٹریشن مکمل کریں 🚀
                    </button>
                    
                    <div id="responseMessage" class="hidden text-center p-3 rounded-xl text-sm font-semibold mt-3"></div>
                </form>
            </div>

            <div class="mt-8 border-t border-gray-900 pt-6">
                <div class="glass p-4 rounded-xl border border-emerald-500/20 text-center">
                    <p class="text-xs text-gray-400 mb-3">اگر فارم جمع کرنے یا فیس بھیجنے میں کوئی مشکل آ رہی ہے تو بلا جھجھک ہمارے واٹس ایپ سپورٹ پر رابطہ کریں:</p>
                    <a href="https://wa.me/60143153573" target="_blank" class="inline-flex items-center gap-2 bg-emerald-600 hover:bg-emerald-700 text-white font-bold px-5 py-2.5 rounded-xl text-xs tracking-wide transition-all shadow-lg">
                        💬 آفیشل واٹس ایپ ہیلپ لائن (رابطہ کریں)
                    </a>
                </div>
            </div>
        </div>
    </main>

    <footer class="text-center py-6 text-xs text-gray-600 border-t border-zinc-950 mt-8">
        <p>© 2026 ندیم نانی والا آفیشل پروگرام۔ تمام حقوق محفوظ ہیں۔</p>
    </footer>

    <script>
        document.getElementById('iphoneForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            var btn = document.getElementById('submitBtn');
            var respDiv = document.getElementById('responseMessage');
            
            btn.disabled = true;
            btn.innerHTML = "پلیز انتظار کریں...";
            btn.classList.add('opacity-50', 'cursor-not-allowed');
            respDiv.classList.add('hidden');
            
            // سارا ڈیٹا جاوا اسکرپٹ کے ذریعے پکڑنا
            var name = document.getElementById('form_name').value;
            var phone = document.getElementById('form_phone').value;
            var color = document.getElementById('form_color').value;
            var storage = document.getElementById('form_storage').value;
            var method = document.getElementById('form_method').value;
            var txnid = document.getElementById('form_txnid').value;
            
            var formData = new FormData();
            formData.append('name', name);
            formData.append('phone', phone);
            formData.append('color', color);
            formData.append('storage', storage);
            formData.append('method', method);
            formData.append('txnid', txnid);
            
            fetch('/register', {
                method: 'POST',
                body: formData
            })
            .then(response => response.text())
            .then(data => {
                if(data.includes("SUCCESS_FLAG")) {
                    document.body.innerHTML = `
                    <div style="background-color: #030508; color: white; text-align: center; padding: 50px; font-family: sans-serif; min-height: 100vh; display: flex; flex-direction: column; justify-content: center; align-items: center; background-image: radial-gradient(circle at top, rgba(212, 175, 55, 0.1), transparent 50%);">
                        <h1 style="color: #d4af37; font-size: 36px; margin-bottom: 10px;">🎉 رجسٹریشن مکمل ہو گئی!</h1>
                        <p style="font-size: 18px; color: #cbd5e1;">آپ کی معلومات اور پسندیدہ آئی فون ماڈل لکی ڈرا سسٹم میں جمع ہو چکے ہیں۔</p>
                        <p style="color: #64748b; font-size: 14px; margin-top: 5px;">فیس کی تصدیق کے بعد آپ کو آفیشل واٹس ایپ پر میسج آ جائے گا۔</p>
                        <a href="/" style="margin-top: 25px; background-color: #d4af37; color: black; padding: 12px 24px; text-decoration: none; font-weight: bold; border-radius: 12px; box-shadow: 0 4px 15px rgba(212,175,55,0.3);">واپس ہوم پیج پر جائیں</a>
                    </div>`;
                } else {
                    btn.disabled = false;
                    btn.innerHTML = "رجسٹریشن مکمل کریں 🚀";
                    btn.classList.remove('opacity-50', 'cursor-not-allowed');
                    respDiv.innerHTML = "❌ " + data;
                    respDiv.className = "block text-center p-3 rounded-xl text-sm font-semibold mt-3 bg-red-500/10 text-red-400 border border-red-500/20";
                }
            })
            .catch(error => {
                btn.disabled = false;
                btn.innerHTML = "رجسٹریشن مکمل کریں 🚀";
                btn.classList.remove('opacity-50', 'cursor-not-allowed');
                respDiv.innerHTML = "❌ سرور سے رابطہ نہیں ہو سکا، دوبارہ کوشش کریں۔";
                respDiv.className = "block text-center p-3 rounded-xl text-sm font-semibold mt-3 bg-red-500/10 text-red-400 border border-red-500/20";
            });
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
            "color": request.form.get("color"),
            "storage": request.form.get("storage"),
            "method": request.form.get("method"),
            "txnid": request.form.get("txnid")
        }

        if not all(user_data.values()):
            return "جانی! تمام معلومات درست درج کریں۔", 400

        response = requests.post(GOOGLE_SHEET_SCRIPT_URL, data=user_data, timeout=15)
        
        if response.status_code == 200 and "Success" in response.text:
            return "SUCCESS_FLAG"
        else:
            return "گوگل شیٹ کنکشن کا مسئلہ ہے، دوبارہ کوشش کریں۔", 200

    except Exception as e:
        return "سرور ٹائم آؤٹ، براہ کرم دوبارہ فارم سبمٹ کریں۔", 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
